from markdown_to_blocks import *
from block_type import *
from htmlnode import *
from text_to_textnodes import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        if block.strip():  # Only process non-empty blocks
            html_node = block_to_html_node(block)
            children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    # Join lines and normalize whitespace
    text = " ".join([line.strip() for line in block.split("\n")])
    # Create child nodes with inline formatting
    children = text_to_children(text)
    return ParentNode("p", children, None)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    # Split by lines and remove the code fence markers
    lines = block.strip().split("\n")
    
    # Find and remove the code fence lines
    clean_lines = []
    for line in lines:
        if line.strip() == "```":
            continue
        # Remove leading whitespace but preserve indentation within the code block
        clean_lines.append(line.strip())
    
    # Join the lines with newlines
    content = "\n".join(clean_lines)
    
    
    if content:
        content += "\n"
    
    # Create the HTML nodes
    code_node = LeafNode("code", content)
    pre_node = ParentNode("pre", [code_node])
    
    return pre_node

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    
    for item in items:
        item = item.strip()
        # Check if the line is a numbered list item
        if re.match(r"^\d+\.\s", item):
            # Find the position after the number and period
            pos = item.find(". ") + 2
            text = item[pos:]
            children = text_to_children(text)
            html_items.append(ParentNode("li", children))
    
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    
    for item in items:
        item = item.strip()
        # Only process lines that are actually list items
        if item.startswith("- "):
            # Extract the text after the "- " prefix
            text = item[2:]
            children = text_to_children(text)
            html_items.append(ParentNode("li", children))
    
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    # Extract content from blockquote lines
    lines = block.strip().split("\n")
    content_lines = []
    
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            # Remove the '>' and trim whitespace
            line_content = line[1:].strip()
            content_lines.append(line_content)
    
    # Join with spaces (not newlines)
    content = " ".join(content_lines)
    
    # Process any inline formatting in the content
    children = text_to_children(content)
    
    # Create and return the blockquote node
    return ParentNode("blockquote", children)


# def text_to_children(text):
#     # Step 1: Convert text to a list of TextNodes
#     text_nodes = text_to_textnodes(text)
    
#     # Step 2: Convert each TextNode to an HTMLNode
#     html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    
#     # Step 3: Return the list of HTMLNode objects
#     return html_nodes

# def split_list_block(block):
#     lines = block.split("\n")  # Split block into lines
#     return [line.strip()[2:] for line in lines if line.strip()]

# def split_list_block2(block):
#     lines = block.split("\n")  # Split block into lines
#     return [line.strip()[3:] for line in lines if line.strip()]


# def markdown_to_html_node(markdown):
#     BLOCK_TYPE_TO_HTML_TAG = {
#         BlockType.PARAGRAPH: "p",
#         BlockType.HEADING: "h1",  # Default assignment, adjusted dynamically later
#         BlockType.CODE: "pre",
#         BlockType.QUOTE: "blockquote",
#         BlockType.UNORDERED_LIST: "ul",
#         BlockType.ORDERED_LIST: "ol",
#     }

#     blocks = markdown_to_blocks(markdown)  # Step 1: Split the markdown into blocks
    
#     # List to collect all block nodes
#     child_nodes = []

#     for block in blocks:
#         block_type = block_to_block_type(block)  # Step 1.2: Determine the block type
#         tag = BLOCK_TYPE_TO_HTML_TAG.get(block_type)  # Get the default HTML tag

#         # Handle special case - HEADING
#         if block_type == BlockType.HEADING:
#             # Determine the heading level based on the number of `#`
#             heading_level = 0
#             for char in block:
#                 if char == '#':
#                     heading_level += 1
#                 else:
#                     break
            
#             # Adjust the tag dynamically for heading levels (h1, h2, etc.)
#             tag = f"h{heading_level}"
            
#             # Parse children (inline Markdown parsing for headings)
#             children = text_to_children(block)
#             html_node = ParentNode(tag=tag, children=children)

#         # Handle special case - CODE
#         # Handle BlockType.CODE
#         elif block_type == BlockType.CODE:
#             # Step 1: Strip the triple backticks and surrounding whitespace
#             lines = block.strip().splitlines()  # Split block into lines and strip whitespace
            
#             # Step 2: Filter out any lines containing just backticks (e.g., the start/end markers)
#             content_lines = [line for line in lines if not line.strip().startswith("```")]

#             # Step 3: Normalize indentation by finding the minimum leading spaces across all lines
#             if content_lines:
#                 min_indent = min(len(line) - len(line.lstrip()) for line in content_lines if line.strip())
#                 normalized_lines = [line[min_indent:] for line in content_lines]
#             else:
#                 normalized_lines = []

#             # Step 4: Join the normalized lines back into a single string with preserved line breaks
#             code_text = "\n".join(normalized_lines)

#             # Step 5: Create a LeafNode for the raw code (tag="code", value=code_text)
#             text_node = LeafNode(tag="code", value=code_text)

#             # Step 6: Wrap the LeafNode in a ParentNode with <pre> (outermost wrapper)
#             html_node = ParentNode(tag="pre", children=[text_node])

#         # Handle BlockType.UNORDERED_LIST
#         elif block_type == BlockType.UNORDERED_LIST:
#             # Step 1: Split the block into list items
#             list_items = split_list_block(block)  # Define this helper function!
            
#             # Step 2: Convert each list item to an <li> node
#             li_nodes = []
#             for item in list_items:
#                 # Parse children (handles inline markdown within the list items)
#                 children = text_to_children(item)  
#                 li_nodes.append(HTMLNode(tag="li", children=children))
            
#             # Step 3: Wrap <li> nodes inside a parent <ul> node
#             html_node = HTMLNode(tag="ul", children=li_nodes)
#         # Handle BlockType.ORDERED_LIST
#         elif block_type == BlockType.ORDERED_LIST:
#             # Step 1: Split the block into list items
#             list_items = split_list_block2(block)  # A helper function, same as for <ul>
            
#             # Step 2: Convert each list item to an <li> node
#             li_nodes = []
#             for item in list_items:
#                 # Parse children (handles inline markdown within the list items)
#                 children = text_to_children(item)
#                 li_nodes.append(ParentNode(tag="li", children=children))
            
#             # Step 3: Wrap <li> nodes inside a parent <ol> node
#             html_node = ParentNode(tag="ol", children=li_nodes)
#         # Step 2: Process the block based on the type
#         elif block_type == BlockType.PARAGRAPH:
#             # Handle paragraphs
#             children = text_to_children(block.strip())
#             html_node = ParentNode(tag="p", children=children)

#         elif block_type == BlockType.QUOTE:
#             # Handle quotes
#             # Remove the '> ' marker and parse inline markdown into children
#             children = text_to_children(block.strip("> ").strip())
#             html_node = ParentNode(tag="blockquote", children=children)

#                 # Add the processed `HTMLNode` to the list of child nodes
#         child_nodes.append(html_node)

#         # Wrap all block nodes inside a single `div` parent node
#     return ParentNode(tag="div", children=child_nodes)
        