import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QToolBar,
    QLabel,
    QLineEdit,
    QListWidget,
    QTextEdit,
    QGridLayout
)
from PyQt6.QtCore import Qt

from app.view.welcome_window import WelcomeWindow
from app.view.filter_bar import FilterBar
from app.view.keyword_explorer import KeywordExplorer
from app.view.tool_bar import ToolBar
from app.view.document_explorer import DocumentExplorer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Document Manager")
        self.setGeometry(100, 100, 800, 600)

        # Apply styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0F0F0;
            }
            QToolBar {
                background-color: #55A1F2;
                padding: 5px;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #A0A0A0;
                border-radius: 5px;
                padding: 2px;
            }
            QListWidget {
                background-color: #FFFFFF;
                border: 1px solid #A0A0A0;
                border-radius: 5px;
            }
            QTextEdit {
                background-color: #FFFFFF;
                border: 1px solid #A0A0A0;
                border-radius: 5px;
            }
        """)

        # Toolbar
        self.toolbar = ToolBar()
        self.addToolBar(self.toolbar)

        # Filter bar
        self.filter_bar = FilterBar()

        # Layout with three columns
        self.keywords_list = KeywordExplorer([f'key{i}' for i in range(25)])
        self.document_explorer = DocumentExplorer([(i, f"DOC_{i}") for i in range(55)])
        self.document_info = QTextEdit()

        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.filter_bar)
        self.columns_layout = QHBoxLayout()
        self.columns_layout.addWidget(self.keywords_list)
        self.columns_layout.addWidget(self.document_explorer)
        self.columns_layout.setStretchFactor(self.document_explorer, 1)
        self.columns_layout.addWidget(self.document_info)
        self.main_layout.addLayout(self.columns_layout)

        # Central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    welcome_window = WelcomeWindow()

    # Connect the welcome window buttons to show the main window and close the welcome window
    def open_database():
        main_window.show()
        welcome_window.close()

    def create_database():
        main_window.show()
        welcome_window.close()

    welcome_window.open_database_button.clicked.connect(open_database)
    welcome_window.create_database_button.clicked.connect(create_database)

    welcome_window.show()
    sys.exit(app.exec())
