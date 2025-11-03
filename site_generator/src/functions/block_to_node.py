from ..nodes import ParentNode, LeafNode
from .text_to_children import text_to_children


def code_block_to_node(block: str) -> ParentNode:
    """
    Функция для преобразования блока с кодом в ParentNode
    c информацией о языке, если она предоставлена
    """
    code_tag_len = 3
    stripped_block = block[code_tag_len:-code_tag_len]
    lines = stripped_block.split("\n")
    heading_line = lines[0]
    code_lines = lines[1:]
    code_text = "\n".join(code_lines)
    code_info = {}
    if heading_line:
        code_info = {"class": f"language-{heading_line}"}
    code_node = LeafNode("code", code_text, code_info)
    return ParentNode("pre", [code_node])


def quote_block_to_node(block: str) -> ParentNode:
    """
    Функция для преобразования блока с цитатой в ParentNode
    """
    stripped_lines = []
    lines = block.split("\n")
    quote_tag_len = 1
    for line in lines:
        stripped_lines.append(line[quote_tag_len:])
    text = "\n".join(stripped_lines)
    return ParentNode("blockquote", [ParentNode("p", text_to_children(text))])


def ul_block_to_node(block: str) -> ParentNode:
    """
    Функция для преобразования блока с неупорядоченным списком в ParentNode
    """
    children = []
    list_tag_len = 2
    lines = block.split("\n")
    for line in lines:
        children.append(ParentNode("li", text_to_children(line[list_tag_len:])))
    return ParentNode("ul", children)


def ol_block_to_node(block: str) -> ParentNode:
    """
    Функция для преобразования блока с упорядоченным списком в ParentNode
    """
    children = []
    lines = block.split("\n")
    for line in lines:
        text = line.split(" ", 1)[1] #Берется линия без тэга листа
        children.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", children)
