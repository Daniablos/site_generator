from __future__ import annotations

class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list[HTMLNode] = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("")
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        html_attributes = []
        for key, value in self.props.items():
            html_attributes.append(f'{key}="{value}"')
        return " " + " ".join(html_attributes)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, value: HTMLNode):
        return(
            self.tag == value.tag
            and self.value == value.value
            and self.children == value.children
            and self.props == value.props
        )
    
