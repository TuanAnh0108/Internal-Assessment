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
