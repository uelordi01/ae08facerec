sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pip \
    zip
sudo apt-get clean
apt install python3-distro
sudo apt-get install cmake
sudo apt-update
sudo apt-get install libboost1.62-*
# sudo nano /etc/dphys-swapfile

# now install python libraries within this virtual environment
sudo sed -i 's/CONF_SWAPSIZE=100/CONF_SWAPSIZE=1024/g' /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start

git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git dlib/
sudo python3 setup.py install --compiler-flags "-mfpu=neon"
sudo apt-get install libatlas-base-dev
sudo apt-get install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test

sudo apt-get install libgtk-3-dev
sudo apt-get install libcanberra-gtk*
sudo apt-get install libatlas-base-dev gfortran
python -m pip install opencv-contrib-python==4.1.0.25
#change faceswap file
sudo sed -i 's/CONF_SWAPSIZE=1024/CONF_SWAPSIZE=100/g' /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start

sudo pip3 install face_recognition
#git clone --single-branch https://github.com/ageitgey/face_recognition.git

#get this tutorial repository:
git clone https://github.com/uelordi01/ae08facerec.git