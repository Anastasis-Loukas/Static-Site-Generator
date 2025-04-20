
from textnode import *
from htmlnode import *

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(text_node)

    
    # Test 1: Create an HTMLNode with some props
    node = HTMLNode(tag="a", value="Visit Boot.dev", props={"href": "https://boot.dev", "target": "_blank"})
    print("Props to HTML:", node.props_to_html())
    print("Representation:", repr(node))

    # Test 2: Create a node with no props
    empty_node = HTMLNode(tag="div", value="No props here.")
    print("Props to HTML (no props):", empty_node.props_to_html())
    print("Representation (no props):", repr(empty_node))

    # Test 3: Nested children example
    child1 = HTMLNode(tag="span", value="Child 1")
    child2 = HTMLNode(tag="span", value="Child 2")
    parent = HTMLNode(tag="div", children=[child1, child2])
    print("Representation (with children):", repr(parent))


    # Create some leaf nodes
    p_node = LeafNode("p", "Hello, world!")
    a_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    raw_node = LeafNode(None, "Just some text")
    
    # Print their HTML representations
    print(p_node.to_html())  # Should print: <p>Hello, world!</p>
    print(a_node.to_html())  # Should print: <a href="https://www.google.com">Click me!</a>
    print(raw_node.to_html())  # Should print: Just some text
    
    # Test the ValueError
    try:
        LeafNode("div", None)
        print("Failed: Should have raised ValueError")
    except ValueError as e:
        print(f"Success: Raised ValueError as expected: {e}")

if __name__ == "__main__":
    main()