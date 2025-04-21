import re


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
     # images
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_title(markdown):
    lines = markdown.splitlines()
    
    for line in lines:
        # Strip leading/trailing whitespace
        line = line.strip()
        
        # Check if it's an h1 header (starts with single #)
        if line.startswith("#") and not line.startswith("##"):
            # Remove the # and strip whitespace
            title = line[1:].strip()
            return title
    
    raise Exception("No h1 header found in the markdown")
