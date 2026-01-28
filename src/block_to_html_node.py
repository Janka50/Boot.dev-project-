from src.htmlnode import ParentNode, LeafNode
from src.text_to_Nodes import text_to_children, text_node_to_html_node
from src.block_type import block_to_block_type
def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == "heading":
        level = len(block.split(" ")[0])
        text = block[level + 1 :]
        children = [
            text_node_to_html_node(n)
            for n in text_to_children(text)
        ]
        return ParentNode(f"h{level}", children)

    if block_type == "paragraph":
        children = [
            text_node_to_html_node(n)
            for n in text_to_children(block)
        ]
        return ParentNode("p", children)

    if block_type == "quote":
        text = "\n".join(line[2:] for line in block.split("\n"))
        children = [
            text_node_to_html_node(n)
            for n in text_to_children(text)
        ]
        return ParentNode("blockquote", children)

    if block_type == "code":
        code = block.strip("```").strip()
        return ParentNode(
            "pre",
            [LeafNode("code", code)]
        )

    if block_type == "ulist":
        items = []
        for line in block.split("\n"):
            text = line[2:]
            children = [
                text_node_to_html_node(n)
                for n in text_to_children(text)
            ]
            items.append(ParentNode("li", children))
        return ParentNode("ul", items)

    if block_type == "olist":
        items = []
        for line in block.split("\n"):
            text = line.split(". ", 1)[1]
            children = [
                text_node_to_html_node(n)
                for n in text_to_children(text)
            ]
            items.append(ParentNode("li", children))
        return ParentNode("ol", items)

    raise Exception("Unknown block type")
