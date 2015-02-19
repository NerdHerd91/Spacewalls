#! /usr/bin/python

import os
import time
from threading import Thread
import urllib

image_url = "http://lorempixel.com/1920/1080/";
dest_path = "/home/justin/Pictures/wallpaper/image.jpg"

def download(image_url, dest_path):
    print "starting download of: " + image_url
    f = urllib.urlopen(image_url)
    with open(dest_path, "wb") as imageFile:
        imageFile.write(f.read())
    print "wrote download to: " + dest_path

def changeBackground():
    download(image_url, dest_path)
    os.system("gsettings set org.gnome.desktop.background picture-uri file://" + dest_path)
    print "background changed"


class UpdateBackgroundThread(Thread):
    def __init__(self):
        self.stopped = False
        Thread.__init__(self) #super constructor
    def run(self):
        while not self.stopped:
            changeBackground()
            time.sleep(3)


UpdateBackgroundThread().start()

#changeBackground()
