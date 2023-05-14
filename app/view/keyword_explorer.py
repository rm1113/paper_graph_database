from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
    QFrame)
from PyQt6.QtCore import pyqtSignal
from app.view.keyword_label import KeywordLabel


class KeywordExplorer(QWidget):
    add_to_filter = pyqtSignal(int)
    filter_by_only = pyqtSignal(int)

    def __init__(self, keyword_list=None):
        super(KeywordExplorer, self).__init__()

        if keyword_list is None:
            keyword_list = []

        self.setMinimumWidth(150)
        self.colors = ['#5dade2', "#f1948a", "#58d68d"]

        self.layout = QVBoxLayout()

        self.title = QLabel('Keywords list:')
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        self.keywords_widget = QWidget()
        self.keywords_layout = QVBoxLayout()

        self.keywords_widget.setLayout(self.keywords_layout)

        self.scroll_area.setWidget(self.keywords_widget)

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.scroll_area)
        # self.layout.addStretch()

        self.setLayout(self.layout)

        self.update_keywords(keyword_list)

    def update_keywords(self, keyword_list):
        self.clear_keywords_layout()
        for i, keyword in enumerate(keyword_list):
            # Set color, id and name
            color = self.colors[i % len(self.colors)]
            key_id = keyword[0]
            key_name = keyword[1]
            # Create label and connect signals
            label = KeywordLabel(key_id, key_name, color)
            label.add_to_filter.connect(self.add_to_filter.emit)
            label.filter_by_only.connect(self.filter_by_only.emit)
            # Add label to the layout
            self.keywords_layout.addWidget(label)
        self.keywords_layout.addStretch()

    def clear_keywords_layout(self):
        while self.keywords_layout.count():
            child = self.keywords_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
