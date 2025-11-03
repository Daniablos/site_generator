from..nodes import LeafNode
from . import text_to_textnode

def text_to_children(text: str) -> list[LeafNode]:
    """
    Функция для трансформации текста в строку, а затем в лист из LeafNode
    """
    children = []
    if text:
        lines = text.split("\n")
        new_text = " ".join(lines)
        text_nodes = text_to_textnode(new_text)
        for node in text_nodes:
            children.append(node.to_html_node())
        return children