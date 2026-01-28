import unittest
from textnode import TextNode, TextType
from textparsing import split_nodes_delimiter
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_code(self):
        node = TextNode("Use `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            result,
            [
                TextNode("Use ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" here", TextType.TEXT)
            ]
        )

    def test_single_bold(self):
        node = TextNode("This is **bold_text** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold_text", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_invalid_syntax(self):
        node = TextNode("This is **bold_text without end", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)
