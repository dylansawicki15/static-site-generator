import unittest

from textnode import TextNode, TextType
from split_delimiter import split_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter(self):
        nodes = [TextNode("Hello, World!", TextType.TEXT), TextNode("This is a test", TextType.TEXT)]
        new_nodes = split_delimiter(nodes, ",", TextType.TEXT)
        self.assertEqual(new_nodes, [TextNode("Hello", TextType.TEXT), TextNode(" World!", TextType.TEXT), TextNode("This is a test", TextType.TEXT)])
    def test_split_delimiter_with_multiple_delimiters(self):
        nodes = [TextNode("Hello, World, This is a test", TextType.TEXT)]
        new_nodes = split_delimiter(nodes, ",", TextType.TEXT)
        self.assertEqual(new_nodes, [TextNode("Hello", TextType.TEXT), TextNode(" World", TextType.TEXT), TextNode(" This is a test", TextType.TEXT)])
    def test_split_delimiter_with_multiple_delimiters_and_multiple_nodes(self):
        nodes = [TextNode("Hello, World", TextType.TEXT), TextNode("This is a test", TextType.TEXT)]
        new_nodes = split_delimiter(nodes, ",", TextType.TEXT)
        self.assertEqual(new_nodes, [TextNode("Hello", TextType.TEXT), TextNode(" World", TextType.TEXT), TextNode("This is a test", TextType.TEXT)])
    def test_split_delimiter_bold(self):
        nodes = [TextNode("Hello, World!", TextType.BOLD)]
        new_nodes = split_delimiter(nodes, ",", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("Hello", TextType.BOLD), TextNode(" World!", TextType.BOLD)])
    def test_split_delimiter_italic(self):
        nodes = [TextNode("Hello, World!", TextType.ITALIC)]
        new_nodes = split_delimiter(nodes, ",", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("Hello", TextType.ITALIC), TextNode(" World!", TextType.ITALIC)])
    def test_split_delimiter_code(self):
        nodes = [TextNode("Hello, World!", TextType.CODE)]
        new_nodes = split_delimiter(nodes, ",", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("Hello", TextType.CODE), TextNode(" World!", TextType.CODE)])
