#!/usr/bin/python
import os

os.system("sudo airmon-ng stop wlan0mon")
os.system("sudo ifconfig wlan0 up")
os.system("systemctl start NetworkManager")
print("Command executed successfully.")

