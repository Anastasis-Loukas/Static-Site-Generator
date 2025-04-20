from split_nodes_delimiter import *
from split_nodes_image import *
from split_nodes_link import *

def text_to_textnodes(text):
     # Start with one big text node
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Split based on different delimiters
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    #specialized functions for complex patterns
    nodes = split_nodes_image(nodes)  # function for handling ![alt](url)
    nodes = split_nodes_link(nodes)   # function for handling [text](url)
    
    return nodes