# Development

## List of Technique used in the program
1. [Sign Up for students](##SignUpforstudents)
1. [Secured Log In](#login)
1. [Database](#database)
1. [Students App Flashcard](#database)
1. [Students App Quizz](#database)
1. [History Windows](#historywindows)
1. [Kanji Learning Windows](#kanjiLearningWindows)

## Sign Up for students

To sign up, the user must provide name, userName and password which will be checked against the database of user credentials. The database of user credentials is saved as studentsAccs.csv, and includes all of the users' encrypted credentials.

The code is explained below:

1. Assign the inputted data to variables
2. Open the database file to check if the username is already existed or not. If yes, empty all the input and set placed holder text, to show error message
3. If not, check if the re_confirmed password is matched to password or not. If yes, do the same as if the usernam is existed.
4. If the input mets all the criterion, rite the input to the database file to store information

```.py
#Assign the input to variables
name = self.lineEdit.text()
userName = self.lineEdit_3.text()
passWord = self.lineEdit_2.text()
rePassword = self.lineEdit_4.text()

#Open the database file
with open("StudentAccs/studentsAccs.csv", "r+") as StudentAccF:
  accountL = []
  file = csv.reader(StudentAccF, delimiter=",")  # Split the data by the ","
  for row in file:
      for acc in row:
          accountL.append(acc)  # Append all the words in the list into the vocab array

  #check if the usernam is already exist
  if name in accountL or userName in accountL:
      #Set the placeholder text to notify the user that the username is already exist
      self.lineEdit.setPlaceholderText("Already exist")
      self.lineEdit_3.setPlaceholderText("Already exist")
      self.emptyLineEdit()
  #check if the re_confirmed password is matched with the password
  elif passWord != rePassword:
      #Set the placeholder text to notify the user that the reconfirmed password is matched to password
      self.lineEdit_4.setPlaceholderText("Wrong Confirmed Password")
      self.emptyLineEdit()

  elif passWord != rePassword and (name in accountL or userName in accountL):
      self.lineEdit.setPlaceholderText("Already exist")
      self.lineEdit_3.setPlaceholderText("Already exist")
      self.lineEdit_4.setPlaceholderText("Wrong Confirmed Password")
  #If all the criterion is fulfilled, write the inputted data into databaese file
  else:
      StudentAccF.write(name + ",")
      StudentAccF.write(userName + ",")
      StudentAccF.write(passWord + "\n")

      #Close the window and
      self.close()
      self.successSignUp()
```

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

#### Teacher App

For the teacher app, there will be only one user uses it so that there is no need for store username and password in the database. Instead I will just store them
inside the program.

  ```.py
    username = "sensei"
    password = "sensei"
  ```

#### Student App

To log a student user in, the user must provide an username and password, which will be checked in the database of user credential ludes all of the users' encrypted credentials. The database of user credentials is saved as `StdudentsAcc.csv`, and includes all of the users' encrypted credentials.

The code is explained below:

1. Assign the inputted username and password
2. Open the database file to check if the username exist in the file. If not, simply empty the input box
3. If yes, take out the password that is matched to the username. 
4. Check the password, if the password is not correct. Simply empty the input box
5. If yes, close the window and enter the app

  ```.py
def enterApp(self):
  #Set the input to variables
  username = self.lineEdit.text()
  password = self.lineEdit_2.text()
  # Open the database file
  with open("StudentAccs/studentsAccs.csv", "r") as studentAccF:
      studentAccL = []
      students = []
      file = csv.reader(studentAccF, delimiter=",")  # Split the data by the ","
      for row in file:
          students.append(row)
          for detailed in row:
              studentAccL.append(detailed)  

      # Check if the username is on the students account list
      if username in studentAccL:
          # Take out the index of the username in list
          index = studentAccL.index(username)
          Lindex = int(index / 3)
          # Take out the password that match to username
          studentsPassword = students[Lindex][2]

          # Check the password
          if password == studentsPassword:
              print("Correct")
              self.close()
          else:
              self.lineEdit.setText("")
              self.lineEdit_2.setText("")
              self.lineEdit.repaint()
              self.lineEdit_2.repaint()
      # If not, simply empty the input so that the user can input again
      else:
          self.lineEdit.setText("")
          self.lineEdit_2.setText("")
          self.lineEdit.repaint()
          self.lineEdit_2.repaint()
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

Then the table also need to represent the data in the .csv file. As the students will open the windows to see what new words, they have already had and edit them if need, so that the table need to show all the words that they add to the database file from the previous sections.
In order to write the data into the table, I will 
1. Open the database file.
2. I will split the data by "," to read all of the vocab and and their definitions inside the file
3. I will implement two for loops, one for loops to assign the index row and the text of each item in the database file, one for loop to take out the item and the index col of each item in a row.
4. Then I will set item or write the data into the cell of the table through the "tableWidget.setItem(row, col, content)" function.

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

**Generate the table with the given number of vocabs and and set the timer**

a. Disable the Generate button after it is pressed

After pressing **generate button**, the programm will disable the button so that the users cannot generate or reset the quizz. 

```.py
self.pushButton.setEnabled(False)
```

b. Generate empty table with the number of vocabs rows

The number of rows of the table is the number of vocabs that the users chosen. I will generate the table with that amount of rows. Here is the snippet of code for generating the empty table.

```.py
def generateTable(self):
    # Take the number of row from the user input
    numberOfRow = int(self.comboBox.currentText())
    # Create the table with number of rows above
    self.tableWidget.setRowCount(numberOfRow)

    self.tableWidget.repaint()
```
`.tableWidget.setRowCount(numberOfRow)` is the syntax for creating a table with the given `number of rows`.

 **Set the timer for the quizz**

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
**Generate random questions and write them into the table**

a. Declare global variables to make it is available throughout classess

As I will use these variables for the other methods: checkAnswers and show the answers in the history windows. The `global` keyword allows modify variables outside of the current scope which is method in this part.

```.py
def addingQ(self):
  global chosenTopic
  global numberOfVocab
  global filePath
  global arrayN, definition, definitionAnswer
```
numberOfVocab = int(self.comboBox.currentText())

b. Open data file with given topic chosen 

Firstly, I will assign vocab file path for variable `filePath`. I will get the topic chosen through the user input. Then I will concatenate the string with `.csv` to make the name of the file and assign to variable `fileName`. Finally, all the vocab quizz files are stored in the VocabQuizz folder so that concatenating `VocabQuizz/` with the fileName will make up the Path to the file.

```.py
# Get the chosen topic from users

chosenTopic = self.comboBox_2.currentText()

# Open the file that have the name of input topic
fileName = chosenTopic + ".csv"
filePath = "VocabQuizz/" + fileName

with open(filePath, "r") as quizzFile:
    file = csv.reader(quizzFile, delimiter=",")

```
c. Generate random questions

To create randoms questions, I will focus on using array and random function. Firstly, I will append all the English words inside the vocab file into an array. Through this, I can access and get the words from the array by using their indexes. Also, I will append the Japanese words in order to check the answers.

```.py
arrayN = []
definition = []

# Append all the English word into array
for i in file:
    arrayN.append(i[1])
    definition.append(i[0])
```

Now, I create an array that contains random numbers without duplicate. These numbers are the indexes of the words in the English and Japanses array that I created in the previous steps. 
By using `random.sample(population, k)`, I can generate a list of **unique** elements within the **range of population** and with the length of **k**. `https://docs.python.org/3/library/random.html`. This method is suitable for my program as the users will choose the number of vocabs they want to take in a given array. Also, it will not duplicate so that the English words will not appear twice or more in the quizz.

```.py
# Create list of random numbers without duplicating
output = random.sample(range(numberOfVocab), numberOfVocab)
```

Next I will write data to the table with the random english words by using `tableWidget.setItem(row,0,item)` to write the `item` to the cell at `row = row, col = 0`. The reason for the column = 0 is that because the quiz will only display the Enlgish word for the students in the first column and the cells in the second column will be empty so that the users can input new words when taking the quiz. Also I will append the English words and their Japanese words into two arrays so that I can use these two arrays to check the answers after they submit their quizzes.

```.py
# Array for storing random english words
global randomEnglishWords

# Set the text for cell
for k in range(0, self.tableWidget.rowCount()):
    # Write the data to the cell at row k and col 0
    self.tableWidget.setItem(k, 0, QTableWidgetItem(arrayN[output[k]]))
    
    # Append the Enlish words and its definiton for the checking answers purpose later.
    definitionAnswer.append(definition[output[k]])
    randomEnglishWords.append(arrayN[output[k]])

# Reload the data in the table again
self.tableWidget.repaint()
```
### Check answers and display results

**Check Answers**

One success criteria of the program is that it will automatically check the answers and calculate the results for the students. Firstly, I will loop through all the rows in the table, then assign the inputted answers to the `inputAnswer` variable by using `QTableWidgetItem(self.tableWidget.item(row, col).text)`. This function will take out the content of the element inside the cell at the coordinate (row,col). A further explantion for the function is in this website: `https://doc.qt.io/qt-5/qtablewidgetitem.html`. As the inputted answers are all in the second column so that in this case `col = 1`. 

```.py
# Loop through all the row in the table to check the inputted answers
for indexRow in range(self.tableWidget.rowCount()):
    inputAnswer = QTableWidgetItem(self.tableWidget.item(indexRow, 1)).text()
```

Then inside the loop, I will also check if the inputted answers are the same as the answers. As the inputted data is Japanese words that is non-ASCII text, so that Python cannot compare them. In order to do that, I use `unicodedata.normalize(form, unistr)` to return the normal form for the Unicode string unistr `https://docs.python.org/3/library/unicodedata.html`. If the answer is correct, increase the `scoreQ` by 1, then append the correct Answers into `correctAnswers` array, else append all the wrong answer into the `wrongAnswers` list. The reason for appending into two arrays is that the finish quizz windows will display both the correct and wrong answers so that the tables will take the data from 2 files that contain these two arrays.

```.py
# Check if the answers are correct
correctAnswersIndex = []
correctAnswers = []
wrongAnswers = []
wrongAnswersIndex = []
scoreQ = 0 # Variable to take the score of the quiz

if unicodedata.normalize('NFC', inputAnswer) == unicodedata.normalize('NFC', definitionAnswer[indexRow]):
    scoreQ += 1  # Increase the score by 1
    correctAnswers.append(inputAnswer)
    correctAnswersIndex.append(indexRow)
else:
    wrongAnswers.append(inputAnswer)
    wrongAnswersIndex.append(indexRow)
```

**Store the results**

Through storing the students records into two files `fileHistoryNameCorrect`, which for correct answers and `fileHistoryNameWrong`, which for wrong answers for quizz, the finish quizz tables can take the data from these two files to display data into 2 tables inside the windows. Also, by adding date taken the quiz will help teacher to keep track of it. Here is the snippet of code with comment.

```.py
def storeResult(self):

    # Take the date that the quiz is taken
    global today, d, fileHistoryNameWrong, fileHistoryPathWrong, fileHistoryNameCorrect, fileHistoryPathCorrect

    today = date.today()
    d = today.strftime("%d-%m-%Y")

    # Create the correct answers file with the name of current date
    fileHistoryNameCorrect = d + "-correctAns.csv"
    fileHistoryPathCorrect = "History File/" + fileHistoryNameCorrect

    # Create the wrong answers file with the name of current date
    fileHistoryNameWrong = d + "-wrongAns.csv"
    fileHistoryPathWrong = "History File/" + fileHistoryNameWrong

    # Write the correct answers to the file
    with open(fileHistoryPathCorrect, "w+") as historyFile:
        for i in range(len(correctAnswers)):
            historyFile.write(randomEnglishWords[correctAnswersIndex[i]] + ",")
            historyFile.write(correctAnswers[i] + "\n")

    # Write the wrong answers to the file
    with open(fileHistoryPathWrong, "w+") as historyFile_1:
        for m in range(0, len(wrongAnswers)):
            historyFile_1.write(randomEnglishWords[wrongAnswersIndex[m]] + ",")
            historyFile_1.write(wrongAnswers[m] + ",")
            historyFile_1.write(definitionAnswer[m + 1] + "\n")
```

**Display the result of students quizz**

The result window will display: `The score of the quizz`, `Table of wrong answers`, `Table of correct answers`. The `scoreQ` is the variable showing the result of the quiz that the user just finished. Also, as the user can choose the number of vocab to take so that showing the nuber of vocabs will help the teachers to keep track of students' performance. Furthermore, in the wrong answers, there will be 3 columns that are English words, inputted answers and the correct answers. From here the users can compare their answers with the correct answers. 
```.py

def loadResult(self):
  
  # Set the label for the result
  self.label_2.setText("Your Score is: " + str(scoreQ) + "/" + str(numberOfVocab))
  self.label_2.repaint()
  with open(fileHistoryPathWrong, "r+") as resultWrong:  # Open the file
      file = csv.reader(resultWrong, delimiter=",")  # Split the data by the ","

      numberOfRowWrong = len(wrongAnswers)
      # Create the table with number of rows above
      self.tableWidget.setRowCount(numberOfRowWrong)

      for i, row in enumerate(file):
          for j, col in enumerate(row):
              self.tableWidget.setItem(i, j, QTableWidgetItem(col))  # Set the data to the table

      # Reload the content of the table again
      self.tableWidget.repaint()
      # Erase the data inside the file

  with open(fileHistoryPathCorrect, "r+") as resultCorrect:  # Open the file
      file_1 = csv.reader(resultCorrect, delimiter=",")  # Split the data by the ","

      numberOfRowCorrect = len(correctAnswers)
      # Create the table with number of rows above
      self.tableWidget_2.setRowCount(numberOfRowCorrect)

      for i, row in enumerate(file_1):
          for j, col in enumerate(row):
              self.tableWidget_2.setItem(i, j, QTableWidgetItem(col))  # Set the data to the table

      # Erase the data inside the file
      # Reload the table
      self.tableWidget_2.repaint()
```
**Save the detail of the quizz**

After finishing the quiz, the program will save the details of the quizz: `Date taken`, `Chosen Topic`, `Number of vocabs`, `Score that the students got`. Simply, the program will use all of the variables `d`, which is today date; `chosenTopic`, `numberOfVocab`, `scoreQ` from the previous part of the program. All of these variables will be written into `historyFile.csv`. The History Windows in the next part will use the data from this file to display all the information related to the quizz.

```.py

filePath = "Students Record Quiz/historyFile.csv"
today = date.today()
d = today.strftime("%d-%m-%Y")

with open(filePath, "a+") as historyFile:
    historyFile.write(d + ",")
    historyFile.write(chosenTopic + ",")
    historyFile.write(str(numberOfVocab) + ",")
    historyFile.write(str(scoreQ) + ",")
```

## History Windows
This windows will show the record of all the quiz that students take. The method used for this part is the same as writing the data into table in the previous parts. Here is the snippet of code with comment.

```.py
    def loadTable(self):

        historyFile = open("Students Record Quiz/historyFile.csv", "r")
        # Set the number of rows for the table based on the number of lines on the files
        self.tableWidget.setRowCount(len(list(historyFile)))
        # Reload the table
        self.tableWidget.repaint()
        
        
        fileH = csv.reader(historyFile, delimiter=",")  # Split the data by the ","
        arrayN = [] # array to store all the data into
        
        # Load through all the fileH and append data into the array.
        for i in fileH: 
            arrayN.append(i)
        
        # Load the data into the table
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(i, j, QTableWidgetItem(arrayN[i][j]))
        
        # Reload the table.
        self.tableWidget.repaint()

```

## Kanji Learning Windows
As a part of success criteria, the kanji learning windows will randomly generate kanji words from the database. In this part, in order to help students learn kanji more effective, I make it as the multiple choice test without calculating the score or record the results. So that, instead of just showing the words and its defintion, the program can help the students remember longer and more active the kanji words.
1. openning the csv file and append all the of data inside into an array

```.py
with open("VocabList/Kanji.csv") as kanji_file:
    file = csv.reader(kanji_file, delimiter=",")
    kanjiArray = []

    for word in file:
        kanjiArray.append(word)
```
2. Generate 4 random kanji words from the kanji Array. The reason for 4 is that this is the multiple choices with 4 options. Through taking out 4 kanjis, 4 definitions are also generated to be displayed as the choices for the kanji word. In here, I use `random.sample()` to generate elements without duplicating. 

```.py
randomKanji = random.sample(kanjiArray, 4)
```
3. Set text from random words to the radio buttons from the randomKanji arrays

The program will run every time the user press the next button and after generating the kanji, it will stop. In this part I use `while` loop to implement the function as the number of times that the user presses the `next` button is unknown so using `for loop` in this case is not appropriate. By assign `True` or `False` to the variable `flag`, the program can continue or stop through `while flag`. 
At the previous part, the program has already created 4 random words and store them to the `kanjiArray`. Thus, in this part, the program just need to set text, which is elements from the array to the radio buttons. Because the radio buttons cannot change their orders or randomly taken, taking random text from the list and assign to the radio buttons is a solution for this. The method is: generate 4 non-duplicated random numbers in range(0,3) as the length of the `kanjiArray` is 4 then append them all into `randomIndexList` array. Now the last step is setting text from the random kanji array. Below is the snippet of code with comment.  
```.py
def loadKanji(self):

    with open("VocabList/Kanji.csv") as kanji_file:
        file = csv.reader(kanji_file, delimiter=",")
        kanjiArray = []
        flag = True

        for word in file:
            kanjiArray.append(word)

        while flag:  # The program will run until the user exit.

            l = 0
            randomKanji = random.sample(kanjiArray, 4)

            # Array with random indexes
            randomIndexList = []

            while len(randomIndexList) < 4:
                index = random.randint(0, 3)

                if index not in randomIndexList:
                    randomIndexList.append(index)

            # Set the text for the label t
            self.label_2.setText(randomKanji[randomIndexList[index]][0])

            # Assign the correct answers for the variable to check it later
            # using global for the purpose of using it in another function
            self.correctAns = randomKanji[randomIndexList[index]][1]
            self.label_2.repaint()

            self.checkAnswer()

            # Assign random text for each button
            self.checkBox.setText(randomKanji[randomIndexList[l]][1])
            self.checkBox.repaint()
            l += 1
            self.checkBox_2.setText(randomKanji[randomIndexList[l]][1])
            self.checkBox_2.repaint()
            l += 1
            self.checkBox_3.setText(randomKanji[randomIndexList[l]][1])
            self.checkBox_3.repaint()
            l += 1
            self.checkBox_4.setText(randomKanji[randomIndexList[l]][1])
            self.checkBox_4.repaint()

            flag = False
```

## Students List in the Teacher App

As the teachers will see all the record of quizzes of students that sign up and use the Students App. In order for teachers to do that, I will create push buttons that will lead to each student's history. So after the students sign up, all of their name are saved in the `StudentAcc.csv`, so that I will read the file lines by lines to take out the students' name and append them into a list. Then I will create buttons with the name from the list. And to store and organize all the buttons, I will create a empty Group Box to add the buttons inside it.

Here are the steps:
1. Create an empty Group Box
2. Open and read the students's name file
3. Append all the students name to a list
4. Use for loops to create buttons
5. Assign the text for the buttons through looping the students name list
6. Add the buttons to the group box.

```.py
def loadStudentsList(self):
    
    # Create a Group Box to store buttons
    self.vbox = QVBoxLayout()
     
    #Open the studentsAccs.csv file
    with open("../Students App/StudentAccs/studentsAccs.csv") as studentL:
        accountL = []
        studentName = []
        file = csv.reader(studentL, delimiter=",")  # Split the data by the ","
        for row in file:
            for acc in row:
                accountL.append(acc)  # Append all the words in the list into the vocab array
        # Append the name of students to a list
        for i in range(0, len(accountL), 3):
            studentName.append(accountL[i])
        # Create buttons
        for i in studentName:
            self.btn = QPushButton('{}'.format(i), self)
            self.vbox.addWidget(self.btn)
            self.vbox.addStretch(1)
            self.groupBox.setLayout(self.vbox)
```
               
