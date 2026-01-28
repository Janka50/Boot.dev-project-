import unittest
from textnode import TextNode, TextType
from markdownImages import extract_markdown_links
from splitNodes import split_nodes_images,  split_nodes_links
from textnode import TextType as t

class TestSplitNodesImage(unittest.TestCase):
    def test_single_image(self):
        nodes = [
            TextNode(
                "This is ![cat](cat.png)",
                TextType.TEXT
            )
        ]

        result = split_nodes_images(nodes)

        self.assertEqual(
            result,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("cat", TextType.IMAGE, "cat.png"),
            ]
        )



class TestSplitNodesLink(unittest.TestCase):
    def test_single_link(self):
        nodes = [
            TextNode(
                "Go to [Boot.dev](https://www.boot.dev)",
                TextType.TEXT
            )
        ]

        result = split_nodes_links(nodes)

        self.assertEqual(
            result,
            [
                TextNode("Go to ", TextType.TEXT),
                TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
            ]
        )



if __name__ == "__main__":
    unittest.main()
