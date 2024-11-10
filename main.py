import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLineEdit, QPushButton, QVBoxLayout, QLabel)
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("bmi_calculator")
        self.setGeometry(300, 300, 300, 300)

        self.ok_button = QPushButton("Ок", self)
        #ok_button.clicked.connect(self.close)

        self.text_input_mass = QLabel("input your mass:")

        self.text_input_height = QLabel("input your height (cm):")

        self.line_edit_mass = QLineEdit(self)

        self.line_edit_height = QLineEdit(self)

        layout = QVBoxLayout()
        layout.addWidget(self.text_input_mass)
        layout.addWidget(self.line_edit_mass)
        layout.addWidget(self.text_input_height)
        layout.addWidget(self.line_edit_height)
        layout.addWidget(self.ok_button)
        #self.setLayout(layout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

"""print("Введите вашу массу тела")
mass = int(input())
print("Введите ваш рост в см")
cm = int(input())
print(f"Ваш bmi = {round(mass/(cm/100)**2, 2)}")"""