# Development

### 1. Install and import necessary libraries to the mainApp.
#### a. Install PyQt5
 ```.sh
 pip install pyqt5
 ```
 #### b. Import libraries
 ```.py
 import sys, os, hashlib
 from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog, QLineEdit
 ```
### 2. Convert ui file to py file
```.sh
python3 pyuic.py name.ui -o name.py
```
### 3. Add all the Main Windows to the mainApp
#### a. Teacher App
```.py
class Home(QMainWindow, mainW):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.log_out)
        self.pushButton_3.clicked.connect(self.list_Q)
        self.pushButton_4.clicked.connect(self.grade)
        self.pushButton_5.clicked.connect(self.add)
        self.pushButton_6.clicked.connect(self.delete)
        self.pushButton_7.clicked.connect(self.edit)
        self.pushButton_8.clicked.connect(self.texport)

        logVar = log_in(self)
        logVar.show()

    def log_out(self):
        sys.exit(0)

    def list_Q(self):
        listq = listQ(self)
        listq.show()

    def grade(self):
        list_grade = grade(self)
        list_grade.show()

    def texport(self):
        Export = export(self)
        Export.show()

    def edit(self):
        Edit_S = edit_search(self)
        Edit_S.show()

    def delete(self):
        Delete = delete(self)
        Delete.show()

    def add(self):
        Add = add(self)
        Add.show()
```

#### b. Students App

### 4. Hash a password 
```.py
import hashlib
import os

password = "123456"
salt = os.urandom(32)   #This is the combination with the password, which makes the passwords harder to crack

key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt,1000) #encode the password with the hashlib library
```
### 5. Main Home Window
#### a.Teacher App

```.py
from teachers_ListFunct import Ui_MainWindow as mainW
from teachers_log_in import teacherLogin
from teachers_edit import teacherEdit
from teachers_delete import teacherDelete
from teachers_add import teacherAdd
from teachers_ListOfQuestions import teacherListOfQ
from teachers_grade import teacherGrade


class Home(QMainWindow, mainW):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.log_out)

        logVar = log_in(self)
        logVar.show()

    def log_out(self):
        sys.exit(0)


class log_in(teacherLogin):
    def __init__(self, parent=None):
        super(log_in, self).__init__(parent)
        self.setupUi(self)


class edit_search(teacherEdit):
    def __init__(self, parent=None):
        super(edit_search, self).__init__(parent)
        self.setupUi(self)


class delete(teacherDelete):
    def __init__(self, parent=None):
        super(delete, self).__init__(parent)
        self.setupUi(self)


class add(teacherAdd):
    def __init__(self, parent=None):
        super(add, self).__init__(parent)
        self.setupUi(self)


class listQ(teacherListOfQ):
    def __init__(self, parent=None):
        super(listQ, self).__init__(parent)
        self.setupUi(self)


class grade(teacherGrade):
    def __init__(self, parent=None):
        super(grade, self).__init__(parent)
        self.setupUi(self)


app = QApplication(sys.argv)  # creating the application with arguments from user
mainW = Home()  # setting the main window to the Home UI
mainW.show()
app.exec_()

```
#### b.Students App

### 6. Log In Window (For both Teacher and Students App)
  Due to the user would like to be the exclusive user for this app so that the username and the password do not need to change. Hence, I will just create a username and passwork right inside the Python file instead of storting it in the database file.
  
