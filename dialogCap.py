import cv2, os
import numpy as np
from PIL import Image
from PyQt4 import QtGui, QtCore

class DialogCapture(QtGui.QInputDialog):
    def __init__(self):

        # c = cv2.VideoCapture(0)

        QtGui.QInputDialog.__init__(self)

    def face_dialog(self):
        print "pressed Capture Face"
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter image face name:')
        
        if ok:
            print "image face name: " + text
            return text
        else:
            return