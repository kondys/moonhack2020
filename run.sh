wget https://github.com/KanoComputing/community-sdk/archive/python.zip -O community-sdk.zip.
unzip -j community-sdk.zip 'community-sdk-python/communitysdk/*' -d ./communitysdk. 
sudo pip3 install sphero_sprk
sudo python3 kano-sphero.py