import re
from enum import Enum

class BlockType(Enum):
   PARAGRAPH = "paragraph"
   HEADING = "heading"
   CODE = "code"
   QUOTE = "quote"
   UNORDERED_LIST = "unordered_list"
   ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    # Filter out empty lines
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    
    if not non_empty_lines:
        return BlockType.PARAGRAPH
        
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
        
    if len(lines) > 1 and block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
        
    if non_empty_lines[0].startswith(">"):
        if all(line.startswith(">") for line in non_empty_lines):
            return BlockType.QUOTE
        return BlockType.PARAGRAPH
        
    # Check for unordered list - all non-empty lines must start with "- "
    if all(line.startswith("- ") for line in non_empty_lines):
        return BlockType.UNORDERED_LIST
        
    # Check for ordered list - all non-empty lines must start with a number followed by period and space
    if all(re.match(r"^\d+\.\s", line) for line in non_empty_lines):
        return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH


# def check_ordered_list(block):
#     lines = block.split('\n')
#     for i, line in enumerate(lines, 1):
#         # Check if line starts with number + period + space
#         # And the number matches the line number
#         if not re.match(rf'^{i}\. ', line):
#             return False
#     return True

# def block_to_block_type(block): # return type
#         if(re.match(r'^#{1,6} .*',block)) :
#             return BlockType.HEADING
#         elif(block.startswith('```') and block.endswith('```')):
#             return BlockType.CODE
#         elif(all(line.startswith('>') for line in block.split('\n'))):
#             return BlockType.QUOTE
#         elif(all(line.startswith('- ') for line in block.split('\n'))):
#             return BlockType.UNORDERED_LIST
#         elif(check_ordered_list(block)):
#             return BlockType.ORDERED_LIST
#         else: 
#             return BlockType.PARAGRAPH
        

   
