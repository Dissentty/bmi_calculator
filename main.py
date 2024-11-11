import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                             QLineEdit, QPushButton, QVBoxLayout, QLabel, QGridLayout)
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("bmi_calculator")
        self.setGeometry(200, 200, 200, 100)

        self.ok_button = QPushButton("Ок", self)
        self.ok_button.clicked.connect(self.calculate_bmi)

        self.text_input_mass = QLabel("input your mass:")

        self.text_input_height = QLabel("input your height (cm):")

        self.line_edit_mass = QLineEdit(self)

        self.line_edit_height = QLineEdit(self)

        self.bmi_label = QLabel("your bmi:")
        self.bmi = QLabel("0")
        self.bmi_state = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.text_input_mass)
        layout.addWidget(self.line_edit_mass)
        layout.addWidget(self.text_input_height)
        layout.addWidget(self.line_edit_height)
        layout.addWidget(self.ok_button)

        layout_2 = QVBoxLayout()
        #layout_2.addWidget(layout)
        layout_2.addWidget(self.bmi_label)
        layout_2.addWidget(self.bmi)
        layout_2.addWidget(self.bmi_state)

        layout_3 = QGridLayout()
        layout_3.addLayout(layout, 0, 0)
        layout_3.addLayout(layout_2, 0, 1)
        #self.setLayout(layout)

        widget = QWidget()
        widget.setLayout(layout_3)
        self.setCentralWidget(widget)

    def calculate_bmi(self):
        try:
            mass = float(self.line_edit_mass.text())
            height_cm = float(self.line_edit_height.text())
            height_m = height_cm / 100
            bmi_value = mass / (height_m ** 2)
            self.bmi.setText(f"{bmi_value:.2f}")

            if bmi_value < 18.5:
                self.bmi_state.setText("Underweight")
            elif 18.5 <= bmi_value < 24.9:
                self.bmi_state.setText("Normal weight")
            elif 25 <= bmi_value < 29.9:
                self.bmi_state.setText("Overweight")
            else:
                self.bmi_state.setText("Obesity")
        except ValueError:
            self.bmi.setText("Error")
            self.bmi_state.setText("Invalid input")

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()