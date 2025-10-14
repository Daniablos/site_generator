from .leafnode import LeafNode
from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    """
    The ParentNode class is a specialized child class of HTMLNode designed to represent HTML elements that contain other HTML nodes as children.
    It's intended for structural HTML elements like div, ul, body, h1, etc., which typically wrap other content rather than holding direct textual value themselves.
    """
    def __init__(self, tag: str, children: list[LeafNode], props: dict[str: str] = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        """
        This method provides the concrete implementation for rendering a ParentNode and all its children into a complete HTML string.
        """
        if not self.tag:
            raise ValueError("All parent nodes must have a tag!")
        if not self.children:
            raise ValueError("All parent nodes must have a child!")
        
        tmp_str = ""
        for child in self.children:
            tmp_str += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{tmp_str}</{self.tag}>"
