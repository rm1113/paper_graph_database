from PyQt6.QtWidgets import QLabel


class KeywordLabel(QLabel):
    def __init__(self, key_id, name, color="#5dade2"):
        super().__init__()

        self.setMaximumSize(200, 30)
        self.setText(name)
        self.color = color
        self.update_style()
        self.key_id = key_id

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
