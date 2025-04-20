import unittest
from htmlnode import *  # Ensure your file is named correctly!

class TestHTMLNode(unittest.TestCase):
    def test_multiple_attributes(self):
        node = HTMLNode(tag="a", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com" target="_blank"')

    def test_empty_props(self):
        node = HTMLNode(tag="div", props={})
        self.assertEqual(node.props_to_html(), '')

    def test_one_attribute(self):
        node = HTMLNode(tag="p", props={"class": "text"})
        self.assertEqual(node.props_to_html(), ' class="text"')
    def test_repr(self):
        node = HTMLNode(tag="p", value="Hello, world!", children=[], props={"class": "greeting"})
        self.assertEqual(
        repr(node),
        "HTMLNode(tag=p,value=Hello, world!,children=[],props={'class': 'greeting'})"
        )

        # Test with None values
        node_none = HTMLNode()
        self.assertEqual(
        repr(node_none),
        "HTMLNode(tag=None,value=None,children=None,props=None)"
        )
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")
    
    def test_leaf_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()
    def test_leaf_no_value_constructor(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)
        
    def test_leaf_value_becomes_none(self):
        node = LeafNode("p", "Hello")
        # Simulate the value being changed to None after creation , or was already None
        node.value = None
        with self.assertRaises(ValueError):
            node.to_html()
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
    def test_parent_with_properties(self):
        child = LeafNode("span", "text")
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><span>text</span></div>')

    def test_missing_tag(self):
        child = LeafNode("span", "text")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_complex_nesting(self):
        innermost = LeafNode("b", "bold text")
        inner = ParentNode("p", [innermost, LeafNode(None, "normal text")])
        outer = ParentNode("div", [
            LeafNode("h1", "Title"),
            inner,
            LeafNode("footer", "Copyright")
        ])
        # Check the resulting HTML string
        self.assertEqual(
        outer.to_html(),
        "<div><h1>Title</h1><p><b>bold text</b>normal text</p><footer>Copyright</footer></div>"
    )
        
    def test_none_children_raises_error(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()
    def test_empty_children_list(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")
    
    
    
class TestTextNodeToHtmlNode(unittest.TestCase):
        def test_text(self):
            node = TextNode("This is a text node", TextType.TEXT)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "This is a text node")
            self.assertEqual(html_node.props, None
                             )
        def test_bold(self):
            node = TextNode("This is bold text", TextType.BOLD)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "b")
            self.assertEqual(html_node.value, "This is bold text")
            self.assertEqual(html_node.props, None)

        def test_italic(self):
            node = TextNode("This is italic text", TextType.ITALIC)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "i")
            self.assertEqual(html_node.value, "This is italic text")
            self.assertEqual(html_node.props, None)

        def test_code(self):
            node = TextNode("This is code", TextType.CODE)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "code")
            self.assertEqual(html_node.value, "This is code")
            self.assertEqual(html_node.props, None)

        def test_link(self):
            node = TextNode("Click me", TextType.LINK, "https://example.com")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "a")
            self.assertEqual(html_node.value, "Click me")
            self.assertEqual(html_node.props, {"href": "https://example.com"})

        def test_image(self):
            node = TextNode("Alt text", TextType.IMAGE, "https://example.com/image.png")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "img")
            self.assertEqual(html_node.value, "")
            self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "Alt text"})

