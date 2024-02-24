import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from main_test import Ui_MainWindow


def wrong_Password_massageBox():
    massageBox = QMessageBox()
    massageBox.setText("Password should be more than 3 letters")
    massageBox.setWindowTitle("Warning!")
    massageBox.setIcon(QMessageBox.Warning)
    massageBox.exec()


def blank_Email_or_Password_massageBox():
    massageBox = QMessageBox()
    massageBox.setText("Blank Email or Password")
    massageBox.setWindowTitle("Warning!")
    massageBox.setIcon(QMessageBox.Warning)
    massageBox.exec()


class MyWindow:
    def __init__(self):
        self.window = QMainWindow()
        self.initUI = Ui_MainWindow()
        self.initUI.setupUi(self.window)

        self.valid_Email = "e-mail"
        self.valid_password = "password"

        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Sign_In)
        self.initUI.Log_In.clicked.connect(self.Login_user)
        self.initUI.Log_Out.clicked.connect(self.User)

    def show(self):
        self.window.show()

    def wrong_Email_massageBox(self):
        massageBox = QMessageBox()
        massageBox.setText("Please enter a valid E-Mail")
        massageBox.setWindowTitle("Warning!")
        massageBox.setIcon(QMessageBox.Warning)
        massageBox.exec()

    def wrong_Credentials_massageBox(self):
        massageBox = QMessageBox()
        massageBox.setText("Invalid username or password")
        massageBox.setWindowTitle("Warning!")
        massageBox.setIcon(QMessageBox.Warning)
        massageBox.exec()

    def successful_login(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.User_Page)

    def Login_user(self):
        email_input = self.initUI.Email_Input.text()
        password_input = self.initUI.Password_Input.text()

        if len(email_input) <= 3 or '@' not in email_input:
            self.wrong_Email_massageBox()
        elif len(password_input) <= 3:
            wrong_Password_massageBox()
        elif email_input == '' or password_input == '':
            blank_Email_or_Password_massageBox()
        elif email_input == self.valid_Email and password_input == self.valid_password:
            self.successful_login()
        else:
            self.wrong_Credentials_massageBox()

    def User(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Sign_In)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(application.exec_())
