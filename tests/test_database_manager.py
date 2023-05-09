from app.model.database_manager import DatabaseManager
from app.model.keyword_node import KeywordNode
from app.model.document_node import DocumentNode

import unittest
from pathlib import Path
import tempfile


class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.database_manager = DatabaseManager()

    def test_initialization(self):
        self.assertEqual(self.database_manager.database, [])
        self.assertEqual(self.database_manager.keywords, {})
        self.assertEqual(self.database_manager.documents, {})

    def test_add_document(self):
        doc = DocumentNode("Test Title")
        doc_id = self.database_manager.add_document(doc)
        self.assertEqual(self.database_manager.documents[doc_id], doc)

    def test_remove_document(self):
        doc = DocumentNode("Test Title")
        doc_id = self.database_manager.add_document(doc)
        self.database_manager.remove_document(doc_id)
        self.assertNotIn(doc_id, self.database_manager.documents)
        self.assertIsNone(self.database_manager.database[doc_id])

    def test_add_keyword(self):
        keyword = KeywordNode("Test Keyword")
        keyword_id = self.database_manager.add_keyword(keyword)
        self.assertEqual(self.database_manager.keywords[keyword_id], keyword)

    def test_remove_keyword(self):
        keyword = KeywordNode("Test Keyword")
        keyword_id = self.database_manager.add_keyword(keyword)
        self.database_manager.remove_keyword(keyword_id)
        self.assertNotIn(keyword_id, self.database_manager.keywords)
        self.assertIsNone(self.database_manager.database[keyword_id])

    def test_connect_and_disconnect_document_and_keyword(self):
        doc = DocumentNode("Test Title")
        doc_id = self.database_manager.add_document(doc)
        keyword = KeywordNode("Test Keyword")
        keyword_id = self.database_manager.add_keyword(keyword)

        self.database_manager.connect_document_and_keyword(doc_id, keyword_id)
        self.assertIn(keyword_id, self.database_manager.database[doc_id])
        self.assertIn(doc_id, self.database_manager.database[keyword_id])

        self.database_manager.disconnect_document_and_keyword(doc_id, keyword_id)
        self.assertNotIn(keyword_id, self.database_manager.database[doc_id])
        self.assertNotIn(doc_id, self.database_manager.database[keyword_id])

    def test_save_and_load_schema(self):
        doc = DocumentNode("Test Title")
        doc_id = self.database_manager.add_document(doc)
        keyword = KeywordNode("Test Keyword")
        keyword_id = self.database_manager.add_keyword(keyword)
        self.database_manager.connect_document_and_keyword(doc_id, keyword_id)

        with tempfile.TemporaryDirectory() as tempdir:
            temp_file = Path(tempdir) / 'test_database_manager.pickle'
            self.database_manager.save_schema(temp_file)

            loaded_database_manager = DatabaseManager()
            loaded_database_manager.load_schema(temp_file)

            self.assertEqual(loaded_database_manager.database, self.database_manager.database)
            self.assertEqual(loaded_database_manager.keywords, self.database_manager.keywords)
            self.assertEqual(loaded_database_manager.documents, self.database_manager.documents)


if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()