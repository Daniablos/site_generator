from __future__ import annotations


class HTMLNode:
    """
    Represent a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents).
    It can be block level or inline, and is designed to only output HTML.
    """
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list[HTMLNode] = None,
        props: dict[str: str] = None,
    ):
        self.tag = tag
        """A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)"""
        self.value = value
        """A string representing the value of the HTML tag (e.g. the text inside a paragraph)"""
        self.children = children
        """A list of HTMLNode objects representing the children of this node"""
        self.props = props
        """A dictionary of key-value pairs representing the attributes of the HTML tag."""

    def to_html(self):
        raise NotImplementedError("")

    def props_to_html(self) -> str:
        """
        Converts the props dictionary into a single string suitable for inclusion as HTML attributes within an opening tag.
        """
        if not self.props:
            return ""
        html_attributes = []
        #For each pair, it formats them into a string like key="value".
        for key, value in self.props.items():
            html_attributes.append(f'{key}="{value}"')
        #It then joins all these attribute strings with a space, and prefixes the entire result with an additional space.
        return " " + " ".join(html_attributes)

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, value: HTMLNode) -> bool:
        return (
            self.tag == value.tag
            and self.value == value.value
            and self.children == value.children
            and self.props == value.props
        )
