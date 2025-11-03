from ..nodes import ParentNode, LeafNode
from .text_to_children import text_to_children


def code_block_to_node(block: str) -> ParentNode:
    """
    Функция для преобразования блока с кодом в ParentNode
    c информацией о языку, если она предоставлена
    """
    stripped_block = block[3:-3]
    lines = stripped_block.split("\n")
    text = "\n".join(lines[1:])
    code_info = {}
    if lines[0]:
        code_info = {"class": f"language-{lines[0]}"}
    code_node = [LeafNode("code", text, code_info)]
    return ParentNode("pre", code_node)


def quote_block_to_node(block: str) -> ParentNode:
    """
    Функция для преобразования блока с цитатой в ParentNode
    """
    stripped_lines = []
    lines = block.split("\n")
    for line in lines:
        stripped_lines.append(line[1:])
    text = "\n".join(stripped_lines)
    return ParentNode("blockquote", [ParentNode("p", text_to_children(text))])


def ul_block_to_node(block: str) -> ParentNode:
    """
    Функция для преобразования блока с неупорядоченным списком в ParentNode
    """
    children = []
    lines = block.split("\n")
    for line in lines:
        children.append(ParentNode("li", text_to_children(line[2:])))
    return ParentNode("ul", children)


def ol_block_to_node(block: str) -> ParentNode:
    """
    Функция для преобразования блока с упорядоченным списком в ParentNode
    """
    children = []
    lines = block.split("\n")
    for line in lines:
        text = line.split(" ", 1)[1]
        children.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", children)
