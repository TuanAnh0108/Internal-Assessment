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

#### b.Students App

### 6. Log In Window (For both Teacher and Students App)
  Due to the user would like to be the exclusive user for this app so that the username and the password do not need to change. Hence, I will just create a username and passwork right inside the Python file instead of storting it in the database file.
  
