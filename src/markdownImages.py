import re

def extract_markdown_images(markdown_text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, markdown_text)
    return matches 

def extract_markdown_links(text):
    pattern = r"(?<!\!)\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)
    