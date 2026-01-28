from src.textnode import TextNode, TextType
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only split Text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        # Split the text by delimiter
        parts = node.text.split(delimiter)

        # If even number of parts, we have unbalanced delimiters
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax for delimiter: {delimiter}")

        # Build nodes
        for i, part in enumerate(parts):
            if part == "":
                continue

            if i % 2 == 0:
                # Outside delimiter → plain text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Inside delimiter → styled text
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

         
         
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    delimiters = [
        ("`", TextType.CODE),
        ("**", TextType.BOLD),
        ("*", TextType.ITALIC),
    ]

    for delimiter, text_type in delimiters:
        new_nodes = []

        for node in nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue

            split_nodes = split_nodes_delimiter(
                node.text, delimiter, text_type
            )
            new_nodes.extend(split_nodes)

        nodes = new_nodes

    return nodes
node = TextNode("This is text with a `code block` word", TextType.TEXT)
result = split_nodes_delimiter([node], "`", TextType.CODE)

for n in result:
    print(n)