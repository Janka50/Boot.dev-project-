def markdown_to_html_node(markdown: str):
    markdown = markdown.strip()
    from src.htmlnode import ParentNode, LeafNode
    from src.markdownBlocks import markdown_to_blocks
    from src.block_type import block_to_block_type, BlockType
    from src.text_to_Nodes import text_to_children, text_node_to_html_node
    
    blocks = markdown_to_blocks(markdown)
    children_nodes = []
    for block in blocks:
        block = block.strip()   # ✅ CRITICAL
        block_type = block_to_block_type(block)
        print("DETECTED TYPE:", block_type, "FOR:", repr(block))


        if block_type == BlockType.PARAGRAPH:
            inline_nodes = text_to_children(block)
            p_node = ParentNode(
                "p",
                [text_node_to_html_node(n) for n in inline_nodes]
            )
            children_nodes.append(p_node)

        elif block_type == BlockType.HEADING:
            first_line = block.split("\n")[0]
            level = len(first_line) - len(first_line.lstrip("#"))
            text = first_line[level + 1 :]

            inline_nodes = text_to_children(text)
            h_node = ParentNode(
              f"h{level}",
              [text_node_to_html_node(n) for n in inline_nodes]
               )
            children_nodes.append(h_node)

        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            code_text = "\n".join(lines[1:-1])
            code_node = ParentNode(
                "pre",
                [ParentNode("code", [LeafNode(None, code_text)])]
            )
            children_nodes.append(code_node)

        elif block_type == BlockType.QUOTE:
            lines = [line[2:] for line in block.split("\n")]
            inline_nodes = text_to_children("\n".join(lines))
            p_node = ParentNode(
                "p",
                [text_node_to_html_node(n) for n in inline_nodes]
            )
            quote_node = ParentNode("blockquote", [p_node])
            children_nodes.append(quote_node)

        elif block_type == BlockType.UNORDERED_LIST:
            li_nodes = []
            for line in block.split("\n"):
                text = line[2:]
                inline_nodes = text_to_children(text)
                li_nodes.append(
                    ParentNode(
                        "li",
                        [text_node_to_html_node(n) for n in inline_nodes]
                    )
                )
            children_nodes.append(ParentNode("ul", li_nodes))

        elif block_type == BlockType.ORDERED_LIST:
            li_nodes = []
            for line in block.split("\n"):
                _, text = line.split(". ", 1)
                inline_nodes = text_to_children(text)
                li_nodes.append(
                    ParentNode(
                        "li",
                        [text_node_to_html_node(n) for n in inline_nodes]
                    )
                )
            children_nodes.append(ParentNode("ol", li_nodes))

    return ParentNode("div", children_nodes)
