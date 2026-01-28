from src.textnode import TextNode, TextType
from copy_static import copy_recursive_directory
from src.generate_page import generate_page
from src.generate_pages_recursive import generate_pages_recursive
from src.text_to_Nodes import text_to_children
import sys

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    node = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.boot.dev"
    )
    
    copy_recursive_directory("static", "docs")
    print("Static files copied Successfully...")
    
    
    print(text_to_children("Hello **world** ![img](x.png)"))
    generate_page(
        from_path="content/index.md",
        template_path="template.html",
        dest_path="public/index.html",
        basepath=basepath
    )
    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath
        
    )

if __name__ == "__main__":

  main()