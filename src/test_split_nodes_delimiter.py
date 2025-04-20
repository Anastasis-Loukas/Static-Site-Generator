import unittest
from split_nodes_delimiter import *

class TestSplitNodesDelimeter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
    # Test 1: Basic case with a single delimiter pair
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This is text with a "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "code block"
        assert new_nodes[1].text_type == TextType.CODE
        assert new_nodes[2].text == " word"
        assert new_nodes[2].text_type == TextType.TEXT
    def test_split_nodes_delimiter_multiple(self):   
        # Test 2: Multiple occurrences of delimiter
        node = TextNode("This has `code` and `more code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(new_nodes) == 4
       
       # First text node (before first delimiter)
        assert new_nodes[0].text == "This has "
        assert new_nodes[0].text_type == TextType.TEXT
        
        # First code node
        assert new_nodes[1].text == "code"
        assert new_nodes[1].text_type == TextType.CODE
        
        # Middle text node (between code blocks)
        assert new_nodes[2].text == " and "
        assert new_nodes[2].text_type == TextType.TEXT
        
        # Second code node
        assert new_nodes[3].text == "more code"
        assert new_nodes[3].text_type == TextType.CODE
        
    def test_split_nodes_delimiter_error(self):   
        # Test 3: Empty sections
        node = TextNode("`code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(new_nodes) == 1
        assert new_nodes[0].text == "code"
        assert new_nodes[0].text_type == TextType.CODE
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This has **bold text** in it", TextType.TEXT) 
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This has "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "bold text"
        assert new_nodes[1].text_type == TextType.BOLD
        assert new_nodes[2].text == " in it"
        assert new_nodes[2].text_type == TextType.TEXT
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This has _italic text_ in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "This has "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "italic text"
        assert new_nodes[1].text_type == TextType.ITALIC
        assert new_nodes[2].text == " in it"
        assert new_nodes[2].text_type == TextType.TEXT
    def test_split_nodes_delimiter_mixed_nodes(self): # is this 100% correct ???
    # Start with a mix of TEXT and BOLD nodes
        nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this has `code` in it", TextType.TEXT)
        ]
        
        # Apply code delimiter
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        
        # Should split the last TEXT node and leave the BOLD node alone
        assert len(new_nodes) == 5
        assert new_nodes[0].text == "This is "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "bold"
        assert new_nodes[1].text_type == TextType.BOLD
        assert new_nodes[2].text == " and this has "
        assert new_nodes[2].text_type == TextType.TEXT
        assert new_nodes[3].text == "code"
        assert new_nodes[3].text_type == TextType.CODE
        assert new_nodes[4].text == " in it"
        assert new_nodes[4].text_type == TextType.TEXT