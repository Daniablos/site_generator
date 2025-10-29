from enum import Enum

class BlockType(Enum):
    """
    Типизация блоков в формате Markdown
    """

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    """
    Функция для определения типа блока.
    Берет блок избавленный от начальных и конечных пробелов и пустых строк и 
    проверяет условия для каждого типа блоков.
    """
    lines = block.split("\n")
    if block.startswith("#"):
        num_hashes = 0
        for char in block:
            if char == "#":
                num_hashes += 1
            else:
                break
        if 1 <= num_hashes <= 6:
            if len(block) > num_hashes and block[num_hashes] == " ":
                return BlockType.HEADING
    
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    is_ordered_list = True
    for i, line in enumerate(lines):
        prefix = f"{i+1}. "
        if not line.startswith(prefix):
            is_ordered_list = False
            break
    
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

