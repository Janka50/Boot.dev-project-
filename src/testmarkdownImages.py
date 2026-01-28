import unittest
from markdownImages import extract_markdown_links 
from textnode import TextNode# replace 'your_module' with your actual filename

class TestMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
     text = "This is a [Boot.dev](https://www.boot.dev) link"
     result = extract_markdown_links(text)
     expected = [("Boot.dev", "https://www.boot.dev")]
     self.assertListEqual(result, expected)

    def test_multiple_links(self):
     text = "Links: [Boot.dev](https://www.boot.dev) and [YouTube](https://www.youtube.com)"
     result = extract_markdown_links(text)
     expected = [
        ("Boot.dev", "https://www.boot.dev"),
        ("YouTube", "https://www.youtube.com"),
    ]
     self.assertListEqual(result, expected)
    
    def test_ignore_images(self):
     text = "Here is a [link](https://link.com) and an ![image](https://img.com)"
     result = extract_markdown_links(text)
     expected = [("link", "https://link.com")]
     self.assertListEqual(result, expected)
    
    def test_no_links(self):
     text = "Just some text without links"
     result = extract_markdown_links(text)
     expected = []
     self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()