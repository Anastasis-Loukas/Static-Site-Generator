from enum import Enum

class TextType(Enum):
   TEXT = "text"
   BOLD = "bold"
   ITALIC = "italic"
   CODE = "code"
   LINK = "link"
   IMAGE = "image"
   
class TextNode:
   def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
   def __eq__(self, text_node):
       return (self.text == text_node.text and 
            self.text_type == text_node.text_type and 
            self.url == text_node.url)
   def __repr__(self):
       text_type_str = self.text_type if isinstance(self.text_type, str) else self.text_type.value
       return f"TextNode({self.text}, {text_type_str}, {self.url})" 
       
   