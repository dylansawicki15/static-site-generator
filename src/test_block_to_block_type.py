import unittest

from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    def test_block_to_block_type_code(self):
        block = "```python\nprint('Hello, World!')```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    def test_block_to_block_type_quote(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    def test_block_to_block_type_unordered_list(self):
        block = "- This is a list item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    def test_block_to_block_type_ordered_list(self):
        block = """1. This is a list item
2. This is another list item
3. This is a third list item"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)