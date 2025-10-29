import unittest

from textnode import TextNode, TextType
from split_nodes_image_and_link import split_nodes_image, split_nodes_link

class TestSplitNodesImageAndLink(unittest.TestCase):
    def test_split_nodes_image(self):
        nodes = [TextNode("This is text before ![image](https://i.imgur.com/zjjcJKZ.png) and after", TextType.IMAGE)]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(new_nodes, [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")])

    def test_split_nodes_link(self):
        nodes = [TextNode("This is text before [link](https://example.com) and after", TextType.LINK)]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual([TextNode("link", TextType.LINK, "https://example.com")], new_nodes)
    
    def test_split_multiple_nodes_image(self):
        nodes = [
            TextNode("![first image](https://i.imgur.com/zjjcJKZ.png) and ![second image](https://example.com/image.png)", TextType.IMAGE),
            TextNode("This is a text with no image", TextType.TEXT),
            TextNode("Another image ![third](https://i.imgur.com/xyz.png)", TextType.IMAGE)
        ]
        new_nodes = split_nodes_image(nodes)
        expected = [
            TextNode("first image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("second image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode("This is a text with no image", TextType.TEXT),
            TextNode("third", TextType.IMAGE, "https://i.imgur.com/xyz.png")
        ]
        self.assertListEqual(expected, new_nodes)
    
    def test_split_multiple_nodes_link(self):
        nodes = [
            TextNode("[first link](https://example.com) and [second link](https://boot.dev)", TextType.LINK),
            TextNode("This is a text with no link", TextType.TEXT),
            TextNode("Another link [third](https://google.com)", TextType.LINK)
        ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode("first link", TextType.LINK, "https://example.com"),
            TextNode("second link", TextType.LINK, "https://boot.dev"),
            TextNode("This is a text with no link", TextType.TEXT),
            TextNode("third", TextType.LINK, "https://google.com")
        ]
        self.assertListEqual(expected, new_nodes)