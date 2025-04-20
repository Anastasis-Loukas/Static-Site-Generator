import unittest
from split_nodes_image import *
from split_nodes_link import *


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_basic(self):
    # Test with a single image
        node = TextNode(
            "This is text with an ![image](https://example.com/img.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
            ],
            new_nodes,
        )

    def test_split_image_no_images(self):
        # Test with no images
        node = TextNode("This is text with no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_nodes_image_at_start(self):
        # Test with image at the beginning
        node = TextNode(
            "![start image](https://example.com/start.png) followed by text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("start image", TextType.IMAGE, "https://example.com/start.png"),
                TextNode(" followed by text", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_nodes_image_multiple_nodes(self):
        # Test with multiple nodes, some containing multiple images
        node1 = TextNode(
            "First node with ![image1](https://example.com/img1.png) and ![image2](https://example.com/img2.png)",
            TextType.TEXT,
        )
        node2 = TextNode("Second node with no images", TextType.TEXT)
        node3 = TextNode(
            "Third node with ![image3](https://example.com/img3.png)",
            TextType.TEXT,
        )
        
        new_nodes = split_nodes_image([node1, node2, node3])
        
        self.assertListEqual(
            [
                TextNode("First node with ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "https://example.com/img1.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "https://example.com/img2.png"),
                TextNode("Second node with no images", TextType.TEXT),
                TextNode("Third node with ", TextType.TEXT),
                TextNode("image3", TextType.IMAGE, "https://example.com/img3.png"),
            ],
            new_nodes,
        )
class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link_basic(self):
    # Test with a single link
        node = TextNode(
            "This is text with a [link](https://example.com/page)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com/page"),
            ],
            new_nodes,
        )
    def test_split_nodes_link_multiple(self):
    # Test with multiple links
        node = TextNode(
            "This is text with a [link](https://example.com/page) and another [second link](https://example.org/other)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com/page"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://example.org/other"),
            ],
            new_nodes,
        )
    def test_split_nodes_link_no_links(self):
    # Test with no links
        node = TextNode("This is text with no links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
    def test_split_nodes_link_at_start(self):
    # Test with link at the beginning
        node = TextNode(
            "[start link](https://example.com/start) followed by text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("start link", TextType.LINK, "https://example.com/start"),
                TextNode(" followed by text", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_nodes_link_multiple_nodes(self):
    # Test with multiple nodes, some containing multiple links
        node1 = TextNode(
            "First node with [link1](https://example.com/link1) and [link2](https://example.com/link2)",
            TextType.TEXT,
        )
        node2 = TextNode("Second node with no links", TextType.TEXT)
        node3 = TextNode(
            "Third node with [link3](https://example.com/link3)",
            TextType.TEXT,
        )
        
        new_nodes = split_nodes_link([node1, node2, node3])
        
        self.assertListEqual(
            [
                TextNode("First node with ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "https://example.com/link1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "https://example.com/link2"),
                TextNode("Second node with no links", TextType.TEXT),
                TextNode("Third node with ", TextType.TEXT),
                TextNode("link3", TextType.LINK, "https://example.com/link3"),
            ],
            new_nodes,
        )