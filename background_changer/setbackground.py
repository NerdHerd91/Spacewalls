#! /usr/bin/python

import ctypes
import os
from os.path import expanduser
import platform
import subprocess
import sys
import tempfile
import time
from threading import Thread
import urllib


image_url = "http://lorempixel.com/1920/1080/";

PLATFORM_LINUX = "Linux"
PLATFORM_OSX = "Darwin"
PLATFORM_WINDOWS = "Windows"

platform = platform.system()
if not(platform == PLATFORM_LINUX or platform == PLATFORM_OSX or platform == PLATFORM_WINDOWS):
    print "Your platform (" + platform + ") is not supported."
    sys.exit(-1)

def download(image_url, dest_path):
    print "starting download of: " + image_url
    f = urllib.urlopen(image_url)
    with open(dest_path, "wb") as imageFile:
        imageFile.write(f.read())
    print "wrote download to: " + dest_path

# windows call to set wallpaper
SPI_SETDESKWALLPAPER = 20

# applescript to set wallpaper
OSX_SET_WALLPAPER_APPLESCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def setBackground(image_path):
    if platform == PLATFORM_LINUX:
        os.system("gsettings set org.gnome.desktop.background picture-uri file://" + image_path)
    if platform == PLATFORM_OSX:
        subprocess.Popen(OSX_SET_WALLPAPER_APPLESCRIPT%image_path, shell=True)
    if platform == PLATFORM_WINDOWS:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 0)
    print "background changed"

def getImageFilename():
    if platform == PLATFORM_OSX:
        (fd, filename) = tempfile.mkstemp()
        return filename;
    else:
        return expanduser("~") + "/spacewalls_image.jpg"


def deleteTempImageIfNeeded(filename):
    if platform == PLATFORM_OSX:
        time.sleep(2) # setting the background fails if we don't wait before deleting
        os.remove(filename)

def updateBackground():
    image_file = getImageFilename();
    try:
        download(image_url, image_file)
        setBackground(image_file)          
    finally:
        deleteTempImageIfNeeded(image_file)

class UpdateBackgroundThread(Thread):
    def __init__(self):
        self.stopped = False
        Thread.__init__(self) #super constructor
    def run(self):
        while not self.stopped:
            updateBackground()
            time.sleep(5)


#UpdateBackgroundThread().start()

updateBackground()
