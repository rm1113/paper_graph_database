from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QFrame
from PyQt6.QtCore import Qt, QEvent, pyqtSignal
from PyQt6.QtGui import QContextMenuEvent
from app.view.document_widget import DocumentWidget


class DocumentExplorer(QWidget):
    document_selected = pyqtSignal()

    def __init__(self, documents=None, signal_to_connect_with_selection=None):
        super(DocumentExplorer, self).__init__()

        if documents is None:
            documents = []

        # if signal_to_connect_with_selection is not None:
        #     self.document_selected.connect(signal_to_connect_with_selection)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        self.documents_widget = QWidget()
        self.documents_layout = QVBoxLayout()
        self.documents_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.documents_widget.setLayout(self.documents_layout)

        self.scroll_area.setWidget(self.documents_widget)

        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

        self.update_documents(documents)

    def update_documents(self, documents):
        self.clear_documents_layout()
        for i, document in enumerate(documents):
            doc_widget = DocumentWidget(*document)
            doc_widget.installEventFilter(self)
            self.documents_layout.addWidget(doc_widget)

    def clear_documents_layout(self):
        while self.documents_layout.count():
            child = self.documents_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                self.deselect_all_except(obj)
                self.document_selected.emit()
            elif event.button() == Qt.MouseButton.RightButton:
                print("Right click placeholder")
        elif event.type() == QEvent.Type.MouseButtonDblClick:
            print("Double click placeholder")
        return super().eventFilter(obj, event)

    def deselect_all_except(self, widget):
        for i in range(self.documents_layout.count()):
            w = self.documents_layout.itemAt(i).widget()
            if w != widget:
                w.setStyleSheet("")
            else:
                w.setStyleSheet("background-color: #ADD8E6;")

    # @pyqtSignal(bool)
    # def document_selected(self):
    #     return True
