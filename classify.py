import tensorflow as tf
import sys
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def classify(image_path):
    # Read the image_data
    image_data = tf.io.gfile.GFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line in tf.io.gfile.GFile("tf_files/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.io.gfile.GFile("tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.compat.v1.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        predictions = sess.run(softmax_tensor, \
                {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        
        result = None
        for node_id in top_k:
            human_string = label_lines[node_id]
            accuracy = predictions[0][node_id]
            print('%s (score = %.5f)' % (human_string, accuracy))
            if accuracy >= 0.9:
                result = human_string
    return result

    print("Método para clasificar creado correctamente")

# Enable logging
try:
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
except Exception as e:
    print("Error logging {}".format(e.args))

def start(bot, update):
    try:
        username = update.message.from_user.username
        message = "Hello " + username
        update.message.reply_text(message)
    except Exception as e:
        print("Error start {}".format(e.args))


def help(bot, update):
    try:
        username = update.message.from_user.username
        update.message.reply_text('Hello {}, please send a image for classify'.format(username))
    except Exception as e:
        print("Error help {}".format(e.args))

def analize(bot, update):
    try:
        message = "Receiving image..."
        update.message.reply_text(message)
        print(message)
        
        photo_file = bot.getFile(update.message.photo[-1].file_id)
        id_user = update.message.from_user.id
        id_file = photo_file.file_id
        id_analisis = str(id_user) + "-" + str(id_file)
        
        filename = os.path.join('downloads/', '{}.jpg'.format(id_analisis))
        photo_file.download(filename)
        message = "Image received, analyzing, please wait a few seconds"
        update.message.reply_text(message)
        print(message)
        
        result = classify(filename)
        print(result)
        update.message.reply_text(result)
        print("Waiting image..")
    except Exception as e:
        print("Error analize {}".format(e.args))


def echo(bot, update):
    try:
        update.message.reply_text(update.message.text)
        print("Receiving text...")
        print("Waiting for another test...")
        print(update.message.from_user)
    except Exception as e:
        print("Error echo {}".format(e.args))

def error(bot, update, error):
    try:
        logger.warn('Update "%s" caused error "%s"' % (update, error))
    except Exception as e:
        print("Error error {}".format(e.args))

def main():
    try:
        print('ClassifyImagesBot init token')

        updater = Updater(TOKEN)
        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print('ClassifyImagesBot init dispatcher')


        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        # on noncommand detect the document type on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_handler(MessageHandler(Filters.photo, analize))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()
        print('ClassifyImagesBot ready')
        updater.idle()
    except Exception as e:
        print("Error main {}".format(e.message))

    print("Bot configurado correctamente")
    
if __name__ == '__main__':
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    url ='https://medium.com/shibinco/create-a-telegram-bot-using-botfather-and-get-the-api-token-900ba00e0f39'
    msg ="Please generate a telegram token for a new bot.\n\nFor a guide on how to get a token, go to:\n\n"
    print(msg,url)
    TOKEN = input('\nPlease input your telegram API token: ')
    try:
        main()
    except Exception as e:
        print("Error name: {}".format(e.args))