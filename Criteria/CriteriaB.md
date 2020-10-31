![SystemDiagram](teacher_app_1.jpg)

![SystemDiagram](teacher_app.jpg)

![SystemDiagram](student_app.jpg)

![SystemDiagram](student_app_1.jpg)

  **Fig1.** The initial design of the Food Management App. These picutes show the detail of the background of each function. These were made based on the success criteria
  
![SystemDiagram](SystemDiagram.png)

  **Fig2.** This is the system diagram of the Japanese Review System showing the input, software and output.
  
  --------------------------------------------------------------------
  
  **TEACHER APP**
  
  ![SystemDiagram](teacher_login.jpg)

  **Fig3.**  The login ui design window containing username and password input only due to the teacher can only access it by herself.
  
   ![SystemDiagram](teacher_listFunct.jpg)

  **Fig4.**  The list of functions window shows all the functions that the user can access through the program. Also, with the log out button, the user can log out and quit the program immediately.
  
  ![SystemDiagram](teacher_add.jpg)

  **Fig5.**  The add new questions ui window allows user to add a single or multiple questions for the tests. After creating, the questions will be save in the database and shown in the list of questions table.
  
  ![SystemDiagram](teacher_questionList.jpg)

  **Fig6.**  All the created questions will be shown in the table. Also the anwers and correct answers are listed in this area.
  
  ![SystemDiagram](teacher_delete.jpg)

  **Fig7.**  The delete function will delete the question inputted and all of its answers in the table of questions and datatbase.
  
  ![SystemDiagram](teacher_edit_search.jpg)

  **Fig8.** This is a multipurpose windows as it features both searching and editting the information of the questions created by the users.
  
  ![SystemDiagram](teacher_export.jpg)

  **Fig9.** The export function helps teacher to export all the questions that they created. Then they can use this file to send to their students for test purpose.
  
 --------------------------------------------------------------------
  
  **STUDENT APP**
  
  ![SystemDiagram](student_login.jpg)

  **Fig10.**  The login ui design window containing username and password input only due to the students can only access it by thenselves.
  
  ![SystemDiagram](student_test.jpg)

  **Fig11.** The window will show the test for students with questions, answer chose and timer.
  
  ![SystemDiagram](student_finish.jpg)

  **Fig12.**  The finish window notifies the students that they have finished the test and shows the score of the test.
  
  ![SystemDiagram](student_history.jpg)

  **Fig13.**  The history table will show the date and time the tests taken and the grade for each test.
  
  ![SystemDiagram](Add_diagram.png)
  **Fig14.** This is the flowchart showing how the add function works
  
  ![SystemDiagram](Delete_diagram.png)
  **Fig15.** This is the flowchart showing how the delete function works
  
  ### Expected input and output
  
  #|Function|INPUT|OUTPUT
---|---|---|---
1| Add Questions | Questions, Answer Choice and Correct Answers|Data in the Databse file and in the questions data table
2| Edit and Search Questions | Question ID | All the properties of the questions and the new data (if the information is editted) will be saved in the database file and the question list table.
3| Delete Question | Question ID | All the properties of the questions will be deleted from the database file and also in the questions table.
4| Export | Directory | The database file will be saved in the github server |
5| Student Grades |  | Showing the students' name and their score |
6| Take test | Student Answers | Showing the score and the wrong questions |
7| History | | Showing the previous score |   
  
   ### Testing Plan

