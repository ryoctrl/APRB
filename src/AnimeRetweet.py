import numpy as np
import cv2
import os
import sys
import glob
from matplotlib import pyplot as plt
import configparser

#config = ConfigParser.SafeConfigParser()
config = configparser.SafeConfigParser()
config.read("config.ini")

cascade_xml = config.get("settings", "cascade_xml")

def facedetect(file):
	###Settings
	scaleFactor = 1.03
	#scaleFactor = 1.0064
	nb = 5
	#nb = 2

	#face_cascade = cv2.CascadeClassifier('lbpcascade_animeface.xml')
	face_cascade = cv2.CascadeClassifier(cascade_xml)
	img = cv2.imread(file)
	gray = ""
	try:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	except:
		print("OpenCV Error")
		return False

	faces = face_cascade.detectMultiScale(gray, scaleFactor, nb, minSize=(100, 100))
	if len(faces) > 0:
		return True
	else:
		return False
