from document_node import DocumentNode
from keyword_node import KeywordNode
import pickle
from pathlib import Path


class DatabaseManager:
    def __init__(self, dataset_title=None):
        if dataset_title is None:
            self._dataset_title = 'database'
        else:
            self._dataset_title = dataset_title
        self._database = []  # adjacency list
        self._keywords = {}   # dict keyword_id: KeywordNode
        self._documents = {}  # dict document_id: DocumentNode
        self._max_id = -1  # current maximal id

    @property
    def database(self):
        return self._database

    @property
    def keywords(self):
        return self._keywords

    @property
    def documents(self):
        return self._documents

    def _invalid_id(self, object_id):
        if object_id > self._max_id or object_id < 0 or self._database[object_id] is None:
            return True
        return False

    def add_document(self, document: DocumentNode) -> int:
        self._max_id += 1
        self._documents[self._max_id] = document     # create new one
        self._database.append([])
        return self._max_id  # id of the new document

    def remove_document(self, document_id):
        if self._invalid_id(document_id) or document_id not in self.documents:
            return

        # Remove all connections
        for connections in self._database[document_id]:
            self._database[connections].remove(document_id)

        self._database[document_id] = None
        self._documents.pop(document_id)

    def update_document(self, document_id: int, updated_document: DocumentNode) -> int:
        if self._invalid_document_id(document_id):
            return -1

        if document_id in self._documents:
            self._documents[document_id] = updated_document
        return document_id

    def add_keyword(self, keyword: KeywordNode) -> int:
        self._max_id += 1
        self._keywords[self._max_id] = keyword
        self._database.append([])
        return self._max_id  # id of the new keyword

    def remove_keyword(self, key_id:int) -> None:
        if self._invalid_id(key_id) or key_id not in self._keywords:
            return
        # Remove all connections
        for connection in self._database[key_id]:
            self._database[connection].remove(key_id)

        # Remove the keyword
        self._keywords.pop(key_id)
        self._database[key_id] = None

    def update_keyword(self, key_id: int, new_keyword: KeywordNode) -> int:
        if self._invalid_id(key_id) or key_id not in self._keywords:
            return -1

        self._keywords[key_id] = new_keyword
        return key_id

    def connect_document_and_keyword(self, doc_id: int, key_id: int) -> None:
        if self._invalid_id(doc_id) or self._invalid_id(key_id):
            return
        if doc_id not in self.documents or key_id not in self.keywords:
            return

        self._database[doc_id].append(key_id)
        self._database[key_id].append(doc_id)

    def disconnect_document_and_keyword(self, doc_id: int, key_id: int) -> None:
        if self._invalid_id(doc_id) or self._invalid_id(key_id):
            return
        if doc_id not in self.documents or key_id not in self.keywords:
            return

        if key_id in self._database[doc_id]:
            self._database[doc_id].remove(key_id)
            self._database[key_id].remove(doc_id)

    def get_connected_documents_by_keyword(self, key_id):
        if self._invalid_id(key_id) or key_id not in self._keywords:
            return None

        result = [self._documents[doc_id] for doc_id in self._database[key_id] if doc_id in self._documents]
        return result

    def save_schema(self, filepath: Path = None) -> Path:

        result = {
            'adj_list': self._database,
            'documents': {i: d.serialize() for i, d in self._documents.items()},
            'keywords': {i: k.serialize() for i, k in self._keywords.items()}
        }
        if filepath is None:
            filepath = self._dataset_title
        with open(filepath, 'wb') as f:
            pickle.dump(result, f)
        return filepath

    def load_schema(self, filepath):
        with open(filepath, 'rb') as f:
            model = pickle.load(f)

        # Clean current database
        self._database = []
        self._keywords = {}
        self._database = {}

        self._database = model['adj_list']
        for i, keyword_info in model['keywords'].items():
            self._keywords[i] = KeywordNode(keyword_info['name'], keyword_info['description'])

        for i, doc_info in model['documents'].items():
            self.documents[i] = DocumentNode(title=doc_info['title'], author=doc_info['author'],
                                             doi=doc_info['doi'], date=doc_info['date'],
                                             local_file_path=doc_info['local_path'])

    def save_database(self):
        raise NotImplementedError

    def load_database(self):
        raise NotImplementedError

    def __str__(self):
        if len(self._database) and len(self._documents) and len(self._keywords) == 0:
            return "Empty database"

        result = "Keywords: "
        for key_id, keyword in self._keywords.items():
            result += f"{keyword} ({len(self._database[key_id])}) "
        result += '\nDocuments:\n'
        for doc_id, doc in self.documents.items():
            result += f"{doc_id}: {doc.title} -> "
            for key_id in self._database[doc_id]:
                if key_id in self._keywords:
                    result += f"{self._keywords[key_id].name} "
            result += ";\n"
        return result


if __name__ == "__main__":
    pap1 = DocumentNode(title='pap1')
    pap2 = DocumentNode(title='pap2')
    pap3 = DocumentNode(title='pap3')
    pap4 = DocumentNode(title='pap4')
    key1 = KeywordNode('key1')
    key2 = KeywordNode('key2')
    db = DatabaseManager()
    print(db)
    db.add_document(pap1)
    db.add_keyword(key1)
    db.add_document(pap2)
    db.connect_document_and_keyword(0, 1)
    db.connect_document_and_keyword(2, 1)
    print(db)
    db.disconnect_document_and_keyword(0, 1)
    db.disconnect_document_and_keyword(0, 1)
    db.connect_document_and_keyword(2, 0)
    print(db)
    file = 'temp'
    db.save_schema(file)
    print(db)
    db.load_schema(file)
    print(db)
