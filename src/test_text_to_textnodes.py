import unittest
from textnode import *
from text_to_textnodes import *


class TestExtractMarkdown(unittest.TestCase):
    def test_text_to_textnodes_simple_text(self):
        text = "Hello world"
        expected = [TextNode("Hello world", TextType.TEXT)]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, got {actual}"
    def test_text_to_textnodes_bold_text(self):
        text = "Hello **world**"
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD)
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, got {actual}"
    def test_text_to_textnodes_italic_text(self):
        text = "Hello _world_"
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.ITALIC)
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, got {actual}"
    def test_text_to_textnodes_code_text(self):
        text = "Hello `world`"
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.CODE)
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, got {actual}"
    def test_text_to_textnodes_link(self):
        text = "Check out [this link](https://boot.dev)"
        expected = [
            TextNode("Check out ", TextType.TEXT),
            TextNode("this link", TextType.LINK, "https://boot.dev")
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, got {actual}"
    def test_text_to_textnodes_image(self):
        text = "Check out ![image](https://example.com/img.jpg)"
        expected = [
            TextNode("Check out ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.jpg")
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, got {actual}"
    def test_text_to_textnodes_complex(self):
        text = "This is **bold** with an _italic_ word and `code` plus a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" plus a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        actual = text_to_textnodes(text)
        assert actual == expected, f"Expected {expected}, got {actual}"