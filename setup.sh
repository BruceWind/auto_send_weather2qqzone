sudo apt-get install scons
sudo apt-get install libboost-dev libboost-thread-dev
sudo apt-get install libboost-system-dev libboost-python-dev
mkdir  PyV8download
cd PyV8download
wget https://github.com/emmetio/pyv8-binaries/raw/master/pyv8-linux64.zip

unzip pyv8-linux64.zip
sudo cp * /usr/lib/python2.7/dist-packages/
cd ../
## done

python test.py
