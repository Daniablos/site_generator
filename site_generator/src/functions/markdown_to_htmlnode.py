from ..nodes import ParentNode
from . import markdown_to_blocks, block_to_block_type, BlockType
from .text_to_children import text_to_children
from .block_to_node import (
    code_block_to_node,
    quote_block_to_node,
    ul_block_to_node,
    ol_block_to_node,
)


def markdown_to_htmlnode(markdown: str) -> ParentNode:
    """
    Функция для преобразования MarkDown файла в единый ParentNode
    с другими HTMLNode в качестве 'детей'.
    """
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case BlockType.HEADING1:
                text = block[2:]
                node = ParentNode("h1", text_to_children(text))
            case BlockType.HEADING2:
                text = block[3:]
                node = ParentNode("h2", text_to_children(text))
            case BlockType.HEADING3:
                text = block[4:]
                node = ParentNode("h3", text_to_children(text))
            case BlockType.HEADING4:
                text = block[5:]
                node = ParentNode("h4", text_to_children(text))
            case BlockType.HEADING5:
                text = block[6:]
                node = ParentNode("h5", text_to_children(text))
            case BlockType.HEADING6:
                text = block[7:]
                node = ParentNode("h6", text_to_children(text))
            case BlockType.PARAGRAPH:
                text = block
                node = ParentNode("p", text_to_children(text))
            case BlockType.CODE:
                node = code_block_to_node(block)
            case BlockType.QUOTE:
                node = quote_block_to_node(block)
            case BlockType.UNORDERED_LIST:
                node = ul_block_to_node(block)
            case BlockType.ORDERED_LIST:
                node = ol_block_to_node(block)
        nodes.append(node)
    return ParentNode("div", nodes)
