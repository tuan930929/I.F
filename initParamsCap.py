import cv2, os
import numpy as np
import requests
from PIL import Image
from PyQt4 import QtGui, QtCore

    def __init__(self):
        self.capturing = False
        self.has_faces = False
        self.has_training = False
        self.keyClock = "49281ca5b77add2379dd0470ec0c3339"
        self.cascPath = "haarcascades/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        self.recognizer = cv2.createLBPHFaceRecognizer()
        self.c = cv2.VideoCapture(0)
        self.images = []
        self.labels = []
        self.labels_name = []
        # self.images_path = "training_txt/images.txt"
        # self.labels_path = "training_txt/labels.txt"
        # self.labels_name_path = "training_txt/labels_name.txt"