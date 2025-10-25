def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Splits a Markdown string into a list of cleaned, non-empty text blocks.

    Blocks are primarily determined by two consecutive newline characters.
    Each resulting block is stripped of leading/trailing whitespace, and any
    blocks that become empty after stripping are discarded.
    """
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block:
            stripped_blocks.append(stripped_block)
    return stripped_blocks
