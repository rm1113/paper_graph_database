from app.view.keyword_label import KeywordLabel
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QFrame, QScrollArea
from PyQt6.QtCore import pyqtSignal, Qt


class FilterBar(QFrame):
    add_to_filter = pyqtSignal(int)
    filter_by_only = pyqtSignal(int)
    remove_from_filter = pyqtSignal(int)

    def __init__(self):
        # TODO: add clear filter function
        super(FilterBar, self).__init__()
        self.colors = ['#5dade2', "#f1948a", "#58d68d"]

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setMaximumHeight(90)

        self.layout = QHBoxLayout()

        # scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.scroll_widget = QWidget()

        self.scroll_widget.setLayout(self.layout)

        self.scroll_area.setWidget(self.scroll_widget)

        # Create a layout for the FilterBar and add the scroll area to it
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.scroll_area)
        self.scroll_area.setMaximumHeight(80)
        self.setLayout(main_layout)
        main_layout.addStretch()

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def update_filter(self, keyword_list):
        self.clear_layout()
        for i, keyword in enumerate(keyword_list):
            # Get id, name and color for the label
            key_id, key_name = keyword
            color = self.colors[i % len(self.colors)]
            # Create label and connect signals
            label = KeywordLabel(key_id, key_name, color)
            label.add_to_filter.connect(self.add_to_filter.emit)
            label.remove_from_filter.connect(self.remove_from_filter.emit)
            label.filter_by_only.connect(self.filter_by_only.emit)
            # Add label to the layout
            self.layout.addWidget(label)
        self.layout.addStretch()
