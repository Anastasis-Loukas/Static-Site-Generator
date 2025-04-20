
from textnode import *

class HTMLNode:
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        attributes = []
        if not self.props:
            return ''  # Return an empty string for no props
        for k, v in self.props.items():
            attributes.append(f'{k}="{v}"')  # Each attribute added as key="value"
        return " " + " ".join(attributes)  # Join with spaces and add leading space
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag},value={self.value},children={self.children},props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Call the parent constructor
        # Assuming HTMLNode has children as a parameter with default empty list
        super().__init__(tag, value, [], props)

        # Ensure value is provided (not None)
        if value is None:
            raise ValueError("LeafNode must have a value")
    def to_html(self):
        #print("to_html method in LeafNode called")  # Debug print
        if(self.value is None):
            raise ValueError("All leaf nodes must have a value.")
        if(self.tag is None):
            return self.value
        # Build opening tag with props if they exist
        opening_tag = f"<{self.tag}"
        if self.props:
            for key, value in self.props.items():
                opening_tag += f' {key}="{value}"'
        opening_tag += ">"
        
        # Create the full HTML string with opening tag, value, and closing tag
        return f"{opening_tag}{self.value}</{self.tag}>"
class ParentNode(HTMLNode):
    def __init__(self, tag,children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        
        if(self.tag is None):
            raise ValueError("Missing tag")
        if self.children is None:  # or possibly: if not self.children
            raise ValueError("Missing children")
        # Create opening tag
        html = f"<{self.tag}"
        # Add props if they exist
        if self.props:
            # Logic to handle props
            for prop_name, prop_value in self.props.items():
                html += f' {prop_name}="{prop_value}"'
        html += ">"
        
        # Add children's HTML
        for child in self.children:
            html += child.to_html()  # Recursive call!
        
        # Add closing tag
        html += f"</{self.tag}>"

        return html

def text_node_to_html_node(text_node):
    if(text_node.text_type == TextType.TEXT):
        # For TEXT type, no tag is needed, just the text value
        return LeafNode(None, text_node.text)
    elif(text_node.text_type == TextType.BOLD):
        return LeafNode("b", text_node.text)
    elif(text_node.text_type == TextType.ITALIC):
        return LeafNode("i", text_node.text)
    elif(text_node.text_type == TextType.CODE):
       return LeafNode("code", text_node.text)
    elif(text_node.text_type == TextType.LINK):
       return LeafNode("a", text_node.text,{"href": text_node.url})
    elif(text_node.text_type == TextType.IMAGE):
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception(f"Invalid text type: {text_node.text_type}")
        



  

            