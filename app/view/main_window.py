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
from PyQt6.QtCore import Qt, pyqtSlot

from app.view.welcome_window import WelcomeWindow
from app.view.filter_bar import FilterBar
from app.view.keyword_explorer import KeywordExplorer
from app.view.tool_bar import ToolBar
from app.view.document_explorer import DocumentExplorer
from app.view.document_details import DocumentDetails


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db_file = None

        # Connect welcome window
        self.welcome_window = WelcomeWindow()
        self.welcome_window.file_selected.connect(self.on_file_selected)
        self.welcome_window.create_database_button.clicked.connect(self.on_new_database)

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
        self.filter_bar.remove_from_filter.connect(self.remove_from_filter)
        self.filter_bar.filter_by_only.connect(self.filter_by_only)
        self.filter_bar.clear_filter_signal.connect(self.clear_filter)
        self.filter_bar.update_filter([(i, f"key{i}") for i in range(25)])  # TODO: remove

        # Layout with three columns
        # Keyword Explorer
        self.keywords_list = KeywordExplorer([(i, f'key{i}') for i in range(25)])  # TODO: remove
        self.keywords_list.add_to_filter.connect(self.add_to_filter)
        self.keywords_list.filter_by_only.connect(self.filter_by_only)
        self.keywords_list.remove_from_db.connect(self.remove_keyword_from_db)

        # Document explorer
        self.document_explorer = DocumentExplorer([(i, f"DOC_{i}") for i in range(55)])  # TODO: remove
        self.document_explorer.select_document_signal.connect(self.select_document_slot)
        self.document_explorer.open_document_signal.connect(self.open_file_in_os)

        # Document info window
        self.document_info = DocumentDetails()
        self.document_info.add_to_filter.connect(self.add_to_filter)
        self.document_info.filter_by_only.connect(self.filter_by_only)
        self.document_info.open_document_signal.connect(self.open_file_in_os)

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

        # Widget connections
        self.document_explorer.select_document_signal.connect(lambda: self.document_info.set_enabled(True))

        # TODO: add update function

    @pyqtSlot(str)
    def on_file_selected(self, file):
        # TODO: file validation
        self.db_file = file
        print(f"DB file catched: {file}")
        self.welcome_window.close()
        self.show()

    @pyqtSlot()
    def on_new_database(self):
        self.db_file = None
        print("New DB ")
        self.welcome_window.close()
        self.show()

    def begin(self):
        self.welcome_window.show()

    @pyqtSlot(int)
    def add_to_filter(self, key_id):
        print(f"Add to filter key_id={key_id}")
        key_name = f"key_{key_id}"  # TODO: get from controller
        self.filter_bar.add_keyword_to_filter(key_id, key_name)
        # TODO: implement

    @pyqtSlot(int)
    def remove_from_filter(self, key_id):
        print(f"Remove from filter key_id={key_id}")
        self.filter_bar.remove_keyword_from_filter(key_id)
        # TODO: update filter in controller

    @pyqtSlot(int)
    def filter_by_only(self, key_id):
        print(f"Filter by only key_id={key_id}")
        key_name = f"key_{key_id}"
        self.filter_bar.update_filter([(key_id, key_name)])
        # TODO: update controller filter

    @pyqtSlot(int)
    def remove_keyword_from_db(self, key_id):
        print(f"Remove keyword from database: key_id={key_id}")
        # TODO: implement

    @pyqtSlot()
    def clear_filter(self):
        print("CLEAR FILTER")  # TODO: implement

    @pyqtSlot(int)
    def select_document_slot(self, doc_id):
        # TODO: get data from controller
        doc_info = {
            'title': f'Document #{doc_id}',
            'doi': f"doi:{doc_id}",
            'author': 'Me',
            'date': 'Now'
        }
        key_lists = [(doc_id+i, f"key_{doc_id+i}") for i in range(3)]
        self.document_info.update_data(doc_id, doc_info, key_lists)

    @pyqtSlot(int)
    def open_file_in_os(self, doc_id):
        print(f"Open file with id:{doc_id}")
        # TODO: implement


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.begin()

    sys.exit(app.exec())
