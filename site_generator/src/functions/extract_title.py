from . import markdown_to_blocks, block_to_block_type, BlockType

def extract_title(markdown: str) -> str:
    """
    Функция возвращает текст из первого попавшегося h1 в MD файле.
    Поднимает ошибку, если h1 отсутствует
    """
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING1:
            return block[2:]
    raise Exception("File doesn't have 'h1' header!")