import unittest
from block_type import *

class TestBlockTypeDetection(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Secondary heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Level 6 heading"), BlockType.HEADING)
    
    def test_code(self):
        self.assertEqual(block_to_block_type("```\nsome code\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```\nmulti-line\ncode block\n```"), BlockType.CODE)
    
    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), BlockType.QUOTE)
    
    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item one"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- Item one\n- Item two"), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), BlockType.ORDERED_LIST)
    
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("This is a multi-line\nparagraph with several\nlines of text."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)  # Empty block