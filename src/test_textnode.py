import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is different text", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD,'www.example.com') #1
        node2 = TextNode("This is a text node", TextType.BOLD,None)
        self.assertNotEqual(node, node2)
    def test_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD) #2
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_different_text_and_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD) #3
        node2 = TextNode("This is different text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()