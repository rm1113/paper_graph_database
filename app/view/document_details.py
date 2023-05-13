from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSlot
from app.view.keyword_explorer import KeywordExplorer


class DocumentDetails(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Document name
        self.doc_name = QLabel('Document Name')
        self.doc_name.setFont(QFont('Arial', 20))
        layout.addWidget(self.doc_name)

        # Document author
        self.doc_author = QLabel('Author: ')
        layout.addWidget(self.doc_author)

        # DOI field
        self.doi_field = QLabel('DOI: ')
        layout.addWidget(self.doi_field)

        # Date field
        self.date_field = QLabel('Date: ')
        layout.addWidget(self.date_field)

        # Keyword bar
        self.keyword_bar = KeywordExplorer()
        layout.addWidget(self.keyword_bar)

        # Button to add keyword
        self.add_keyword_button = QPushButton('Add keyword')
        layout.addWidget(self.add_keyword_button)

        # Button to show all connected documents
        self.show_docs_button = QPushButton('Show connected documents')
        layout.addWidget(self.show_docs_button)

        # Button to edit document info
        self.edit_doc_button = QPushButton('Edit document info')
        # Button to delete document from the database
        self.delete_doc_button = QPushButton('Delete document')

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.edit_doc_button)
        button_layout.addWidget(self.delete_doc_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.set_enabled(False)

    # @pyqtSlot
    # def set_enabled_slot(self):
    #     self.set_enabled(True)

    @pyqtSlot(bool)
    def set_enabled(self, enabled):
        self.setEnabled(enabled)
        if enabled:
            self.setStyleSheet("")  # Return to default style when enabled
        else:
            self.setStyleSheet("QWidget { background-color: #D3D3D3 }")  # Greyed out when disabled
