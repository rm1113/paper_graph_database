from PyQt6.QtWidgets import QWidget, QGridLayout, QScrollArea, QFrame
from PyQt6.QtCore import Qt

from app.view.document_widget import DocumentWidget


class DocumentExplorer(QWidget):
    def __init__(self, documents=None):
        super(DocumentExplorer, self).__init__()

        if documents is None:
            # documents = []
            documents = [(i, f"doc_{i}") for i in range(5)]

        self.layout = QGridLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        self.documents_widget = QWidget()
        self.documents_layout = QGridLayout()
        self.documents_widget.setLayout(self.documents_layout)

        self.scroll_area.setWidget(self.documents_widget)

        self.layout.addWidget(self.scroll_area)
        # self.layout.setAlignment()
        self.setLayout(self.layout)

        self.update_documents(documents)

    def update_documents(self, documents):
        self.clear_documents_layout()
        for i, document in enumerate(documents):
            doc_widget = DocumentWidget(*document)
            doc_widget.clicked.connect(self.on_document_clicked)
            doc_widget.doubleClicked.connect(self.on_document_double_clicked)
            self.documents_layout.addWidget(doc_widget, i // 5, i % 5)  # Adjust grid size as needed

    def clear_documents_layout(self):
        while self.documents_layout.count():
            child = self.documents_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def on_document_clicked(self):
        sender = self.sender()
        for i in range(self.documents_layout.count()):
            widget = self.documents_layout.itemAt(i).widget()
            if widget is sender:
                widget.select()
            else:
                widget.deselect()

    def on_document_double_clicked(self):
        print("Document double clicked")
