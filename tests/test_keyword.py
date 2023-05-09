import unittest
from app.model.keyword_node import KeywordNode


class TestKeywordNode(unittest.TestCase):

    def test_initialization(self):
        keyword = KeywordNode("test_keyword", "test_description")
        self.assertEqual(keyword.name, "test_keyword")
        self.assertEqual(keyword.description, "test_description")

    def test_rename(self):
        keyword = KeywordNode("test_keyword", "test_description")
        keyword.rename("new_test_keyword")
        self.assertEqual(keyword.name, "new_test_keyword")

    def test_change_description(self):
        keyword = KeywordNode("test_keyword", "test_description")
        keyword.change_description("new_test_description")
        self.assertEqual(keyword.description, "new_test_description")

    def test_serialize(self):
        keyword = KeywordNode("test_keyword", "test_description")
        serialized_data = keyword.serialize()
        self.assertEqual(serialized_data, {
            'name': 'test_keyword',
            'description': 'test_description'
        })


if __name__ == '__main__':
    unittest.main()
