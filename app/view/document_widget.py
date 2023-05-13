from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QHBoxLayout
from PyQt6.QtGui import QPixmap, QMouseEvent, QIcon
from PyQt6.QtCore import Qt, pyqtSignal


class DocumentWidget(QWidget):
    clicked = pyqtSignal()
    doubleClicked = pyqtSignal()

    def __init__(self, doc_id, title):
        super().__init__()
        self.doc_id = doc_id
        icon_path = 'C:\\Users\\RM\\Documents\\GitHub\\paper_graph_database\\resourses\\essay.png'
        # self.layout = QVBoxLayout(self)
        self.layout = QHBoxLayout(self)
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QPixmap(QIcon(icon_path).pixmap(15, 15)))  # Set the icon
        self.title_label = QLabel(title)

        self.layout.addWidget(self.icon_label)
        self.layout.addWidget(self.title_label)

        self.setMinimumHeight(30)
        self.layout.addStretch()

        self.clicked.connect(self.mousePressEvent)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        if event.button() == Qt.MouseButton.RightButton:
            self.open_menu()
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.doubleClicked.emit()
        super().mouseDoubleClickEvent(event)

    def open_menu(self):
        print("Right click event")

    def select(self):
        self.setStyleSheet("background-color: #e0e0e0")  # Change the color as per requirement

    def deselect(self):
        self.setStyleSheet("")
