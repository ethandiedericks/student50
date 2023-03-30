# Student50

### Summary:
For my CS50P Final project I decided to create a Student Administration System with a functional GUI.

### Video Demo: 
[Video Demo Link](https://youtu.be/Srm1rKQZ0HM)

### Description: 
This project is a Student Administration System. It provides a student with a GUI to sign up for a course and view or change their information once logged in. There is also administrator functionality which allows the admin to perform CRUD operations (Create, Read, Update, Delete).

I was quite interested in learning how to make Python GUIs, so I chose a project of this nature. I was also interested in learning more about databases and how they might function in a project like this.

I did contemplate if I should create a GUI or just run everything in the terminal, I went back and forth on it, but I ended up deciding to create a GUI as I would be able to showcase it to more people that way.
At the time of starting this project, I had no idea how to use databases such as SQLite so that took me some time to learn and use.
Tkinter was the most difficult part of this project because I had to go through so much documentation and tutorials on how to do specific things. I used customtkinter as well because it gave my home window a classy look, so I fell in love instantly.
My biggest challenges however was pushing windows to the back and bringing the new window to the front, as well as the database tree view. At first I had no idea how I would show my database to the admin user and then eventually after tons of research, I got my answer!

Every user entry is validated to some extent, with the password validation I used Regex and for the email and mobile numbers I used external libraries.

### Acknowledgements:
Thank you to David Malan and his team for conducting this course in the best possible way I can imagine and for making it free for everyone around the world to take!

#### Libraries Used:

The following libraries and tools are used to make this project:

[customtkinter](https://pypi.org/project/customtkinter/0.3/)
[email-validator](https://pypi.org/project/email-validator/)
[phonenumbers](https://pypi.org/project/phonenumbers/)