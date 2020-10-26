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
        export_t = export(self)
        export_t.show()

    def edit(self):
        edit_S = edit_search(self)
        edit_S.show()

    def delete(self):
        delete_t = delete(self)
        delete_t.show()

    def add(self):
        add_t = add(self)
        add_t.show()

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
 
 ```.py
    def __init__(self, parent=None):
        super(log_in, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.exit_app)
        self.pushButton.clicked.connect(self.enterApp)

    def exit_app(self):
        sys.exit(0)  # 0 mean without errors

    def enterApp(self):
        if self.lineEdit.text() == username and self.lineEdit_2.text() == password:  # Check if the
            # username and password
            # are correct
            self.close()
        else:
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
  ```
  ### 7. Teacher App Add New Questions
  ```.py
   class add(teacherAdd):

    def __init__(self, parent=None):
        super(add, self).__init__(parent)
        self.setupUi(self)

        # Set placeholder text for each input box
        self.lineEdit.setPlaceholderText("Enter the question")
        self.lineEdit_2.setPlaceholderText("Enter the answer A")
        self.lineEdit_3.setPlaceholderText("Enter the answer B")
        self.lineEdit_4.setPlaceholderText("Enter the answer C")
        self.lineEdit_5.setPlaceholderText("Enter the answer D")

        # Connect with the function when the button is clicked
        self.pushButton.clicked.connect(self.moreQ)
        self.pushButton_2.clicked.connect(self.cancelQ)
        self.pushButton_3.clicked.connect(self.createdQ)

    def moreQ(self):

        # Open database file with the name that is the date created
        date_created = datetime.datetime.now().strftime("%x")
        filename = date_created + ".txt"

        with open(filename, "a") as out_file_add:
            # Assign input text into variables
            stringQ = self.lineEdit.text() + " "
            stringaA = self.lineEdit_2.text() + " "
            stringaB = self.lineEdit_3.text() + " "
            stringaC = self.lineEdit_4.text() + " "
            stringaD = self.lineEdit_5.text() + " "
            string_correct_A = self.lineEdit_6.text() + "\n"

            # Write the input text into the data base file
            out_file_add.write(stringQ)
            out_file_add.write(stringaA)
            out_file_add.write(stringaB)
            out_file_add.write(stringaC)
            out_file_add.write(stringaD)
            out_file_add.write(string_correct_A)

        # Empty lineEdit so users can add another questions
        self.lineEdit.setText("")
        self.lineEdit2.setText("")
        self.lineEdit3.setText("")
        self.lineEdit4.setText("")
        self.lineEdit5.setText("")
        self.lineEdit6.setText("")
        self.lineEdit7.setText("")

    def createdQ(self):  # If the users press the create button, simply close the window
        self.close()

    def cancelQ(self):
        # If the user click close button => delete the database file.
        date_created = datetime.datetime.now().strftime("%x")
        filename = date_created + ".txt"

        if os.path.isfile(filename):
            os.remove(filename)
            self.close()
        else:
            self.close()
   ```
   
 ### 8. Teachers delete questions
  ```.py
class delete(teacherDelete):
    def __init__(self, parent=None):
        super(delete, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setPlaceholderText("Enter question ID: ")
        self.lineEdit_2.setPlaceholderText("Enter the file name: ")

        self.buttonBox.clicked.connect(self.deletef)

        def deletef(self):
            file_name = self.lineEdit_2.text()
            file_path = "Database/" + file_name + ".txt"
            output = []

            with open(file_path, "r+") as file:
                question_ID = self.lineEdit.text()
                for line in file:
                    if not line.startswith(question_ID):  # if the line not startwith the String Input, append it to
                        # the output list => The name                                          # deleted will no
                        # longer in the list
                        file.append(line)
                file.close()
                file = open(file_path, "w")
                file.writelines(output)  # Write the output list to the Database file
                file.close()

   ```
 ### 9. Teachers questions list
  ```.py
class listQ(teacherListOfQ):
    def __init__(self, parent=None):
        super(listQ, self).__init__(parent)
        self.setupUi(self)

        with open("DataBase/26-10-2020.csv") as mydatabase:  # Open the file
            file = csv.reader(mydatabase, delimiter=",")  # Split the data by the ","
            for i, row in enumerate(file):
                for j, col in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(col))  # Set the data to the table
   ``` 
