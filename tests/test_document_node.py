from app.model.document_node import DocumentNode
import unittest
from unittest.mock import Mock, patch
from pathlib import Path


class TestDocumentNode(unittest.TestCase):

    def test_initialization(self):
        document = DocumentNode("test_title", "test_author", "2023-05-01",
                                "10.1016/j.nima.2023.168233", "/path/to/local/file")
        self.assertEqual(document.title, "test_title")
        self.assertEqual(document.author, "test_author")
        self.assertEqual(document.date, "2023-05-01")
        self.assertEqual(document.doi, "10.1016/j.nima.2023.168233")
        self.assertEqual(document.local_file_path, Path("/path/to/local/file"))

    @patch('app.model.document_node.requests.get')
    def test_from_doi(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'message': {
                'title': ['test_title'],
                'author': [{'given': 'Test', 'family': 'Author', 'sequence': 'first'}],
                'published': {'date-parts': [[2023, 5, 1]]},
            }
        }
        mock_get.return_value = mock_response

        document = DocumentNode.from_doi("10.1016/j.nima.2023.168233")
        self.assertEqual(document.title, "test_title")
        self.assertEqual(document.author, "Test Author")
        self.assertEqual(document.date, "2023")

    def test_change_title(self):
        document = DocumentNode("test_title", "test_author", "2023-05-01",
                                "10.1016/j.nima.2023.168233", "/path/to/local/file")
        document.change_title("new_test_title")
        self.assertEqual(document.title, "new_test_title")

    def test_change_doi(self):
        document = DocumentNode("test_title", "test_author", "2023-05-01",
                                "10.1016/j.nima.2023.168233", "/path/to/local/file")
        document.change_doi("new_doi")
        self.assertEqual(document.doi, "new_doi")

    def test_change_author(self):
        document = DocumentNode("test_title", "test_author", "2023-05-01",
                                "10.1016/j.nima.2023.168233", "/path/to/local/file")
        document.change_author("new_author")
        self.assertEqual(document.author, "new_author")

    def test_change_date(self):
        document = DocumentNode("test_title", "test_author", "2023-05-01",
                                "10.1016/j.nima.2023.168233", "/path/to/local/file")
        document.change_date("new_date")
        self.assertEqual(document.date, "new_date")

    def test_change_local_path(self):
        document = DocumentNode("test_title", "test_author", "2023-05-01",
                                "10.1016/j.nima.2023.168233", "/path/to/local/file")
        document.change_local_path("new_path")
        self.assertEqual(document.local_file_path, Path("new_path"))

    def test_serialize(self):
        document = DocumentNode("test_title", "test_author", "2023-05-01",
                                "10.1016/j.nima.2023.168233", "/path/to/local/file")
        serialized_data = document.serialize()
        self.assertEqual(serialized_data, {
            'title': 'test_title',
            'author': 'test_author',
            'date': '2023-05-01',
            'doi': '10.1016/j.nima.2023.168233',
            'local_path': "\\path\\to\\local\\file"
        })


if __name__ == '__main__':
    unittest.main()
