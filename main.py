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
        if ok:
            password = self.PasswordGenerator(size)
            self.password_label.setText(f"Generated Password: {password}")
            

    def PasswordGenerator(self, size):
        SpecialList = ["!", "@", "#", "$", "%", "^", "&", "*"]
        password = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=size))
        return password

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
