from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt


class DocumentWidget(QWidget):
    def __init__(self, doc_id, title, parent=None):
        super(DocumentWidget, self).__init__(parent)
        self.doc_id = doc_id
        self.title = title

        # Layout
        self.layout = QVBoxLayout()

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
