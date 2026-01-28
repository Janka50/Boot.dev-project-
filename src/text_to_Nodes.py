from src.splitNodes import split_nodes_images, split_nodes_links
from src.textnode import TextNode, TextType
from src.textparsing import split_nodes_delimiter
from src.htmlnode import LeafNode  # LeafNode represents a final HTML element like <b>, <i>, <code>
from src.textnode import TextNode, TextType
from src.splitNodes import split_nodes_images, split_nodes_links


def text_to_textnodes(text):
    nodes =  [TextNode(text, TextType.TEXT)]
#inline delimiters

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

 #markdown images and links
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes 




def text_to_children(text: str):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_links(nodes)
    nodes = split_nodes_images(nodes)

    return nodes


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TextType.LINK:
        return LeafNode(
            "a",
            text_node.text,
            {"href": text_node.url},
        )

    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            "img",
            "",
            {"src": text_node.url, "alt": text_node.text},
        )

    raise ValueError(f"Unsupported text type: {text_node.text_type}")