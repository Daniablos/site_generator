from ..nodes import TextType, TextNode
from .extract_links import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    """
    This function processes a list of TextNode objects, identifying and re-typing text segments based on a specified delimiter.
    It's designed to parse simple inline formatting, similar to how markdown handles **bold**, `code` or _italic_.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            splited_text = node.text.split(delimiter)
            if not len(splited_text) % 2:
                raise ValueError(
                    f"Invalid markdown syntax: unmatched delimiter '{delimiter}' found in text: '{node.text}'"
                )
            for i in range(len(splited_text)):
                if splited_text[i]:
                    if not i % 2:
                        new_nodes.append(TextNode(splited_text[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(splited_text[i], text_type))
        else:
            new_nodes.append(node)
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    This function processes a list of TextNode objects, recursively identifying and
      converting Markdown-formatted images within TextType.TEXT nodes 
      into distinct TextNode objects of TextType.IMAGE
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            images = extract_markdown_images(node.text)
            if not images:
                new_nodes.append(node)
                continue
            img = images[0]
            splited_text = node.text.split(f"![{img[0]}]({img[1]})", 1)
            if splited_text[0]:
                new_nodes.append(TextNode(splited_text[0], TextType.TEXT))
            new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
            if splited_text[1]:
                new_nodes.extend(
                    split_nodes_image([TextNode(splited_text[1], TextType.TEXT)])
                )
        else:
            new_nodes.append(node)

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    This function processes a list of TextNode objects, recursively identifying 
    and converting Markdown-formatted links within TextType.TEXT nodes into 
    distinct TextNode objects of TextType.LINK.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links = extract_markdown_links(node.text)
            if not links:
                new_nodes.append(node)
                continue
            link = links[0]
            splited_text = node.text.split(f"[{link[0]}]({link[1]})", 1)
            if splited_text[0]:
                new_nodes.append(TextNode(splited_text[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if splited_text[1]:
                new_nodes.extend(
                    split_nodes_link([TextNode(splited_text[1], TextType.TEXT)])
                )
        else:
            new_nodes.append(node)
    return new_nodes
