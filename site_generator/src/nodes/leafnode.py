from .htmlnode import HTMLNode


class LeafNode(HTMLNode):
    """
    The LeafNode class is a specialized child class of HTMLNode.
    It represents a fundamental type of HTML element that contains
    only text content (value) and cannot have any child nodes.
    It's designed for rendering simple HTML tags (like p, a, span) or
    even raw text directly into the HTML output.
    """

    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        """
        This method is the concrete implementation of how a LeafNode
        renders itself into an HTML string. Unlike the base HTMLNode,
        which raises NotImplementedError, LeafNode provides the actual HTML generation logic.
        """
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        if not self.value:
            if self.tag != "code":
                raise ValueError("All leaf nodes must have a value!")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
