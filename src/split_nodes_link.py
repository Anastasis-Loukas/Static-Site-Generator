from extract_markdown import extract_markdown_links
from textnode import *

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
       
        text = old_node.text
        
        
        links = extract_markdown_links(text)
        
        
        if len(links) == 0:
            result.append(old_node)
            continue
            
       
        remaining_text = text
        
        for link_text, link_url in links:
            
            link_markdown = f"[{link_text}]({link_url})"
            
            
            parts = remaining_text.split(link_markdown, 1)
            
            
            if parts[0]:  
                result.append(TextNode(parts[0], TextType.TEXT))
                
            
            result.append(TextNode(link_text, TextType.LINK, link_url))
            
           
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
            
    return result