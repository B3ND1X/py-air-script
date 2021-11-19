#!/usr/bin/python
import os
import time
print("Scanning WiFi... hit Crtl + C to stop.")
os.system("sudo airmon-ng check kill")
os.system("sudo airmon-ng")
os.system("sudo airmon-ng start wlan0")
os.system("airodump-ng wlan0mon")

