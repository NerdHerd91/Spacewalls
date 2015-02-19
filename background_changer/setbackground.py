#! /usr/bin/python

import ctypes
import os
from os.path import expanduser
import platform
import sys
import time
from threading import Thread
import urllib

# windows call to set wallpaper
SPI_SETDESKWALLPAPER = 20

image_url = "http://lorempixel.com/1920/1080/";
dest_path = expanduser("~") + "/image.jpg"

platform = platform.system()
if not(platform == "Linux" or platform == "Windows"):
    print "Your platform (" + platform + ") is not supported."
    sys.exit(-1)

def download(image_url, dest_path):
    print "starting download of: " + image_url
    f = urllib.urlopen(image_url)
    with open(dest_path, "wb") as imageFile:
        imageFile.write(f.read())
    print "wrote download to: " + dest_path

def changeBackground():
    download(image_url, dest_path)
    if platform == "Linux":
        os.system("gsettings set org.gnome.desktop.background picture-uri file://" + dest_path)
    if platform == "Windows":
        print "changing windows background"
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, dest_path, 0)
    print "background changed"


class UpdateBackgroundThread(Thread):
    def __init__(self):
        self.stopped = False
        Thread.__init__(self) #super constructor
    def run(self):
        while not self.stopped:
            changeBackground()
            time.sleep(3)


#UpdateBackgroundThread().start()

changeBackground()
