import sys
from PyQt4 import QtGui,QtCore
import cv2

class MainScreen(QtGui.QWidget):
    
    def __init__(self):
        super(MainScreen, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        trainingButton = QtGui.QPushButton("Training")
        trainingButton.clicked.connect(self.training)
        detectButton = QtGui.QPushButton("Detect")
        detectButton.clicked.connect(self.detect)

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

    def training(self):
        trainingScreen = TrainingScreen()
        trainingScreen.show()
        # return trainingScreen

    def detect(self):
        detectScreen = DetectScreen()
        trainingScreen.show()
        return trainingScreen

    # def closeEvent(self, event):
        
    #     reply = QtGui.QMessageBox.question(self, 'Message',
    #         "Are you sure to quit?", QtGui.QMessageBox.Yes | 
    #         QtGui.QMessageBox.No, QtGui.QMessageBox.No)

    #     if reply == QtGui.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore() 


class TrainingScreen(QtGui.QWidget):
    """docstring for TrainingScreen"""
    def __init__(self):
        super(TrainingScreen, self).__init__()
        self.initUI()

    def initUI(self):
        
        addButton = QtGui.QPushButton("Add Employee")
        addButton.clicked.connect(self.addEmployee)
        editButton = QtGui.QPushButton("Edit Employee")
        editButton.clicked.connect(self.editEmployee)
        delButton = QtGui.QPushButton("Del Employee")
        delButton.clicked.connect(self.delEmployee)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(addButton)
        vbox.addWidget(editButton)
        vbox.addWidget(delButton)

        hbox = QtGui.QHBoxLayout()
        hbox.addLayout(vbox)
      
        self.setLayout(hbox)    
        
        self.setFixedSize(300,150)
        self.move(700,200)
        self.setWindowTitle('Training')      
        self.show()
        sys.exit(self.exec_())

    def addEmployee(self):
        addEmployee = AddEmployee()
        addEmployee.show()
        return addEmployee

    def editEmployee(self):
        editEmployee = EditEmployee()
        editEmployee.show()
        return editEmployee

    def delEmployee(self):
        delEmployee = DelEmployee()
        delEmployee.show()
        return delEmployee

    # def closeEvent(self, event):
    #     super(TrainingScreen, self).closeEvent(event)

class DetectScreen(QtGui.QWidget):
    
    def __init__(self):
        super(DetectScreen, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        nameLabel = QtGui.QLabel('Employee Name:')
        name = QtGui.QLabel('TuanND')
        statusLabel = QtGui.QLabel('Status:')
        status = QtGui.QLabel('Finding')

        backButton = QtGui.QPushButton("Back")

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(nameLabel, 1, 0)
        grid.addWidget(name, 1, 1)
        grid.addWidget(statusLabel, 2, 0)
        grid.addWidget(status, 2, 1)
        grid.addWidget(backButton, 3, 2)
      
        self.setLayout(grid)    
        
        self.setFixedSize(300,200)
        self.move(600,100)
        self.setWindowTitle('Detect')    
        self.show()
        sys.exit(self.exec_())

class AddEmployee(QtGui.QWidget):
    
    def __init__(self):
        super(AddEmployee, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        name = QtGui.QLabel('Employee Name')
        numberImage = QtGui.QLabel('Number Training Image: ')
        number = QtGui.QLabel('n')

        addButton = QtGui.QPushButton("Add Face")
        eraseButton = QtGui.QPushButton("Erase")
        doneButton = QtGui.QPushButton("Done")

        nameEdit = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1)
        grid.addWidget(numberImage, 2, 0)
        grid.addWidget(number, 2, 1)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(addButton)
        hbox.addWidget(eraseButton)
        hbox.addWidget(doneButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(hbox)
      
        self.setLayout(vbox)    
        
        self.setFixedSize(300,200)
        self.move(600,100)
        self.setWindowTitle('Add Employee')    
        self.show()
        sys.exit(self.exec_())

class EditEmployee(QtGui.QWidget):
    
    def __init__(self):
        super(EditEmployee, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        e1 = QtGui.QLabel('Employee 1')
        e2 = QtGui.QLabel('Employee 2')
        e3 = QtGui.QLabel('Employee 3')
        e4 = QtGui.QLabel('Employee 4')
        

        edit1 = QtGui.QPushButton("Edit")
        edit1.clicked.connect(self.editEmployeeDetail)
        edit2 = QtGui.QPushButton("Edit")
        edit2.clicked.connect(self.editEmployeeDetail)
        edit3 = QtGui.QPushButton("Edit")
        edit3.clicked.connect(self.editEmployeeDetail)
        edit4 = QtGui.QPushButton("Edit")
        edit4.clicked.connect(self.editEmployeeDetail)

        nameEdit = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(e1, 1, 0)
        grid.addWidget(edit1, 1, 1)
        grid.addWidget(e2, 2, 0)
        grid.addWidget(edit2, 2, 1)
        grid.addWidget(e3, 3, 0)
        grid.addWidget(edit3, 3, 1)
        grid.addWidget(e4, 4, 0)
        grid.addWidget(edit4, 4, 1)
      
        self.setLayout(grid)    
        
        self.setFixedSize(300,200)
        self.move(600,100)
        self.setWindowTitle('Edit Employee')    
        self.show()
        sys.exit(self.exec_())

    def editEmployeeDetail(self):
        editEmployeeDetail = EditEmployeeDetail()
        editEmployeeDetail.show()
        return editEmployeeDetail

class DelEmployee(QtGui.QWidget):
    
    def __init__(self):
        super(DelEmployee, self).__init__()
        
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
        sys.exit(self.exec_())

class EditEmployeeDetail(QtGui.QWidget):
    
    def __init__(self):
        super(EditEmployeeDetail, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        name = QtGui.QLabel('Employee Name')
        numberImage = QtGui.QLabel('Number Training Image: ')
        number = QtGui.QLabel('n')

        addButton = QtGui.QPushButton("Add Face")
        eraseButton = QtGui.QPushButton("Erase")
        doneButton = QtGui.QPushButton("Done")

        nameEdit = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1)
        grid.addWidget(numberImage, 2, 0)
        grid.addWidget(number, 2, 1)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(addButton)
        hbox.addWidget(eraseButton)
        hbox.addWidget(doneButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(hbox)
      
        self.setLayout(vbox)    
        
        self.setFixedSize(300,200)
        self.move(600,100)
        self.setWindowTitle('Edit Employee')    
        self.show()
        sys.exit(self.exec_())

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = MainScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()