from __future__ import annotations  # noqa: F404

from enum import Enum


class TextType(Enum):
    """
    Enumeration that provides a type-safe and highly readable way to categorize
    different forms or styles of text content, essential for applications dealing
    with rich text or content processing.
    """

    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    """
    Data structure for breaking down and representing rich text content into discrete,
    typed pieces, making it easier to process, transform, and render.        
    """

    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: TextNode) -> bool:
        return (
            self.text_type == value.text_type
            and self.text == value.text
            and self.url == value.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
