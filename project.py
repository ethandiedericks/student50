# dependencies
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random
import string
import sqlite3
import re
import datetime
import phonenumbers
from email_validator import validate_email, EmailNotValidError

# this is the course options students can choose from
course_options = [
    "CS50's Introduction to Computer Science",
    "CS50's Web Programming with Python and JavaScript",
    "CS50's Introduction to Game Development",
    "CS50's Introduction to Artificial Intelligence with Python",
    "CS50 for Lawyers",
    "CS50's Computer Science for Business Professionals",
    "CS50's Understanding Technology",
    "CS50's Mobile App Development with React Native",
]


# <--------- MAIN FUNCTION --------------->
def main():
    root = ctk.CTk()
    Home(root)
    root.mainloop()
    # admin username: admin
    # admin password: verydifficultpassword


def validate_password(password: str) -> bool:
    """
    validate password

    :param password: the password that needs validating
    :type password: str
    :return: True or False
    :rtype: bool
    """
    if len(password) < 8:
        tk.messagebox.showerror(
            "Password Error",
            "Invalid password\n\
            Password must be more than 8 characters long",
        )
        return False
    if not re.search("[a-z]", password):
        tk.messagebox.showerror(
            "Password Error",
            "Invalid password\n\
            Password must contain atleast 1 lowercase letter",
        )
        return False
    if not re.search("[A-Z]", password):
        tk.messagebox.showerror(
            "Password Error",
            "Invalid password\n\
            Password must contain atleast 1 uppercase letter",
        )
        return False
    if not re.search("[0-9]", password):
        tk.messagebox.showerror(
            "Password Error",
            "Invalid password\nPassword must contain atleast 1 number",
        )
        return False
    if not re.search("[!@#$%^&*()_+]", password):
        tk.messagebox.showerror(
            "Password Error",
            "Invalid password\n\
            Password must contain atleast 1 special character",
        )
        return False
    return True


def validate_mobile(mobile_nr: str) -> bool:
    """
    validate mobile number

    :param mobile_nr: the mobile number that needs validating
    :type mobile_nr: str
    :raise NumberParseException:\
    if mobile number is not in correct format or is invalid
    :return: True or False
    :rtype: bool
    """
    try:
        phonenumbers.parse(mobile_nr)
    except phonenumbers.NumberParseException:
        tk.messagebox.showerror(
            "Mobile Error", "Invalid Mobile Number!\nFormat: +27812797044"
        )
        return False
    return True


def validate_stud_email(email: str) -> bool:
    """
    validate student email

    :param email: the email that needs validating
    :type email: str
    :return: True or False
    :rtype: bool
    """
    try:
        validate_email(email)
    except EmailNotValidError:
        tk.messagebox.showerror("Email Error", "Email not valid!")
        return False
    return True


