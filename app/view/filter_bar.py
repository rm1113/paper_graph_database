from app.view.keyword_label import KeywordLabel
from PyQt6.QtWidgets import QHBoxLayout, QWidget


class FilterBar(QWidget):
    def __init__(self):
        super(FilterBar, self).__init__()
        self.colors = ['#5dade2', "#f1948a", "#58d68d"]
        self.layout = QHBoxLayout()
        self.update_filter(['key1', 'key2', 'key3', 'key4'])
        self.layout.addStretch()
        self.setLayout(self.layout)

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def update_filter(self, keyword_list):
        self.clear_layout()
        for i, keyword in enumerate(keyword_list):
            self.layout.addWidget(KeywordLabel(keyword, self.colors[i % len(self.colors)]))
