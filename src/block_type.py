from src.BlockTypeI import BlockType 

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith("#"):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(
        line.split(".")[0].isdigit() and line.split(".")[1].startswith(" ")
        for line in lines
    ):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH