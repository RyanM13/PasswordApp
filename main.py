from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QInputDialog, QLabel, QPushButton
import sys
import random
import string

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def ask_question(self):
        size, ok = QInputDialog.getInt(self, "Test", "How large would you like the password to be:")
        upper, ok = QInputDialog.getInt(self, "Input Dialog", "How many upper case characters would you like:")
        lower, ok = QInputDialog.getInt(self, "Input Dialog", "How many lower characters would you like:")
        specialC, ok = QInputDialog.getInt(self, "Input Dialog", "How many special characters would you like:")
        numC, ok = QInputDialog.getInt(self, "Input Dialog", "How many numbers would you like:")
        

        if ok:
            password = self.PasswordGenerator(size, upper, lower, specialC, numC)
            self.password_label.setText(f"Generated Password: {password}")
            

    def PasswordGenerator(self, size, upper, lower, specialC, numC):
        SpecialList = ["!", "@", "#", "$", "%", "^", "&", "*"]
        Lowercase_Letters = ''.join(random.choices(string.ascii_lowercase, k=lower))
	#Generates an amount of uppercase characters
        Uppercase_letters = ''.join(random.choices(string.ascii_uppercase, k=upper))
	#Generates an amount of Numerical characters
        Numerical = ''.join(random.choices(string.digits, k=numC))
	#Generates an amount of Special characters			
        Special_char = ''.join(random.choices(SpecialList, k=specialC))

    #Generates the remaining characters needed for length
        Length_char = ''.join([random.choices(string.ascii_letters)
									for char in range(size  - (lower + upper + numC + specialC) )])
			
	#Concatenating the strings together
        Newpassword = Lowercase_Letters + Uppercase_letters + Numerical + str(Special_char) + Length_char

	#Turning the new string into a list for a list function
        Newpassword_List = list(Newpassword)

	#The list function shuffle moves the strings to different postions 
        random.shuffle(Newpassword_List)
			
	#Joining the list back to a string
        Final_Password = ''.join(Newpassword_List)
        return Final_Password 

    def initUI(self):
        self.setWindowTitle("Password Generator App")

        layout = QVBoxLayout()

        # Button to trigger password generation
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.ask_question)
        layout.addWidget(self.generate_button)

        # Label to display the generated password
        self.password_label = QLabel("Your generated password will appear here")
        layout.addWidget(self.password_label)

        # Set the layout for the QWidget
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
