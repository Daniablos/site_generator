from ..nodes import TextType, TextNode

def nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    """
    This function processes a list of TextNode objects, identifying and re-typing text segments based on a specified delimiter.
    It's designed to parse simple inline formatting, similar to how markdown handles **bold**, `code` or _italic_.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            splited_text = node.text.split(delimiter)
            if not len(splited_text) % 2:
                raise ValueError(f"Invalid markdown syntax: unmatched delimiter '{delimiter}' found in text: '{node.text}'")
            for i in range(len(splited_text)):
                if splited_text[i]:
                    if not i % 2:
                        new_nodes.append(TextNode(splited_text[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(splited_text[i], text_type))
        else:
            new_nodes.append(node)
    return new_nodes

