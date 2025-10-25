from .split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from ..nodes import TextType, TextNode


def text_to_textnode(text: str) -> list[TextNode]:
    """
    This function serves as the primary parser for converting a raw Markdown-formatted string
    into a structured list of TextNode objects. It orchestrates a series of
    specialized split_nodes functions to identify and extract various inline Markdown elements,
    transforming them from plain TextType.TEXT into their corresponding rich text TextNode types (images, links, code, bold, italic).
    """
    return split_nodes_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        [TextNode(text, TextType.TEXT)], "`", TextType.CODE
                    ),
                    "**",
                    TextType.BOLD,
                ),
                "_",
                TextType.ITALIC,
            )
        )
    )
