from enum import Enum

class BlockType(Enum):
    """
    Типизация блоков в формате Markdown
    """

    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    HEADING4 = "heading4"
    HEADING5 = "heading5"
    HEADING6 = "heading6"

    PARAGRAPH = "paragraph"
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
            if char != "#":
                break
            num_hashes += 1
        if 1 <= num_hashes <= 6:
            if len(block) > num_hashes and block[num_hashes] == " ":
                match num_hashes:
                    case 1:
                        return BlockType.HEADING1
                    case 2:
                        return BlockType.HEADING2
                    case 3:
                        return BlockType.HEADING3
                    case 4:
                        return BlockType.HEADING4
                    case 5:
                        return BlockType.HEADING5
                    case 6:
                        return BlockType.HEADING6
    
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

