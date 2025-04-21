import os
from generate_page import *

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath):
    entries = os.listdir(dir_path_content)
    
    for entry in entries:
        entry_path = os.path.join(dir_path_content, entry)
        
        if os.path.isfile(entry_path) and entry.endswith('.md'):
            # Calculate relative path and destination
            rel_path = os.path.relpath(entry_path, dir_path_content)
            # Change extension from .md to .html
            rel_path_html = os.path.splitext(rel_path)[0] + '.html'
            dest_path = os.path.join(dest_dir_path, rel_path_html)
            
            # Make sure the destination directory exists
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            # Generate the HTML using your existing function
            generate_page(entry_path, template_path, dest_path,basepath)
            
        elif os.path.isdir(entry_path):
            # Create corresponding directory in destination
            new_dest_dir = os.path.join(dest_dir_path, entry)
            os.makedirs(new_dest_dir, exist_ok=True)
            
            # Recursively process the subdirectory
            generate_pages_recursive(entry_path, template_path, new_dest_dir,basepath)
