# Development

### All the code can be found in the code folder 


## Secured Log In

  An essential part of the program is implementing a secured login method. To make the data more privacy, an encrypted and secured password is crucial.
Due to the user do not want to change the username and password so I will set the username and password and store it inside the program for checking later when
the user enters the username and password for logging in.

**Encrypting the password string**
  ```.py
  import os
  import hashlib

  salt = os.urandom(32) # this creates a 32 bytes
  key = hashlib.pbkdf2_hmac("sha256", str(password).encode("utf-8"), salt, 1000)
  ```
To encrypt the password string both libraries `os` and `hashlib` must be imported.
`salt` is assigned as a string of size random bytes suitable for cryptographic use. More information can be found [here](https://www.geeksforgeeks.org/python-os-urandom-method/). In this example, the random string is 32 bytes.
`key` holds the encrypted password. The module `hashlib.pbkdf2_hmac()` is used with the secure hash algorithm SHA256. More information about this library and module can be found [here](https://docs.python.org/3/library/hashlib.html).

**Getting the username and password and check to confirm log in**

For the teacher app, there will be only one user uses it so that there is no need for store username and password in the database. Instead I will just store them
inside the program.

  ```.py
    username = "sensei"
    password = "sensei"
  ```

To log a student user in, the user must provide an username and password, which will be checked in the database of user credential ludes all of the users' encrypted credentials.
The database of user credentials is saved as `passwords.txt`, and includes all of the users' encrypted credentials.

The code is explained below:

1. The inputted usernam and password are stored
2. The `passwords.txt` file is opened and a for-loop iterates through the encrypted credentials
3. The `verify_password()` function is used to compare every stored password in the text file to the inputted `email + password`
4. If they are equal, the window closes (thus the user gains access to the main window) and they are logged in. The user's book database is loaded
5. If no credentials match, a pop-up is displayed showing an error message, and inputs are cleared


  ```.py
  def enterApp(self):
      username = self.lineEdit.text()
      password = self.lineEdit_2.text()
      
      with open("passwords.txt", "r") as passwordFile:
          for storedPassword in passwordFile:
              if verify_password(storedPassword, email + password):
                  self.close()

          QMessageBox.about(self, "Error", "Error: Wrong password")
          self.lineEdit.clear()
          self.lineEdit_2.clear()
  ```
## Integrating a Database

In the Japanese Learning system, it will stores the vocabulary, its definition, and quiz. This has to be achieved through a database, such that the information can be kept between user sessions.While database solutions such as SQL and SQLite could be chosen, a more practical and lightweight solution will be suitable for such a small-scale project. Thus, a `.csv` file is used to store the data, which can be accessed through the `csv` library in python (`import csv`).