# <--------- GEOMETRY CLASS --------------->
class Geometry:
    def __init__(self, master):
        self.window_width = 1000
        self.window_height = 700
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        master.geometry("1000x700")
        master.configure(bg="#161618")
        master.resizable(False, False)
        # Get the screen width and height
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = int((self.screen_width - self.window_width) // 2)
        y = int((self.screen_height - self.window_height) // 2)

        # Set the window position
        master.geometry(f"+{x}+{y}")


# <--------- HOME CLASS --------------->
class Home:
    def __init__(self, master):
        Geometry(master)
        master.protocol("WM_DELETE_WINDOW", master.quit())
        master.title("Home")

        # create frame
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # create label
        self.home_lbl = ctk.CTkLabel(
            self.frame, text="Welcome to Student50", font=("Helvetica", 26)
        )
        self.home_lbl.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # create buttons
        self.login_btn = ctk.CTkButton(
            self.frame,
            text="Login",
            height=70,
            width=100,
            command=lambda: self.login_click(),
        )
        self.login_btn.place(relx=0.4, rely=0.5, anchor=tk.CENTER)

        # create button
        self.signup_btn = ctk.CTkButton(
            self.frame,
            text="Sign Up",
            height=70,
            width=100,
            command=lambda: self.signup_click(),
        )
        self.signup_btn.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

    def login_click(self):
        """
        pulls up the Login window
        """
        self.login = Login()
        self.login.login_root.mainloop()

    def signup_click(self):
        """
        pulls up the SignUp window
        """
        self.signup = SignUp()
        self.signup.signup_root.mainloop()


# <--------- LOGIN CLASS --------------->
class Login:
    def __init__(self):
        self.login_root = tk.Toplevel()
        Geometry(self.login_root)
        self.login_root.title("Login\t\t Admin - verydifficultpassword")

        # create frame
        self.frame = ctk.CTkFrame(self.login_root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.frame1 = ctk.CTkFrame(self.login_root)
        self.frame1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # create label
        self.login_lbl = ctk.CTkLabel(
            self.frame1,
            text="Login",
            font=("Helvetica", 26)
        )
        self.login_lbl.pack(pady=13, padx=10)

        # create entries
        self.username = ctk.CTkEntry(self.frame1, placeholder_text="Email")
        self.username.pack(pady=12, padx=10)
        self.username.focus_set()
        self.password = ctk.CTkEntry(
            self.frame1,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=12, padx=10)

        # create button
        self.login_btn = ctk.CTkButton(
            self.frame1, text="Login", command=lambda: self.login()
        )
        self.login_btn.pack(pady=12, padx=10)

        self.login_back_btn = ctk.CTkButton(
            self.frame1, text="Back to Home", command=lambda: self.back()
        )
        self.login_back_btn.pack(pady=5, padx=10)

    def back(self):
        """
        destroys the Login window and goes back to Home
        """
        self.login_root.destroy()

    def login(self):
        """
        checks the database for information entered, and logs the user in
        """
        self.student_ID = ""
        if (
            self.username.get().lower() == "admin"
            and self.password.get().lower() == "verydifficultpassword"
        ):
            Admin()
        else:
            try:
                conn = sqlite3.connect("students.db")
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT studentID from students_data\
                    WHERE email= ? and password= ?",
                    (
                        self.username.get(),
                        self.password.get(),
                    ),
                )
                self.student_ID = cursor.fetchall()[0][0]
                conn.commit()
                conn.close()
                self.goto_display()
            except Exception:
                tk.messagebox.showinfo(
                    "Invalid!", "Invalid username or password!")
                self.username.delete(0, tk.END)
                self.password.delete(0, tk.END)
                self.password.configure(placeholder_text="Password")
                self.username.focus_set()

    def goto_display(self):
        """
        pulls up the display window
        """
        self.display = Display(self.student_ID)
        self.display.display_root.mainloop()


# <--------- SIGN UP CLASS --------------->
class SignUp:
    def __init__(self):
        self.signup_root = tk.Toplevel()
        Geometry(self.signup_root)
        self.signup_root.title("Sign Up")

        # create frame
        self.frame = ctk.CTkFrame(self.signup_root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.frame1 = ctk.CTkFrame(self.signup_root)
        self.frame1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # create label
        self.signup_lbl = ctk.CTkLabel(
            self.frame1, text="Sign Up", font=("Helvetica", 26)
        )
        self.signup_lbl.pack(pady=12, padx=10)

        # create studentID
        self.characters = string.ascii_letters + string.digits
        self.studentID = "s" + "".join(
            random.choice(self.characters) for i in range(10)
        )

        # first name
        self.firstname = ctk.CTkEntry(
            self.frame1,
            placeholder_text="First Name"
        )
        self.firstname.pack(pady=12, padx=10)
        self.firstname.focus_set()

        # last name
        self.lastname = ctk.CTkEntry(self.frame1, placeholder_text="Last Name")
        self.lastname.pack(pady=12, padx=10)

        # date of birth entry
        self.dob = ctk.CTkEntry(self.frame1, placeholder_text="YYYY-MM-DD")
        self.dob.pack(pady=12, padx=10)

        # gender drop down
        self.sex_clicked = tk.StringVar(self.signup_root)
        self.sex_clicked.set("Sex")

        self.sex = tk.OptionMenu(self.frame1, self.sex_clicked, "M", "F")
        self.sex.config(bg="#161618", fg="black")
        self.sex.pack(pady=12, padx=10, fill="x", expand=True)

        # email entry
        self.email = ctk.CTkEntry(self.frame1, placeholder_text="Email")
        self.email.pack(pady=12, padx=10)

        # mobile phone entry
        self.mobile = ctk.CTkEntry(self.frame1, placeholder_text="Mobile")
        self.mobile.pack(pady=12, padx=10)

        # courses
        global course_options
        self.course_clicked = tk.StringVar(self.signup_root)
        self.course_clicked.set("Courses")
        self.course = tk.OptionMenu(
            self.frame1,
            self.course_clicked,
            *course_options
        )
        self.course.config(bg="#161618", fg="black", width=10)
        self.course.pack(pady=12, padx=10, fill="x", expand=True)

        # password entry
        self.password = ctk.CTkEntry(
            self.frame1,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=12, padx=10)

        # confirm password
        self.confirm_password = ctk.CTkEntry(
            self.frame1, placeholder_text="Confirm Password", show="*"
        )
        self.confirm_password.pack(pady=12, padx=10)

        # sign up button
        self.signup_btn = ctk.CTkButton(
            self.frame1, text="Sign Up", command=lambda: self.submit()
        )
        self.signup_btn.pack(pady=12, padx=10)

        self.signup_back_btn = ctk.CTkButton(
            self.frame1, text="Back to home", command=lambda: self.back()
        )
        self.signup_back_btn.pack(pady=5, padx=10)

        # command = lambda: self.login()

    def back(self):
        """
        destroys the SignUp window and goes back to the Home window
        """
        self.signup_root.destroy()

    def clear_entries(self):
        """
        clears all entries on the SignUp window
        """
        # Clear entry boxes
        self.firstname.delete(0, tk.END)
        self.lastname.delete(0, tk.END)
        self.dob.delete(0, tk.END)
        self.sex_clicked.set("Sex")
        self.email.delete(0, tk.END)
        self.mobile.delete(0, tk.END)
        self.course_clicked.set("Courses")
        self.password.delete(0, tk.END)
        self.confirm_password.delete(0, tk.END)

    # entry validation
    def validate_first_name(self):
        """
        validate first name

        :return: True or False
        :rtype: bool
        """
        first = self.firstname.get()
        if not len(first) > 0:
            tk.messagebox.showerror("First Name Error", "Invalid First Name")
            return False
        if not first.replace(" ", "").isalpha():
            tk.messagebox.showerror("First Name Error", "Invalid First Name")
            return False
        return True

    def validate_last_name(self):
        """
        validate last name

        :return: True or False
        :rtype: bool
        """
        last = self.lastname.get()
        if not len(last) > 0:
            tk.messagebox.showerror("Last Name Error", "Invalid Last Name")
            return False
        if not last.replace(" ", "").isalpha():
            tk.messagebox.showerror("Last Name Error", "Invalid Last Name")
            return False
        return True

    def validate_dob(self):
        """
        validate date of birth

        :raise ValueError: if the date format entered is invalid
        :return: True or False
        :rtype: bool
        """
        # input date
        date_string = self.dob.get()

        # giving the date format
        date_format = "%Y-%m-%d"

        # using try-except blocks for handling the exceptions
        try:
            # formatting the date using strptime() function
            datetime.datetime.strptime(date_string, date_format)
        # If the date validation goes wrong
        except ValueError:
            # printing the appropriate text if ValueError occurs
            tk.messagebox.showerror(
                "Date Error", "Invalid Date Format!\nFormat: YYYY-MM-DD"
            )
            return False
        return True

    def validate_sex(self):
        """
        checks if the sex chosen is not the default value

        :return: True or False
        :rtype: bool
        """
        if self.sex_clicked.get() == "Sex":
            tk.messagebox.showerror("Sex Error", "Please select a sex.")
            return False
        return True

    def validate_course(self):
        """
        checks if the course chosen is not default

        :return: True or False
        :rtype: bool
        """
        if self.course_clicked.get() == "Courses":
            tk.messagebox.showerror("Course Error", "Please select a course.")
            return False
        return True

    def validate_passwords_match(self):
        """
        checks if the password and confirm password entries match

        :return: True or False
        :rtype: bool
        """
        if not self.password.get() == self.confirm_password.get():
            tk.messagebox.showerror(
                "Password Match Error", "Passwords don't match"
            )
            return False
        return True

    def submit(self):
        """
        validates all the entries and pushes the data to the students database
        """
        if (
            self.validate_first_name()
            and self.validate_last_name()
            and self.validate_dob()
            and self.validate_sex()
            and validate_stud_email(self.email.get())
            and validate_mobile(self.mobile.get())
            and self.validate_course()
            and validate_password(self.password.get())
            and self.validate_passwords_match()
        ):
            # get data
            firstname = self.firstname.get()
            lastname = self.lastname.get()
            studentID = str(self.studentID)
            sex = self.sex_clicked.get()
            date_of_birth = self.dob.get()
            email = self.email.get()
            mobile = self.mobile.get()
            course = self.course_clicked.get()
            password = self.password.get()

            # establish database connection
            conn = sqlite3.connect("students.db")
            # instantiate cursor
            cursor = conn.cursor()
            # create table query
            tbl_query = """CREATE TABLE IF NOT EXISTS students_data
                    (studentID TEXT, firstname TEXT, lastname TEXT,
                    sex TEXT, date_of_birth TEXT,
                    email TEXT, mobile TEXT, course TEXT, password TEXT)
                    """
            # execute table query
            conn.execute(tbl_query)

            # insert student data query
            data_insert_query = """INSERT INTO students_data
            (studentID, firstname, lastname,
            sex, date_of_birth, email, mobile, course, password)
            VALUES(?,?,?,?,?,?,?,?,?)
            """
            # create tuple to store the values of student data
            data_tuple = (
                studentID,
                firstname,
                lastname,
                sex,
                date_of_birth,
                email,
                mobile,
                course,
                password,
            )

            # push student data to students_data table in database
            cursor.execute(data_insert_query, data_tuple)
            conn.commit()
            conn.close()
            tk.messagebox.showinfo(
                "Success",
                "You have successfully signed up for {}".format(course)
            )
            self.clear_entries()
            self.back_to_login()
            # display next window

    def back_to_login(self):
        """
        destroys the SignUp window and goes to the Login window
        """
        self.login = Login()
        self.signup_root.destroy()


# <--------- DISPLAY CLASS --------------->
class Display:
    def __init__(self, student_ID):
        self.display_root = tk.Toplevel()
        Geometry(self.display_root)
        self.display_root.title("Student Information System")
        self.data_tuple = self.fetch_data(student_ID)
        # create frames
        self.frame = ctk.CTkFrame(self.display_root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.frame1 = ctk.CTkFrame(self.display_root, height=300, width=300)
        self.frame1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.studentID_lbl = ctk.CTkLabel(
            self.frame1,
            text="Student ID: ",
            font=("Helvetica", 16),
        )
        self.studentID_lbl.place(relx=0, rely=0)

        self.studentID_result_lbl = ctk.CTkLabel(
            self.frame1, text="Student ID: ", font=("Helvetica bold", 16)
        )
        self.studentID_result_lbl.place(relx=0.5, rely=0)
        self.studentID_result_lbl.configure(
            text="{}".format(self.data_tuple[0]))

        self.fullname_lbl = ctk.CTkLabel(
            self.frame1, text="FullName: ", font=("Helvetica", 16)
        )
        self.fullname_lbl.place(relx=0, rely=0.1, y=15)

        self.fullname_result_lbl = ctk.CTkLabel(
            self.frame1, text="FullName: ", font=("Helvetica bold", 16)
        )
        self.fullname_result_lbl.place(relx=0.5, rely=0.1, y=15)
        self.fullname_result_lbl.configure(
            text="{}".format(self.data_tuple[1] + " " + self.data_tuple[2])
        )

        self.sex_lbl = ctk.CTkLabel(
            self.frame1, text="Sex: ",
            font=("Helvetica", 16)
        )
        self.sex_lbl.place(relx=0, rely=0.2, y=30)

        self.sex_result_lbl = ctk.CTkLabel(
            self.frame1, text="Sex: ", font=("Helvetica bold", 16)
        )
        self.sex_result_lbl.place(relx=0.5, rely=0.2, y=30)
        self.sex_result_lbl.configure(text="{}".format(self.data_tuple[3]))

        self.dob_lbl = ctk.CTkLabel(
            self.frame1, text="Date Of Birth: ", font=("Helvetica", 16)
        )
        self.dob_lbl.place(relx=0, rely=0.3, y=45)

        self.dob_result_lbl = ctk.CTkLabel(
            self.frame1, text="Date Of Birth: ", font=("Helvetica bold", 16)
        )
        self.dob_result_lbl.place(relx=0.5, rely=0.3, y=45)
        self.dob_result_lbl.configure(text="{}".format(self.data_tuple[4]))

        self.mobile_lbl = ctk.CTkLabel(
            self.frame1, text="Mobile: ", font=("Helvetica", 16)
        )
        self.mobile_lbl.place(relx=0, rely=0.4, y=60)

        self.email_lbl = ctk.CTkLabel(
            self.frame1, text="E-mail: ", font=("Helvetica", 16)
        )
        self.email_lbl.place(relx=0, rely=0.5, y=75)

        self.change_email_entry = ctk.CTkEntry(self.frame1)
        self.change_email_entry.place(relx=0.5, rely=0.5, y=75)
        self.change_email_entry.insert(0, self.data_tuple[5])

        self.change_mobile_entry = ctk.CTkEntry(self.frame1)
        self.change_mobile_entry.place(relx=0.5, rely=0.4, y=60)
        self.change_mobile_entry.insert(0, self.data_tuple[6])

        global course_options
        self.course_lbl = ctk.CTkLabel(
            self.frame1, text="Course: ", font=("Helvetica", 16)
        )
        self.course_lbl.place(relx=0, rely=0.6, y=90)
        self.course_clicked = tk.StringVar(self.display_root)
        self.course_clicked.set(self.data_tuple[7])  # set default to db's data
        self.course = tk.OptionMenu(
            self.frame1,
            self.course_clicked,
            *course_options
        )
        self.course.config(bg="#161618", fg="black", width=10)
        self.course.place(relx=0.5, rely=0.6, y=90)

        self.update_btn = ctk.CTkButton(
            self.frame,
            text="Update Info",
            command=lambda: self.is_valid(student_ID)
        )
        self.update_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.back_to_login = ctk.CTkButton(
            self.frame, text="Back to Login", command=lambda: self.goto_login()
        )
        self.back_to_login.place(relx=0.5, rely=0.7, y=40, anchor=tk.CENTER)

    def fetch_data(self, student_ID):
        """
        fetches data by student ID
        """
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * from students_data\
                       WHERE studentID = ?", (student_ID,))
        student_data_tuple = cursor.fetchall()[0]
        conn.commit()
        conn.close()

        return student_data_tuple

    def is_valid(self, student_ID: str) -> bool:
        """
        checks if the mobile number and email entered are correct

        :param student_ID: ID associated with a particular student
        :type student_ID: str
        :return: True or False
        :rtype: bool
        """
        if validate_mobile(self.change_mobile_entry.get()) and\
           validate_stud_email(self.change_email_entry.get()):
            self.update_info(student_ID)

    def update_info(self, student_ID):
        """
        updates the student information in the database

        :param student_ID: ID associated with a particular student
        :type student_ID: str
        """
        conn = sqlite3.connect("students.db")

        # Create a cursor instance
        cursor = conn.cursor()

        cursor.execute(
            """UPDATE students_data SET
            email = :email,
            mobile = :mobile,
            course = :course

            WHERE studentID = :studentID""",
            {
                "studentID": student_ID,
                "email": self.change_email_entry.get(),
                "mobile": self.change_mobile_entry.get(),
                "course": self.course_clicked.get(),
            },
        )

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()
        tk.messagebox.showinfo("Updated!", "Information successfully updated!")

    def goto_login(self):
        """
        destroys the Display window and shows the Login window
        """
        self.display_root.destroy()


# <--------- CRUD CLASS ------------------>
class Admin:
    def __init__(self):
        root = tk.Tk()
        root.title("C R U D")
        root.resizable(False, False)
        root.protocol("WM_DELETE_WINDOW", root.quit())
        self.window_width = 1000
        self.window_height = 700
        root.geometry("1000x700")

        # Get the screen width and height
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = int((self.screen_width - self.window_width) // 2)
        y = int((self.screen_height - self.window_height) // 2)

        # Set the window position
        root.geometry(f"+{x}+{y}")
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure(
            "TreeView",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3",
        )
        self.style.map("TreeView", background=[("selected", "#347083")])

        self.tree_frame = tk.Frame(root)
        self.tree_frame.pack(pady=10)

        self.tree_scroll = tk.Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.setup_tree(root)
        self.runAdmin(root)

    def setup_tree(self, root):
        self.admin_tree = ttk.Treeview(self.tree_frame, selectmode="extended")
        self.admin_tree.pack()

        self.tree_scroll.config(command=self.admin_tree.yview)

        self.admin_tree["columns"] = (
            "studentID",
            "firstname",
            "lastname",
            "sex",
            "date_of_birth",
            "email",
            "mobile",
            "course",
            "password",
        )

        self.admin_tree.column("#0", width=0, stretch=tk.YES)
        self.admin_tree.column("studentID", anchor=tk.CENTER, width=100)
        self.admin_tree.column("firstname", anchor=tk.CENTER, width=100)
        self.admin_tree.column("lastname", anchor=tk.CENTER, width=100)
        self.admin_tree.column("sex", anchor=tk.CENTER, width=70)
        self.admin_tree.column("date_of_birth", anchor=tk.CENTER, width=90)
        self.admin_tree.column("email", anchor=tk.CENTER, width=140)
        self.admin_tree.column("mobile", anchor=tk.CENTER, width=100)
        self.admin_tree.column("course", anchor=tk.CENTER, width=140)
        self.admin_tree.column("password", anchor=tk.CENTER, width=140)

        self.admin_tree.heading("#0", text="", anchor=tk.W)
        self.admin_tree.heading("studentID", text="Student ID", anchor=tk.W)
        self.admin_tree.heading("firstname", text="First Name", anchor=tk.W)
        self.admin_tree.heading("lastname", text="Last Name", anchor=tk.CENTER)
        self.admin_tree.heading("sex", text="Sex", anchor=tk.CENTER)
        self.admin_tree.heading("date_of_birth", text="Date of Birth",
                                anchor=tk.CENTER)
        self.admin_tree.heading("email", text="E-mail", anchor=tk.CENTER)
        self.admin_tree.heading("mobile", text="Mobile", anchor=tk.CENTER)
        self.admin_tree.heading("course", text="Course", anchor=tk.CENTER)
        self.admin_tree.heading("password", text="Password", anchor=tk.CENTER)

        self.admin_tree.tag_configure("oddrow", background="white")
        self.admin_tree.tag_configure("evenrow", background="lightgreen")

        # add data

        # add record entry boxes
        self.data_frame = tk.LabelFrame(root, text="Record")
        self.data_frame.pack(fill="x", expand="yes", padx=20)

        self.studentID_lbl = tk.Label(self.data_frame, text="StudentID: ")
        self.studentID_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.studentID_entry = tk.Entry(self.data_frame)
        self.studentID_entry.grid(row=0, column=1, padx=10, pady=10)

        self.firstname_lbl = tk.Label(self.data_frame, text="First Name: ")
        self.firstname_lbl.grid(row=0, column=2, padx=10, pady=10)
        self.firstname_entry = tk.Entry(self.data_frame)
        self.firstname_entry.grid(row=0, column=3, padx=10, pady=10)

        self.lastname_lbl = tk.Label(self.data_frame, text="Last Name: ")
        self.lastname_lbl.grid(row=0, column=4, padx=10, pady=10)
        self.lastname_entry = tk.Entry(self.data_frame)
        self.lastname_entry.grid(row=0, column=5, padx=10, pady=10)

        self.sex_lbl = tk.Label(self.data_frame, text="Sex: ")
        self.sex_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.sex_clicked = tk.StringVar(root)
        self.sex_clicked.set("Sex")
        self.sex_entry = tk.OptionMenu(
            self.data_frame,
            self.sex_clicked, "M", "F"
        )
        self.sex_entry.grid(row=1, column=1, padx=10, pady=10)

        self.dob_lbl = tk.Label(self.data_frame, text="Date of Birth: ")
        self.dob_lbl.grid(row=1, column=2, padx=10, pady=10)
        self.dob_entry = tk.Entry(self.data_frame)
        self.dob_entry.grid(row=1, column=3, padx=10, pady=10)

        self.pass_lbl = tk.Label(self.data_frame, text="Password: ")
        self.pass_lbl.grid(row=1, column=4, padx=10, pady=10)
        self.pass_entry = tk.Entry(self.data_frame)
        self.pass_entry.grid(row=1, column=5, padx=10, pady=10)

        self.email_lbl = tk.Label(self.data_frame, text="Email: ")
        self.email_lbl.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self.data_frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.mobile_lbl = tk.Label(self.data_frame, text="Mobile: ")
        self.mobile_lbl.grid(row=2, column=2, padx=10, pady=10)
        self.mobile_entry = tk.Entry(self.data_frame)
        self.mobile_entry.grid(row=2, column=3, padx=10, pady=10)

        global course_options
        self.course_lbl = tk.Label(self.data_frame, text="Course: ")
        self.course_lbl.grid(row=2, column=4, padx=10, pady=10)
        self.course_clicked = tk.StringVar(root)
        self.course_clicked.set("Courses")
        self.course_entry = tk.OptionMenu(
            self.data_frame,
            self.course_clicked, *course_options
        )
        self.course_entry.grid(row=2, column=5, padx=10, pady=10, columnspan=5)

        # buttons
        self.button_frame = tk.LabelFrame(root, text="Operations")
        self.button_frame.pack(fill="x", expand="yes", padx=20)

        self.add_button = tk.Button(
            self.button_frame, text="Add Record", command=self.add_record
        )
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.update_button = tk.Button(
            self.button_frame, text="Update Record", command=self.update_record
        )
        self.update_button.grid(row=0, column=2, padx=10, pady=10)

        self.removeall_button = tk.Button(
            self.button_frame, text="Remove All", command=self.remove_all
        )
        self.removeall_button.grid(row=0, column=3, padx=10, pady=10)

        self.removeone_button = tk.Button(
            self.button_frame, text="Remove Selected", command=self.remove_one
        )
        self.removeone_button.grid(row=0, column=4, padx=10, pady=10)

    def runAdmin(self, root):
        # Bind the treeview
        self.admin_tree.bind("<ButtonRelease-1>", self.select_record)
        self.database_handling()
        root.mainloop()

    def clear_entries(self):
        # Clear entry boxes
        self.studentID_entry.delete(0, tk.END)
        self.firstname_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.sex_clicked.set("Sex")
        self.dob_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.course_clicked.set("Courses")

    def select_record(self, e):
        # # clear entry boxes
        self.clear_entries()

        self.selected = self.admin_tree.focus()
        if self.selected:
            self.values = self.admin_tree.item(self.selected, "values")

            self.studentID_entry.insert(0, self.values[0])
            self.firstname_entry.insert(0, self.values[1])
            self.lastname_entry.insert(0, self.values[2])
            self.sex_clicked.set(self.values[3])
            self.dob_entry.insert(0, self.values[4])
            self.email_entry.insert(0, self.values[5])
            self.mobile_entry.insert(0, self.values[6])
            self.course_clicked.set(self.values[7])
            self.pass_entry.insert(0, self.values[8])

    def database_handling(self):
        # Clear the Treeview
        # create studentID

        for record in self.admin_tree.get_children():
            self.admin_tree.delete(record)

        conn = sqlite3.connect("students.db")

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students_data")
        records = cursor.fetchall()
        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                self.admin_tree.insert(
                    parent="",
                    index="end",
                    iid=count,
                    text="",
                    values=(
                        record[0],
                        record[1],
                        record[2],
                        record[3],
                        record[4],
                        record[5],
                        record[6],
                        record[7],
                        record[8],
                    ),
                    tags=("evenrow",),
                )
            else:
                self.admin_tree.insert(
                    parent="",
                    index="end",
                    iid=count,
                    text="",
                    values=(
                        record[0],
                        record[1],
                        record[2],
                        record[3],
                        record[4],
                        record[5],
                        record[6],
                        record[7],
                        record[8],
                    ),
                    tags=("oddrow",),
                )
            count += 1
        conn.commit()

        conn.close()

    # Update record
    def update_record(self):
        if (
            self.validate_first_name()
            and self.validate_last_name()
            and self.validate_dob()
            and self.validate_sex()
            and validate_stud_email(self.email_entry.get())
            and validate_mobile(self.mobile_entry.get())
            and validate_password(self.pass_entry.get())
        ):
            # Grab the record number
            selected = self.admin_tree.focus()
            # Update record
            self.admin_tree.item(
                selected,
                text="",
                values=(
                    self.studentID_entry.get(),
                    self.firstname_entry.get(),
                    self.lastname_entry.get(),
                    self.sex_clicked.get(),
                    self.dob_entry.get(),
                    self.email_entry.get(),
                    self.mobile_entry.get(),
                    self.course_clicked.get(),
                    self.pass_entry.get(),
                ),
            )

            # Update the database
            # Create a database or connect to one that exists
            conn = sqlite3.connect("students.db")

            # Create a cursor instance
            cursor = conn.cursor()

            cursor.execute(
                """UPDATE students_data SET
                firstname = :firstname,
                lastname = :lastname,
                sex = :sex,
                date_of_birth = :dob,
                email = :email,
                mobile = :mobile,
                course = :course,
                password = :pass

                WHERE studentID = :studentID""",
                {
                    "studentID": self.studentID_entry.get(),
                    "firstname": self.firstname_entry.get().capitalize(),
                    "lastname": self.lastname_entry.get().capitalize(),
                    "sex": self.sex_clicked.get(),
                    "dob": self.dob_entry.get(),
                    "email": self.email_entry.get(),
                    "mobile": self.mobile_entry.get(),
                    "course": self.course_clicked.get(),
                    "pass": self.pass_entry.get(),
                },
            )

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

            self.clear_entries()

    # add new record to database
    def add_record(self):
        if (
            self.validate_first_name()
            and self.validate_last_name()
            and self.validate_dob()
            and self.validate_sex()
            and validate_stud_email(self.email_entry.get())
            and validate_mobile(self.mobile_entry.get())
            and self.validate_course()
            and validate_password(self.pass_entry.get())
        ):
            # Create a database or connect to one that exists
            conn = sqlite3.connect("students.db")

            # Create a cursor instance
            cursor = conn.cursor()

            self.newcharacters = string.ascii_letters + string.digits
            self.newstudentID = "s" + "".join(
                random.choice(self.newcharacters) for i in range(10)
            )
            # Add New Record
            tbl_query = """CREATE TABLE IF NOT EXISTS students_data
            (studentID TEXT, firstname TEXT, lastname TEXT, sex TEXT,
            date_of_birth TEXT,
            email TEXT, mobile TEXT, course TEXT, password TEXT)
            """
            # execute table query
            conn.execute(tbl_query)

            # insert student data query
            data_insert_query = """INSERT INTO students_data
            (studentID, firstname, lastname,
            sex, date_of_birth, email, mobile, course, password) VALUES
            (?,?,?,?,?,?,?,?,?)
            """
            # create tuple to store the values of student data
            data_tuple = (
                self.newstudentID,
                self.firstname_entry.get().capitalize(),
                self.lastname_entry.get().capitalize(),
                self.sex_clicked.get(),
                self.dob_entry.get(),
                self.email_entry.get(),
                self.mobile_entry.get(),
                self.course_clicked.get(),
                self.pass_entry.get(),
            )

            # push student data to students_data table in database
            cursor.execute(data_insert_query, data_tuple)

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

            # Clear entry boxes
            self.clear_entries()

            # Clear The Treeview Table
            self.admin_tree.delete(*self.admin_tree.get_children())

            # Run to pull data from database on start
            self.database_handling()

            # Add a little message box for fun
            tk.messagebox.showinfo("Added!", "Your Record Has Been Added!")

    # Remove one record
    def remove_one(self):
        x = self.admin_tree.selection()[0]
        self.admin_tree.delete(x)
        # Create a database or connect to one that exists
        conn = sqlite3.connect("students.db")

        # Create a cursor instance
        cursor = conn.cursor()

        # Delete From Database
        cursor.execute(
            "DELETE from students_data WHERE studentID= ?",
            (self.studentID_entry.get(),),
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear The Entry Boxes
        self.clear_entries()

        # Add a little message box for fun
        tk.messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")

    # Remove all records
    def remove_all(self):
        response = tk.messagebox.askyesno(
            "Hold Up, Wait a Min!",
            "This will delete everything from the table\nAre you sure?",
        )

        # Add logic for message box
        if response == 1:
            # Clear the Treeview
            for record in self.admin_tree.get_children():
                self.admin_tree.delete(record)

            # Create a database or connect to one that exists
            conn = sqlite3.connect("students.db")

            # Create a cursor instance
            c = conn.cursor()

            # Delete Everything From The Table
            c.execute("DROP TABLE students_data")

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()

            # Clear entry boxes if filled
            self.clear_entries()

            # Recreate the table
            # self.recreate_table()

    def recreate_table(self):
        conn = sqlite3.connect("students.db")

        # Create a cursor instance
        c = conn.cursor()

        # Create Table
        c.execute(
            """CREATE TABLE IF NOT EXISTS students_data
            (studentID TEXT, firstname TEXT, lastname TEXT, sex TEXT,
            date_of_birth TEXT,
            email TEXT, mobile TEXT, course TEXT, password TEXT)
            """
        )

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

    def validate_first_name(self):
        first = self.firstname_entry.get()
        if not len(first) > 0:
            tk.messagebox.showerror("First Name Error", "Invalid First Name")
            return False
        if not first.replace(" ", "").isalpha():
            tk.messagebox.showerror("First Name Error", "Invalid First Name")
            return False
        return True

    def validate_last_name(self):
        last = self.lastname_entry.get()
        if not len(last) > 0:
            tk.messagebox.showerror("Last Name Error", "Invalid Last Name")
            return False
        if not last.replace(" ", "").isalpha():
            tk.messagebox.showerror("Last Name Error", "Invalid Last Name")
            return False
        return True

    def validate_dob(self):
        # input date
        date_string = self.dob_entry.get()

        # giving the date format
        date_format = "%Y-%m-%d"

        # using try-except blocks for handling the exceptions
        try:
            # formatting the date using strptime() function
            datetime.datetime.strptime(date_string, date_format)
        # If the date validation goes wrong
        except ValueError:
            # printing the appropriate text if ValueError occurs
            tk.messagebox.showerror(
                "Date Error", "Invalid Date Format!\nFormat: YYYY-MM-DD"
            )
            return False
        return True

    def validate_sex(self):
        if self.sex_clicked.get() == "Sex":
            tk.messagebox.showerror("Sex Error", "Please select a sex.")
            return False
        return True

    def validate_course(self):
        if self.course_clicked.get() == "Courses":
            tk.messagebox.showerror("Course Error", "Please select a course.")
            return False
        return True


if __name__ == "__main__":
    main()
