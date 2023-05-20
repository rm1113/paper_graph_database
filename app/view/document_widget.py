from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, pyqtSignal, QTimer


class DocumentWidget(QWidget):
    select_document_signal = pyqtSignal(int)
    open_document_signal = pyqtSignal(int)
    open_doc_menu_signal = pyqtSignal(int)

    def __init__(self, doc_id, title, parent=None):
        super(DocumentWidget, self).__init__(parent)
        self.doc_id = doc_id
        self.title = title

        # Layout
        self.layout = QVBoxLayout()
        # self.timer = QTimer()
        # self.timer.setSingleShot(True)
        # self.timer.timeout.connect(self.handle_timeout)

        # Icon
        self.icon_label = QLabel()
        icon_path = 'essay.png'
        self.icon_label.setPixmap(QPixmap(icon_path).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio))

        # Title
        self.title_label = QLabel(self.title)
        self.title_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        # Arrange Icon and Title
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.icon_label)
        self.horizontal_layout.addWidget(self.title_label)
        self.horizontal_layout.addStretch()

        # Set layout
        self.setLayout(self.horizontal_layout)

    def mousePressEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
            self.select_document_signal.emit(self.doc_id)
        elif ev.button() == Qt.MouseButton.RightButton:
            self.open_menu()  # TODO: upgrade
            # self.open_doc_menu_signal.emit(self.key_id)

    def mouseDoubleClickEvent(self, a0):
        if a0.button() == Qt.MouseButton.LeftButton:
            self.open_document_signal.emit(self.doc_id)

    def open_menu(self):
        print(f"Open document menu for doc: {self.doc_id}")
