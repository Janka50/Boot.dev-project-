def extract_title(markdown: str) -> str:
    """
    Extracts the first H1 heading from markdown.
    Raises ValueError if no H1 heading is found.
    """
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):  # H1 header
            return line[2:].strip()  # remove '# ' and strip whitespace
    raise ValueError("No H1 header found in markdown")
