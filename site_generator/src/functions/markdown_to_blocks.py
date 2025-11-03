def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Splits a Markdown string into a list of cleaned, non-empty text blocks.

    Blocks are primarily determined by two consecutive newline characters.
    Each resulting block is stripped of leading/trailing whitespace, and any
    blocks that become empty after stripping are discarded.
    """

    blocks = []
    lines = markdown.split("\n")
    inside_code_block = False
    current_block = []

    for line in lines:
        #Блок кода
        if line.startswith("```"): 
            current_block.append(line)
            if inside_code_block:
                blocks.append("\n".join(current_block))
                current_block = []
                inside_code_block = False
            else:
                inside_code_block = True
        elif inside_code_block:
            current_block.append(line)
        #Деление между блоками
        elif line.strip() == "": 
            if current_block:
                blocks.append("\n".join(current_block).strip())
                current_block = []
        else:
            current_block.append(line)
    #Добавление последнего блока
    if current_block:
        blocks.append("\n".join(current_block).strip())
    return blocks
        