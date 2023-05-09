from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton
)

from PyQt6.QtCore import Qt


class WelcomeWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome")
        self.setGeometry(400, 400, 300, 200)

        # Welcome message
        self.welcome_message = QLabel("Welcome to the Document Manager!")
        self.welcome_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Buttons
        self.open_database_button = QPushButton("Open Database")
        self.create_database_button = QPushButton("Create Database")

        # Set the custom style for the buttons
        button_style = """
                QPushButton {
                    font-size: 14px;
                    padding: 10px 20px;
                    border-radius: 8px;
                    background-color: #5dade2;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #2e86c1;
                }
                QPushButton:pressed {
                    background-color: #1c4e80;
                }
                """
        self.open_database_button.setStyleSheet(button_style)
        self.create_database_button.setStyleSheet(button_style)

        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.welcome_message)
        second_layout = QHBoxLayout()
        second_layout.addWidget(self.open_database_button)
        second_layout.addWidget(self.create_database_button)
        self.main_layout.addLayout(second_layout)
        self.setLayout(self.main_layout)


