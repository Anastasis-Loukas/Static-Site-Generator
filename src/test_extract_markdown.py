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

