import unittest
from extract_markdown import *


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_images(self): # multiple images
        matches = extract_markdown_images(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"),("obi wan","https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def test_extract_markdown_links(self): # multiple links
        matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),("to youtube","https://www.youtube.com/@bootdotdev")], matches)
    
    #for extract title

    import unittest

class TestExtractTitle(unittest.TestCase):
    
    def test_standard_title(self):
        markdown = "# This is a title\nSome content here."
        self.assertEqual(extract_title(markdown), "This is a title")
    
    def test_title_with_extra_whitespace(self):
        markdown = "#    Title with extra space    \nContent here."
        self.assertEqual(extract_title(markdown), "Title with extra space")
    
    def test_title_with_leading_whitespace(self):
        markdown = "    # Title with indentation\nContent here."
        self.assertEqual(extract_title(markdown), "Title with indentation")
    
    def test_title_without_space_after_hash(self):
        markdown = "#No space after hash\nContent here."
        self.assertEqual(extract_title(markdown), "No space after hash")
    
    def test_title_with_multiple_spaces_everywhere(self):
        markdown = "   #     Lots   of    spaces    \nContent here."
        self.assertEqual(extract_title(markdown), "Lots   of    spaces")
    
    def test_multiple_headers(self):
        markdown = "# First title\n## Second level\n# Another h1\nContent."
        self.assertEqual(extract_title(markdown), "First title")
    
    def test_header_with_special_characters(self):
        markdown = "# Title with *bold* and [link](https://example.com)\nContent."
        self.assertEqual(extract_title(markdown), "Title with *bold* and [link](https://example.com)")
    
    def test_no_h1_header(self):
        markdown = "## Secondary header\nNo primary header here."
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_empty_markdown(self):
        markdown = ""
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_h1_header_not_at_beginning(self):
            markdown = "Some introductory text\n\n# Title in the middle\nMore content."
            self.assertEqual(extract_title(markdown), "Title in the middle")
    
    def test_hash_in_code_block(self):
        markdown = "```python\n# This is a comment in a code block\n```\n\nMore content."
        self.assertEqual(extract_title(markdown), "This is a comment in a code block")
    
    def test_header_with_punctuation(self):
        markdown = "# Is this a header? Yes!"
        self.assertEqual(extract_title(markdown), "Is this a header? Yes!")
    
    def test_multiline_header(self):
        markdown = "# This header \ncontinues on next line\n\nActual content."
        self.assertEqual(extract_title(markdown), "This header")


