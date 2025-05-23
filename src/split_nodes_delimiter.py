
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []

#     for node in old_nodes:
#         if(node.text_type == TextType.TEXT):
#             start_pos = node.text.find(delimiter)
#             if start_pos != -1:  # If delimiter found
#             # Look for closing delimiter after the first one
#                 end_pos = node.text.find(delimiter, start_pos + len(delimiter))
#                 if end_pos != -1:  # If closing delimiter found
#                     before_text = node.text[:start_pos]
#                     if before_text:  # This checks if the string is not empty
#                         new_nodes.append(TextNode(before_text, TextType.TEXT))

#                     between_text = node.text[start_pos + len(delimiter):end_pos]
#                     if between_text:
#                         new_nodes.append(TextNode(between_text, text_type))

#                     after_text = node.text[end_pos + len(delimiter):]
#                     if after_text:
#                         new_nodes.extend(split_nodes_delimiter([TextNode(after_text, TextType.TEXT)], delimiter, text_type))
#                 else:
#                     raise Exception("that's invalid Markdown syntax")

#             else:
#                 new_nodes.append(node)


#         else:
#             new_nodes.append(node)

#     return new_nodes    