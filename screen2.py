import sys
from PyQt4 import QtGui,QtCore

class Screen2(QtGui.QWidget):
    
    def __init__(self):
        super(Screen2, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        addButton = QtGui.QPushButton("Add Employee")
        # trainingButton.clicked.connect(self.training)
        editButton = QtGui.QPushButton("Edit Employee")
        delButton = QtGui.QPushButton("Del Employee")
        backButton = QtGui.QPushButton("Back")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(addButton)
        vbox.addWidget(editButton)
        vbox.addWidget(delButton)
        vbox.addWidget(backButton)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(vbox)
      
        self.setLayout(hbox)    
        
        self.setFixedSize(300,200)
        self.move(600,100)
        self.setWindowTitle('Training')    
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
    ex = Screen2()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()