# tensorflow_testing_inception
Contains an example project of a classifier made of keyboards and pc mouses 
images to test the Inception already trained model using Tenserflow 1.14. 

## Requirements

* Python => 3.7
* PIP => 19.0
* Tensorflow = 1.14
* python-telegram-bot:latest

### Install requirements (System Install)

#### Ubuntu

```cmd
sudo apt update
sudo apt install python3-dev python3-pip
sudo pip3 install -U virtualenv  # system-wide install
```

#### MacOS

```cmd
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
export PATH="/usr/local/bin:/usr/local/sbin:$PATH"
brew update
brew install python  # Python 3
sudo pip3 install -U virtualenv  # system-wide install
```

#### Windows

Install the Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017, and 2019. Starting with the TensorFlow 2.1.0 version, the msvcp140_1.dll file is required from this package (which may not be provided from older redistributable packages). The redistributable comes with Visual Studio 2019 but can be installed separately:

Go to the Microsoft Visual C++ downloads,
Scroll down the page to the Visual Studio 2015, 2017 and 2019 section.
Download and install the Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017 and 2019 for your platform.
Make sure long paths are enabled on Windows.

Install the 64-bit Python 3 release for Windows (select pip as an optional feature).

```cmd
pip3 install -U pip virtualenv
```

### Check software versions

```cmd
python --version
python3 --version
pip3 --version
```

### Install Requirements

```cmd
pip3 install -r requirements.txt
```

#### More info in tenserflow installs: [Tenserflow PIP](https://www.tensorflow.org/install/pip)

## Setup

Once everything is installed you can start setting up the project. 

On your terminal enter:

```cmd
python3 setup.py
```

This should download Inception Trained Model to your project and start labeling
the images according to the name of the directory they are inside the 
directory training_datasets.

Once it finished the 500 step if everything goes right you can continue. If an
error occurs check your images in the folders to see if they are all there right
and also checking if the images are only on format 'jpg' and 'JPEG'.

## Run the Classifier

To execute just run the command: 

```cmd
python3 classify.py
```

Once you are there you will need to enter an telegram bot api token to connect
this app to your bot and start using it.

Once you entered it you can start using the chatbot sending images to the 
telegram bot and it will check if your image is a keyboard or a pc mouse.

Al files will be saved with the telegram user id and filename in your
downloads directory.

## Author
[thonnysee]

[Github](https://github.com/thonnysee)
