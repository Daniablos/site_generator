from __future__ import annotations

from .leafnode import LeafNode

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

    def to_html_node(self) -> LeafNode:
        """
        This method is responsible for transforming a TextNode object into its
        corresponding HTML representation as a LeafNode. It acts as a dispatcher,
        using Python's match statement (structural pattern matching) to determine
        the appropriate LeafNode based on the TextNode's text_type attribute.
        """
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.LINK:
                if not self.url:
                    raise ValueError("URL is required for link text type but was None.")
                return LeafNode("a", self.text, {"href": self.url})
            case TextType.IMAGE:
                if not self.url:
                    raise ValueError(
                        "URL is required for image text type but was None."
                    )
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
            case _:
                raise ValueError("Unknown text type")

    def __eq__(self, value: TextNode) -> bool:
        return (
            self.text_type == value.text_type
            and self.text == value.text
            and self.url == value.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
