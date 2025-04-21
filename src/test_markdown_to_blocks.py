import unittest
from markdown_to_blocks import *

from textwrap import dedent


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
            md = dedent("""
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """)
            
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
    def test_empty_input(self):
        md = ""
        self.assertEqual(markdown_to_blocks(md), [])

    def test_single_block(self):
        md = "# Heading"
        self.assertEqual(markdown_to_blocks(md), ["# Heading"])

    def test_excessive_blank_lines(self):
        md = "\n\n\n\n# Heading\n\n\n\nParagraph"
        self.assertEqual(markdown_to_blocks(md), ["# Heading", "Paragraph"])

    def test_leading_and_trailing_blank_lines(self):
        md = "\n\n# Heading\nParagraph\n\n"
        self.assertEqual(markdown_to_blocks(md), ["# Heading\nParagraph"])

    def test_all_blank_lines(self):
        md = "\n\n\n\n"
        self.assertEqual(markdown_to_blocks(md), [])