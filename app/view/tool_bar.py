from PyQt6.QtWidgets import (
    QToolBar,
    QWidget,
    QLabel,
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QHBoxLayout
)
from PyQt6.QtGui import QAction


class ToolBar(QToolBar):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.setMovable(False)

        # Connect AddDocument
        add_document_action = QAction("Add Document", self)
        add_document_action.triggered.connect(self.open_add_document_dialog)
        self.addAction(add_document_action)

        # Connect AddKeyword
        add_keyword_action = QAction("Add Keyword", self)
        add_keyword_action.triggered.connect(self.open_add_keyword_dialog)
        self.addAction(add_keyword_action)

        self.add_document_dialog = None
        self.add_keyword_dialog = None

    def open_add_document_dialog(self):
        self.add_document_dialog = AddDocumentDialog()
        self.add_document_dialog.show()

    def open_add_keyword_dialog(self):
        self.add_keyword_dialog = AddKeywordDialog()
        self.add_keyword_dialog.show()

class AddDocumentDialog(QDialog):
    def __init__(self):
        super(AddDocumentDialog, self).__init__()

        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("New Document"))

        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText("Local file path...")
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_file)

        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_path_input)
        file_layout.addWidget(self.browse_button)
        self.layout.addLayout(file_layout)

        self.doi_input = QLineEdit()
        self.doi_input.setPlaceholderText("DOI...")
        self.layout.addWidget(self.doi_input)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Title...")
        self.layout.addWidget(self.title_input)

        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Author...")
        self.layout.addWidget(self.author_input)

        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Date ...")
        self.layout.addWidget(self.author_input)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)
        self.setModal(True)

    def browse_file(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName()[0]
        self.file_path_input.setText(file_path)


class AddKeywordDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Add Keyword')

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Add keyword")
        self.keyword_name_input = QLineEdit()
        self.keyword_name_input.setPlaceholderText("Keyword name")
        self.keyword_description_input = QLineEdit()
        self.keyword_description_input.setPlaceholderText("Keyword description")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.keyword_name_input)
        self.layout.addWidget(self.keyword_description_input)

        self.confirm_button = QPushButton("Confirm", clicked=self.accept)
        self.cancel_button = QPushButton("Cancel", clicked=self.reject)
        self.layout.addWidget(self.confirm_button)
        self.layout.addWidget(self.cancel_button)

        self.setModal(True)

    def get_values(self):
        return self.keyword_name_input.text(), self.keyword_description_input.text()
