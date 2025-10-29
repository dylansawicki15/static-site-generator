import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "Hello, World! This is a test **bold** _italic_ `code`"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("Hello", TextType.TEXT), TextNode("World! This is a test", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode("italic", TextType.ITALIC), TextNode("code", TextType.CODE)])