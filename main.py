import sys
from PyQt4 import QtGui,QtCore

class MainScreen(QtGui.QWidget):
    
    def __init__(self):
        super(MainScreen, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        trainingButton = QtGui.QPushButton("Training")
        # trainingButton.clicked.connect(self.training)
        detectButton = QtGui.QPushButton("Detect")

        picture = QtGui.QLabel(self)
        picture.move(15, 10)
        pixmap = QtGui.QPixmap("timekeeper.png")
        pixmap1 = pixmap.scaled(480, 450)
        picture.setPixmap(pixmap1)
        picture.show()

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(trainingButton)
        hbox.addWidget(detectButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        self.setFixedSize(500,500)
        self.move(600,100)
        self.setWindowTitle('Timekeeper by Face Application')    
        self.show()
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
    
    # def training():
    	

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = MainScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()