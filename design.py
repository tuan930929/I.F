from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):

        # c = cv2.VideoCapture(0)

        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Control Panel')

        self.capture = Capture()
        self.start_capture = QtGui.QPushButton('Start Capture',self)
        self.start_capture.clicked.connect(self.capture.start_capture)

        self.capture_face = QtGui.QPushButton('Capture Face',self)
        self.capture_face.clicked.connect(self.capture.capture_face)

        self.training_face = QtGui.QPushButton('Training Face',self)
        self.training_face.clicked.connect(self.capture.training_face)

        self.recognize_face = QtGui.QPushButton('Recognize Face',self)
        self.recognize_face.clicked.connect(self.capture.recognize_face)

        self.end_capture = QtGui.QPushButton('End Capture',self)
        self.end_capture.clicked.connect(self.capture.end_capture)

        self.quit_button = QtGui.QPushButton('Quit',self)
        self.quit_button.clicked.connect(self.capture.quit_capture)

        vbox = QtGui.QVBoxLayout(self)
        vbox.addWidget(self.start_capture)
        vbox.addWidget(self.capture_face)
        vbox.addWidget(self.training_face)
        vbox.addWidget(self.recognize_face)
        vbox.addWidget(self.end_capture)
        vbox.addWidget(self.quit_button)

        self.setLayout(vbox)
        self.setGeometry(200,200,300,300)
        self.show()