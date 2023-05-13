from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton)
from PyQt6.QtCore import pyqtSlot
from app.view.keyword_explorer import KeywordExplorer


class DocumentDetails(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Document title
        self.doc_name_label = QLabel('Document Title:')
        self.doc_name_data = QLabel("-")
        [layout.addWidget(w) for w in [self.doc_name_label, self.doc_name_data]]

        # Document author
        self.doc_author_label = QLabel('Author: ')
        self.doc_author_data = QLabel('-')
        [layout.addWidget(w) for w in [self.doc_author_label, self.doc_author_data]]

        # DOI field
        self.doi_field_label = QLabel('DOI: ')
        self.doi_field_data = QLabel('-')
        [layout.addWidget(w) for w in [self.doi_field_label, self.doi_field_data]]

        # Date field
        self.date_field_label = QLabel('Date: ')
        self.date_field_data = QLabel('-')
        [layout.addWidget(w) for w in [self.date_field_label, self.date_field_data]]

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

    @pyqtSlot(bool)
    def set_enabled(self, enabled):
        self.setEnabled(enabled)
        if enabled:
            self.setStyleSheet("")  # Return to default style when enabled
        else:
            self.setStyleSheet("QWidget { background-color: #D3D3D3 }")  # Greyed out when disabled

    def update_data(self, document_info):
        title = document_info['title']
        doi = document_info['doi']
        author = document_info['author']
        date = document_info['date']

        self.doc_name_data.setText(self.get_string(title))
        self.doi_field_data.setText(self.get_string(doi))
        self.doc_author_data.setText(self.get_string(author))
        self.date_field_data.setText(self.get_string(date))

    @staticmethod
    def get_string(value):
        return "-" if value is None else value
