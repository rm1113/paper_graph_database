from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import pyqtSignal, pyqtSlot, Qt, QTimer
import PyQt6.QtGui as QtGui


class KeywordLabel(QLabel):
    add_to_filter = pyqtSignal(int)
    filter_by_only = pyqtSignal(int)
    remove_from_filter = pyqtSignal(int)

    def __init__(self, key_id, name, color="#5dade2"):
        super().__init__()

        self.setMaximumSize(200, 30)
        self.setText(name)
        self.color = color
        self.update_style()
        self.key_id = key_id

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.handle_timeout)

    def update_style(self):
        label_style = f"""
        QLabel {{
            font-size: 14px;
            padding: 5px 10px;
            border-radius: 8px;
            background-color: {self.color};
            color: white;
        }}
        """
        self.setStyleSheet(label_style)

    def set_color(self, color):
        self.color = color
        self.update_style()

    def set_name(self, text):
        self.setText(text)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if ev.button() == Qt.MouseButton.LeftButton:
            # self.add_to_filter.emit(self.key_id)
            self.timer.start(200)
        elif ev.button() == Qt.MouseButton.RightButton:
            self.remove_from_filter.emit(self.key_id)

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.button() == Qt.MouseButton.LeftButton:
            self.timer.stop()
            self.filter_by_only.emit(self.key_id)

    def handle_timeout(self):
        self.add_to_filter.emit(self.key_id)
