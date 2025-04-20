from extract_markdown import extract_markdown_images
from textnode import *

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
       # Get the text content of the current node
        text = old_node.text
        
        # Use your extract_markdown_images function to find images
        images = extract_markdown_images(text)
        
        # If no images found, keep the node as is
        if len(images) == 0:
            result.append(old_node)
            continue
            
        # Start with the original text
        remaining_text = text
        
        for image_alt, image_url in images:
            # Find where the image markdown starts
            image_markdown = f"![{image_alt}]({image_url})"
            
            # Split at the image markdown (only split once)
            parts = remaining_text.split(image_markdown, 1)
            
            # parts[0] is text before the image
            if parts[0]:  # Only add if not empty
                result.append(TextNode(parts[0], TextType.TEXT))
                
            # Add the image node
            result.append(TextNode(image_alt, TextType.IMAGE, image_url))
            
            # The rest becomes the remaining text for next iteration
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        # Don't forget text after the last image
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
            
    return result
