from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    print(TextNode("some test text", TextType.LINK, "https://www.google.com"))
    node = HTMLNode(props={"href": "https://www.google.com"})
    print(node.props_to_html())


if __name__ == "__main__":
    main()