import sys
from PyQt4 import QtGui,QtCore
import cv2

class Screen3(QtGui.QWidget):
    
    def __init__(self):
        super(Screen3, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        e1 = QtGui.QLabel('Employee 1')
        e2 = QtGui.QLabel('Employee 2')
        e3 = QtGui.QLabel('Employee 3')
        e4 = QtGui.QLabel('Employee 4')

        del1 = QtGui.QPushButton("Del")
        del2 = QtGui.QPushButton("Del")
        del3 = QtGui.QPushButton("Del")
        del4 = QtGui.QPushButton("Del")

        nameEdit = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(e1, 1, 0)
        grid.addWidget(del1, 1, 1)
        grid.addWidget(e2, 2, 0)
        grid.addWidget(del2, 2, 1)
        grid.addWidget(e3, 3, 0)
        grid.addWidget(del3, 3, 1)
        grid.addWidget(e4, 4, 0)
        grid.addWidget(del4, 4, 1)
      
        self.setLayout(grid)    
        
        self.setFixedSize(300,200)
        self.move(600,100)
        self.setWindowTitle('Edit Employee')    
        self.show()
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
    
    # def webcam(self):
    #     cascPath = sys.argv[1]
    #     faceCascade = cv2.CascadeClassifier(cascPath)

    #     video_capture = cv2.VideoCapture(0)

    #     while True:
    #         # Capture frame-by-frame
    #         ret, frame = video_capture.read()

    #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #         faces = faceCascade.detectMultiScale(
    #             gray,
    #             scaleFactor=1.1,
    #             minNeighbors=5,
    #             minSize=(30, 30),
    #             flags=cv2.CASCADE_SCALE_IMAGE
    #         )

    #         # Draw a rectangle around the faces
    #         for (x, y, w, h) in faces:
    #             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #         # Display the resulting frame
    #         cv2.imshow('Video', frame)

    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break

    #     # When everything is done, release the capture
    #     video_capture.release()
    #     cv2.destroyAllWindows()
    	

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Screen3()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()