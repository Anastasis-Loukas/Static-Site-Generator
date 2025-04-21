#import re

# def markdown_to_blocks(markdown):
#     markdown = markdown.strip()
#     all_blocks = re.split(r'\n\s*\n', markdown)
#     blocks = [block.strip() for block in all_blocks if block.strip()]
#     return blocks

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
