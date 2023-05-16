from app.view.keyword_label import KeywordLabel
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QFrame, QScrollArea, QPushButton
from PyQt6.QtCore import pyqtSignal, Qt, pyqtSlot


class FilterBar(QWidget):
    clear_filter_signal = pyqtSignal()
    filter_by_only = pyqtSignal(int)
    remove_from_filter = pyqtSignal(int)

    def __init__(self):
        # TODO: add clear filter function
        super(FilterBar, self).__init__()
        self.keyword_ids = []

        self.setMaximumHeight(90)


        self.filter_layout = QHBoxLayout()
        self.clear_button = QPushButton('Clear filter')  # TODO: replace with icon
        self.clear_button.clicked.connect(self.clear_filter)
        self.keywords_layout = QHBoxLayout()

        self.filter_layout.addWidget(self.clear_button)
        self.filter_layout.addLayout(self.keywords_layout)

        # scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.scroll_widget = QWidget()

        self.scroll_widget.setLayout(self.filter_layout)

        self.scroll_area.setWidget(self.scroll_widget)

        # Create a layout for the FilterBar and add the scroll area to it
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.scroll_area)
        self.scroll_area.setMaximumHeight(80)
        self.setLayout(main_layout)
        main_layout.addStretch()

        self.keywords_layout.addStretch()
        self.filter_layout.addStretch()

    def clear_filter(self):
        self.clear_filter_signal.emit()
        self.clear_layout()
        self.keyword_ids = []

    def clear_layout(self):
        while self.keywords_layout.count():
            child = self.keywords_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def update_filter(self, keyword_list):
        self.clear_layout()
        self.keyword_ids = []
        for i, keyword in enumerate(keyword_list):
            # Get id and name for the label
            key_id, key_name = keyword
            self.keyword_ids.append(key_id)
            # Create label and connect signals
            label = KeywordLabel(key_id, key_name)
            label.remove_from_filter.connect(self.remove_from_filter.emit)
            label.filter_by_only.connect(self.filter_by_only.emit)
            # Add label to the layout
            self.keywords_layout.addWidget(label)

    def add_keyword_to_filter(self, key_id, key_name):
        if key_id not in self.keyword_ids:
            label = KeywordLabel(key_id, key_name)
            label.remove_from_filter.connect(self.remove_from_filter.emit)
            label.filter_by_only.connect(self.filter_by_only.emit)
            self.keywords_layout.addWidget(label)
            self.keyword_ids.append(key_id)

    def remove_keyword_from_filter(self, key_id):
        for i in range(self.keywords_layout.count()):
            widget = self.keywords_layout.itemAt(i).widget()
            if isinstance(widget, KeywordLabel) and widget.key_id == key_id:
                widget.setParent(None)  # This removes the widget from layout
                self.keyword_ids.remove(key_id)
                break
