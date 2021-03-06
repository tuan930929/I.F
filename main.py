import cv2, os
import numpy as np
import requests
from PIL import Image
from PyQt4 import QtGui, QtCore
# from faceFunc import Capture

class Capture():
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
        self.images_path = "training_txt/images.txt"
        self.labels_path = "training_txt/labels.txt"
        self.labels_name_path = "training_txt/labels_name.txt"

    def start_capture(self):
        print "pressed start"
        self.capturing = True
        cap = self.c
        while(self.capturing):
            self.has_faces = False
            #ret: true - false, frame: pixel array
            ret, frame = cap.read()
            # print("ret")
            # print(ret)
            # print("frame")
            # print(frame)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            # print("faces")
            # print(faces)
            if faces is None:
                self.has_faces = False
            # else:
            #     self.has_faces = True
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                self.has_faces = True

            # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()

    def get_image(self):
         retval, im = self.c.read()
         return im

    def capture_face(self):
        print("pressed Capture Face")
        if self.capturing == False:
            print("Need press Start Capture before!")
            return
        if self.has_faces == False:
            print("Detect no Face!")
            return
        dialog = DialogCapture()
        text = dialog.face_dialog()
        if text is None:
            return
        for i in xrange(30):
            temp = self.get_image()
        print("Taking image...")
        camera_capture = self.get_image()
        file = "training_images/" + text + ".png"
        print(file)
        cv2.imwrite(str(file), camera_capture)
        # print "pressed Capture Face"
        # text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
        #     'Enter image face name:')
        
        # if ok:
        #     print "image face name: " + text

    def training_face(self):
        print "pressed Training Face"
        self.images, self.labels, self.labels_name = self.get_images_and_labels()
        print("self.images")
        print(self.images)

        print("Opening the images.txt")
        self.images_txt = open(self.images_path,'w+')
        print "Truncating the file"
        #Empties the file
        self.images_txt.truncate()
        self.images_txt.write(str(self.images))
        self.images_content = self.images_txt.read()
        self.images_txt.close()
        print("Write to file images.txt success!")

        print("Opening the labels.txt")
        self.labels_txt = open(self.labels_path,'w+')
        print "Truncating the file"
        #Empties the file
        self.labels_txt.truncate()
        self.labels_txt.write(str(self.labels))
        self.labels_content = self.labels_txt.read()
        self.labels_txt.close()
        print("Write to file labels.txt success!")

        print("Opening the labels_name.txt")
        self.labels_name_txt = open(self.labels_name_path,'w')
        print "Truncating the file"
        #Empties the file
        self.labels_name_txt.truncate()
        self.labels_name_txt.write(str(self.labels_name))
        self.labels_name_txt.close()
        print("Write to file labels_name.txt success!")



        self.recognizer.train(self.images, np.array(self.labels))
        print("self.recognizer.train")
        print(self.recognizer.train(self.images, np.array(self.labels)))
        # print("self.images")
        # print(self.images)
        # print("self.labels")
        # print(self.labels)
        print("training face success!")
        self.has_training = True

    def recognize_face(self):
        print "pressed Recognize Face"
        if self.capturing == False:
            print("Need press Start Capture before!")
            return
        if self.has_training == False:
            print("Need Training Face before!")
            return
        if self.has_faces == False:
            print("Detect no Face!")
            return
        # self.capturing = True
        cap = self.c

        while(self.capturing):
            #ret: true - false, frame: pixel array
            ret, frame = cap.read()
            # print("ret")
            # print(ret)
            # print("frame")
            # print(frame)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # predict_image_pil = gray.convert('L')
            # predict_image = np.array(predict_image_pil, 'uint8')

            # faces = faceCascade.detectMultiScale(predict_image)

            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                #The more the value of "conf variable" is, the less the recognizer 
                #has confidence in the recognition. 
                # A "conf value" of 0.0 is a perfect recognition.
                nbr_predicted, conf = self.recognizer.predict(gray[y: y + h, x: x + w])

                for x in range(0, len(self.labels)):
                    if(self.labels[x] == nbr_predicted):
                        print "labels_name is: {} is Correctly Recognized with confidence {}".format(self.labels_name[x], conf)
                        data = {'email':self.labels_name[x],'key':self.keyClock}
                        r = requests.post("http://localhost/chamcong/pages/remoteAuth.php",params=data)
                        print(self.labels_name[x])
                        print(r.url)
                        print(r)
                        return self.labels_name[x]
                    else:
                        print "The face is Incorrect Recognized as {}".format(self.labels_name[x],nbr_predicted)
                print("Face is not in dataset")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()

    def end_capture(self):
        print "pressed End"
        self.capturing = False
        # cv2.destroyAllWindows()

    def quit_capture(self):
        print "pressed Quit"
        if self.capturing == True:
            print("Need press End Capture before")
            return
        cap = self.c
        cv2.destroyAllWindows()
        cap.release()
        QtCore.QCoreApplication.quit()

    def get_images_and_labels(self):
        # Append all the absolute image paths in a list image_paths
        # We will not read the image with the .sad extension in the training set
        # Rather, we will use them to test our accuracy of the training

        #name images like that: 1.tuannd.1.png - serials.name.numberFace.png
        path = '_training_images'
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        # images will contains face images
        images = []
        # labels will contains the label that is assigned to the image
        labels = []
        #labels_name will contains the name of label
        labels_name = []
        for image_path in image_paths:
            # Read the image and convert to grayscale
            image_pil = Image.open(image_path).convert('L')
            # Convert the image format into numpy array
            image = np.array(image_pil, 'uint8')
            # Get the label of the image
            nbr = int(os.path.split(image_path)[1].split("-")[0])
            lbn = os.path.split(image_path)[1].split("-")[1]
            # Detect the face in the image
            faces = self.faceCascade.detectMultiScale(image)
            # If face is detected, append the face to images and the label to labels
            for (x, y, w, h) in faces:
                images.append(image[y: y + h, x: x + w])
                labels.append(nbr)
                labels_name.append(lbn)
                # cv2.imshow("Adding faces to training set...", image[y: y + h, x: x + w])
                cv2.waitKey(50)
        # return the images list and labels list
        print("labels")
        print(labels)
        print("labels_name")
        print(labels_name)
        return images, labels, labels_name

class Window(QtGui.QWidget):
    def __init__(self):

        # c = cv2.VideoCapture(0)

        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Time Keeper')

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

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())