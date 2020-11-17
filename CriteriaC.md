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
## Database

In the Japanese Learning system, it will stores the vocabulary, its definition, and quiz. This has to be achieved through a database, such that the information can be kept between user sessions.While database solutions such as SQL and SQLite could be chosen, a more practical and lightweight solution will be suitable for such a small-scale project. Thus, a `.csv` file is used to store the data, which can be accessed through the `csv` library in python (`import csv`).

**Database for quizzes**

For the vocabulary used for quizzes, the data will be added manually. The vocabulary and its defintion will be seperated by `,` ;

    こんにちは,Hello
    おはようございます,Good morning
    こんばんは,Good Evening
    ありがとう,Thanks
    すみません,Sorry
    ただいま,I am home
    さようなら,Good Bye
    おやすみ,Good night

The reason for storing the data like this will be explained later in the part we access the database and seperate data by delimiter for the quizz.

**Writing input data into database**

A key component of the vocabulary list is that the users can add new vocabulary manually. This can be done by writing inputted vocabulary and its definiton into 
a `.csv` file so that the table can load the data from it. Moreover, if the vocabulary already exist in the file so there is no need to add the word into the file. Instead, the program will simply empty the input.
```.py
  def manual_vocab_add(self):
      # Assign variables to the input text
      new_vocab = self.lineEdit.text()
      new_definition = self.lineEdit_2.text()

      # Open the file to store all the new vocab
      with open("Students App/VocabList/VocabList.csv", "r+") as vocab_listFile:
          vocabL = []
          file = csv.reader(vocab_listFile, delimiter=",")  # Split the data by the ","
          for row in file:
              for vocab in row:
                  vocabL.append(vocab)  # Append all the words in the list into the vocab array

          # Check if the new word is in the file or not
          if new_vocab not in vocabL:
              vocab_listFile.write(new_vocab + ",")
              vocab_listFile.write(new_definition + "\n")

      # Empty the input space for users to continue inputting new words and definitions
      self.lineEdit.setText("")
      self.lineEdit_2.setText("")
```

**Integrating Database**

Then the table also need to represent the data in the .csv file. Below is the snippet code of how to load the data from the database file into the table:

```.py
    def loadTable(self):

        with open("Students App/VocabList/VocabList.csv") as mydatabase:  # Open the file
            file = csv.reader(mydatabase, delimiter=",")  # Split the data by the ","

            for i, row in enumerate(file):
                for j, col in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(col))  # Set the data to the table
        self.tableWidget.repaint()
```

The `enumerate(file)` function returns both the iterable, combined with the index of that value. Through this funtion, the data can be written into 2D array table.

**Delete data in database file**

While the user can manually add the vocabulary into the table, delete the vocabulary is also a key function for the app. 
Firstly, it is a must to get the row of selected cell in the table. Below is the snippet of code for getting the row index:

```.py
    global cell_row
    selected_cell = self.tableWidget.selectedItems()

    # Get the row of the selected cell in the QTable
    for item in selected_cell:
        cell_row = item.row()
```

The method to delete a line containing the vocabulary is that I will add all the words and its definition into an array, then I will check the if the line in the file starts with the deleted vocab, it it does not, append it into the `output array` so the deleted vocab will no longer exist in the `output array`. Finally, I will simply write the `output array` into the database file. Below is the snippet of code:

```.py
        with open("Students App/VocabList/VocabList.csv", "r") as out_file:
            file = csv.reader(out_file, delimiter=",")  # Split the data by the ","
            vocabArray = []
            output = []

            for word in file:
                vocabArray.append(word)  # Add all the words in the list into the array

        with open("Students App/VocabList/VocabList.csv", "r") as out_file_1:
            for line in out_file_1:
                if not line.startswith(vocabArray[cell_row][0]):  # if the line not startwith the String Input
                    # append it to the output list => The name deleted will no longer in the list
                    output.append(line)
            out_file_1.close()

        f = open("Students App/VocabList/VocabList.csv", "w")
        f.writelines(output)  # Write the output list to the Database file
        f.close()
```

As after deleting the vocab, it is necessary to update the table with the new data by using the function loadTable above. As even if the table is loaded, the old data still exist in the cell so it is crucial to clear all the content of the table before reloading the table.

```.py
      self.tableWidget.clear()  # Clear all the content all the table and reload
      self.loadTable()
```




