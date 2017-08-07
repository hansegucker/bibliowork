sudo apt install python3 python3-pip git
git clone https://github.com/hoffmann/googlebooks
cd googlebooks
sudo python3 setup.py install
cd ..
sudo rm -R -f googlebooks
