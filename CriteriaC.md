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

**Database for quizzes and list**

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

**Writing input data into database (Students App Vocabulary List)**

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

**Delete data in database file (Students App Vocabulary List)**

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


## Students App Flashcard

An essential part and one of the priority in the success criteria list, is implementing the flash card based on the vocabulary list they make. The database of the vocabulary list is used for the flash card as all of the vocabulary used for this windows are based on the vocabulary list. 
The process of making flash card follows these steps:


 1. Check if the vocab list is empty or not and open the vocabulary list file
   
  If it is empty,there is no need to load the file and display the vocabulary and its definition there. I will just display a windows to show the finish flash card windows.
    
    ```.py
    if (os.path.getsize("VocabList/VocabList.csv")) == 0: # If the file is empty
          self.close().  # Close the flashcard windows itself
          self.finish_flash(). # Open the finish flash card windows 
    ```
  If it is not, open the vocabulary list file to load the data. I will add all the word into an array so I can get a random word inside the array by creating random index.
  
```.py
with open("VocabList/VocabList.csv", "r") as vocab_list_file:  # Open the file
  file = csv.reader(vocab_list_file, delimiter=",").  # Separate the data in the file by ,
  vocabArray = []       # Create an array to store all the words and its defintion

  for word in file:       # Loop through all the file and append all the data into the vocab array.
      vocabArray.append(word)
```

   3. Generate a random number to take the index of random vocabulary inside the array. In this process, by generating list of random number within the range of vocabulary array length, the vocabulary can be taken randomly from the list as their indexes are random. I also make sure that there are no two duplicated random index appear next to each other so that the situtation of displaying the same vocab next to each other will never happen. Lastly, program will set text for the labels to display it inside the GUI windows.
   
```.py 
       
notTrue = False
randomNums = []. # Array stores all the random index numbers

        # Infinity set random words and definition for the vocab on the flash card
        while not notTrue:
            indexN = random.randint(0, len(vocabArray) - 1)  # Get a random number

            # Check if the next word is duplicate with the previous word or not
            if indexN not in randomNums:
                randomNums.append(indexN)  # Add all the random numbers into the array
                randomVocab = vocabArray[indexN][0]  # Assign the random vocab through the random index
                randomDef = vocabArray[indexN][1]   # Assign the random definition according to the random vocab
                notTrue = True

             # Set Text for word and definition

                self.label_2.setText(randomVocab)
                self.label_2.repaint()
                self.label_3.setText(randomDef)
                self.label_3.repaint()
```
   
  4. Inside the flashcard window, there are two radio buttons: "I have known this word" and "I have not known this word". 
  
  **If the user check on the "I have known this word"**
  The program will delete the word from the vocab list and it will not display inside the flashcard windows and inside the data file anymore. 
  
  a. I will check if the radio button is checked or not. 
  
```.py 
if self.radioButton.isChecked():
```
  
  b. I will open the vocab file again and check if any lines inside the file do not start with the deleted vocab. If it does not, I will append to an new array. So through this, the deleted vocab will not be in the array. Lastly, I just need to write the new array into the vocab list file.

```.py
with open("VocabList/VocabList.csv", "r") as check_file_1:
    for line in check_file_1:
        if not line.startswith(vocabArray[indexN][0]):  # if the line not startwith the String Input
            # append it to the output list => The name deleted will no longer in the list
            output.append(line)
    check_file_1.close()

f = open("VocabList/VocabList.csv", "w")
f.writelines(output)  # Write the output list to the Database file
f.close()
```
 **If the user check on the "I have not known this word"**
 
 The program will just continue the process of loading the flash card as in the **part 3**

## Students App Quizz

### Generate Questions

**Get the chosen topic and Number of Vocab**

The number of vocab will determine how many quizzes to generate and the topic chosen will determine which data the program will take.

```.py
numberOfVocab = int(self.comboBox.currentText())   # The options in the qcombobox are text so that it's necessary to convert it to integer.
chosenTopic = self.comboBox_2.currentText()
```

**Write the data into table with the chosen topic and number of vocabs**

a. Disable the Generate button after it is pressed

After pressing generate quizz, the programm will disable the button so that the users cannot generate ans reset the quizz

```.py
self.pushButton.setEnabled(False)
```

b. Generate empty table with the number of vocabs rows

The number of rows of the table is the number of vocabs that the users chosen. I will generate the table with that amount of rows. Also the users need to enter their answer so that I also create lineEdit inside each row. Here is the snippet of code for generating the empty table.

```.py
def generateTable(self):
    # Take the number of row from the user input
    numberOfRow = int(self.comboBox.currentText())
    # Create the table with number of rows above
    self.tableWidget.setRowCount(numberOfRow)

    # Add QLineEdit inside inside each cell for each row
    for index in range(self.tableWidget.rowCount()):
        inputAnswer = QtWidgets.QLineEdit()
        self.tableWidget.setCellWidget(index, 1, inputAnswer)

    self.tableWidget.repaint()
```
c. Set the timer for the quizz

```.py
def setTheTimer(self):

    # Set the different timer for each selection
    if self.comboBox.currentText() == "5":
        self.count = 20 * 10
    elif self.comboBox.currentText() == "10":
        self.count = 40 * 10
    elif self.comboBox.currentText() == "15":
        self.count = 60 * 10
    elif self.comboBox.currentText() == "20":
        self.count = 80 * 10
    elif self.comboBox.currentText() == "25":
        self.count = 100 * 10
    else:
        self.count = 120 * 10

    # Set text for the timer label
    self.label_2.setText(str(10))
    self.label_2.repaint()

    if self.count == 0:
        self.start = False

    self.start_action()

    timer = QTimer(self)
    timer.timeout.connect(self.showTime)
    timer.start(100)

def showTime(self):

    # checking if flag is true
    if self.start:
        # incrementing the counter
        self.count -= 1

        # timer is completed
        if self.count == 0:
            # making flag false
            self.start = False

            # setting text to the label
            self.submitQ()
            # self.close()

    if self.start:
        # getting text from count
        text = str(self.count / 10) + " s"

        # showing text
        self.label_2.setText(text)

def start_action(self):
    # making flag true
    self.start = True
    # count = 0
    if self.count == 0:
        self.start = False
```

