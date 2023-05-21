from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton)
from PyQt6.QtCore import pyqtSlot, pyqtSignal
from app.view.keyword_explorer import KeywordExplorer


class DocumentDetails(QWidget):
    add_to_filter = pyqtSignal(int)
    filter_by_only = pyqtSignal(int)
    open_document_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        self.doc_id = None

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
        self.keyword_bar.add_to_filter.connect(self.add_to_filter.emit)
        self.keyword_bar.filter_by_only.connect(self.filter_by_only.emit)
        layout.addWidget(self.keyword_bar)

        # Button to open in os viewer
        self.open_file_button = QPushButton("Open file")
        self.open_file_button.clicked.connect(self.emit_open_doc_signal)
        layout.addWidget(self.open_file_button)

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

    def update_data(self, doc_id, document_info, key_id_list):
        self.doc_id = doc_id
        title = document_info['title']
        doi = document_info['doi']
        author = document_info['author']
        date = document_info['date']

        self.doc_name_data.setText(self.get_string(title))
        self.doi_field_data.setText(self.get_string(doi))
        self.doc_author_data.setText(self.get_string(author))
        self.date_field_data.setText(self.get_string(date))

        self.keyword_bar.update_keywords(key_id_list)

    @staticmethod
    def get_string(value):
        return "-" if value is None else value

    def emit_open_doc_signal(self):
        if self.doc_id is not None:
            self.open_document_signal.emit(self.doc_id)
