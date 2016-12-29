sudo apt-get install scons
sudo apt-get install libboost-dev libboost-thread-dev
sudo apt-get install libboost-system-dev libboost-python-dev
# PyV8 install
mkdir  PyV8download
cd PyV8download
wget https://github.com/emmetio/pyv8-binaries/raw/master/pyv8-linux64.zip
unzip pyv8-linux64.zip
sudo cp * /usr/lib/python2.7/dist-packages/
cd ../
## done

##
echo "请先修改 info.conf 设置qq 和 密码"

sudo ln -s /home/$USER/git/auto_send_weather2qqzone/send_shuo.py /usr/bin/sendweather2qqzone
chmod +x send_shuo.py

sendweather2qqzone

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "0 */1 * * * sendweather2qqzone" >> mycron
#install new cron file
crontab mycron
rm mycron
