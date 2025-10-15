import unittest
import pytest

from site_generator import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = TextNode("print('hello world')", TextType.CODE)
        node1 = TextNode("print('hello world')", TextType.CODE)
        self.assertEqual(node, node1)

    def test_neq_type(self):
        node = TextNode("print('hello world')", TextType.CODE)
        node1 = TextNode("print('hello world')", TextType.TEXT)
        self.assertNotEqual(node, node1)

    def test_not_eq_text(self):
        node = TextNode("print(hello world)", TextType.CODE)
        node1 = TextNode("print('hello world')", TextType.CODE)
        self.assertNotEqual(node, node1)

    def test_eq_url_none(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_neq_url_nNone(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.ru")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_eq_empty_string(self):
        node = TextNode("", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_empty_string_with_url(self):
        node = TextNode("", TextType.LINK, "https://empty.com")
        node2 = TextNode("", TextType.LINK, "https://empty.com")
        self.assertEqual(node, node2)


def test_image():
    node = TextNode("image", TextType.IMAGE, "url/path")
    html_node = node.to_html_node()
    assert html_node.to_html() == '<img src="url/path" alt="image">'

    node2 = TextNode("", TextType.IMAGE, "url/path")
    html_node2 = node2.to_html_node()
    assert html_node2.to_html() == '<img src="url/path" alt="">'

    node3 = TextNode("image", TextType.IMAGE)
    with pytest.raises(ValueError) as exit_info:
        node3.to_html_node()
    assert "URL is required for image text type but was None." == str(exit_info.value)


def test_text():
    node = TextNode("text txt", TextType.TEXT)
    html_node = node.to_html_node()
    assert html_node.to_html() == "text txt"

    node2 = TextNode("text", TextType.TEXT, "url/local")
    html_node2 = node2.to_html_node()
    assert html_node2.to_html() == "text"

    node3 = TextNode("", TextType.TEXT)
    html_node3 = node3.to_html_node()
    with pytest.raises(ValueError) as exit_info:
        html_node3.to_html()
    assert "All leaf nodes must have a value!" == str(exit_info.value)


def test_bold():
    node = TextNode("bold", TextType.BOLD, "url")
    html_node = node.to_html_node()
    assert html_node.to_html() == "<b>bold</b>"

    node2 = TextNode("bold", TextType.BOLD)
    html_node2 = node2.to_html_node()
    assert html_node2.to_html() == "<b>bold</b>"


def test_italic():
    node = TextNode("italic", TextType.ITALIC)
    html_node = node.to_html_node()
    assert html_node.to_html() == "<i>italic</i>"

    node2 = TextNode("italic", TextType.ITALIC, "url")
    html_node2 = node2.to_html_node()
    assert html_node2.to_html() == "<i>italic</i>"


def test_code():
    node = TextNode("code", TextType.CODE)
    html_node = node.to_html_node()
    assert html_node.to_html() == "<code>code</code>"

    node = TextNode("code", TextType.CODE, "url")
    html_node = node.to_html_node()
    assert html_node.to_html() == "<code>code</code>"


def test_link():
    node = TextNode("link", TextType.LINK, "url/path")
    html_node = node.to_html_node()
    assert html_node.to_html() == '<a href="url/path">link</a>'

    node2 = TextNode("", TextType.LINK, "url/path")
    html_node2 = node2.to_html_node()
    with pytest.raises(ValueError) as exit_info:
        html_node2.to_html()
    assert "All leaf nodes must have a value!" == str(exit_info.value)

    node3 = TextNode("link", TextType.LINK)
    with pytest.raises(ValueError) as exit_info:
        node3.to_html_node()
    assert "URL is required for link text type but was None." == str(exit_info.value)


def test_no_type():
    node = TextNode("something", "text")
    with pytest.raises(ValueError) as exit_info:
        node.to_html_node()
    assert "Unknown text type" == str(exit_info.value)


if __name__ == "__main__":
    unittest.main()
