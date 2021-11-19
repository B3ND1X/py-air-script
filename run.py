#!/usr/bin/python
import os
os.system("./raspberry.sh")
os.system("sudo airmon-ng check kill")
os.system("sudo airmon-ng")
os.system("sudo airmon-ng start wlan0")
os.system("besside-ng wlam0mon")
os.system("sudo airmon-ng stop wlan0mon")
os.system("sudo ifconfig wlan0 up")
os.system("sudo systemctl start NetworkManager")
print("Done!")
