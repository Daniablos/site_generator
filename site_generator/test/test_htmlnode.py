import unittest

from site_generator import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://localhost:8888"},
        )
        node2 = HTMLNode(props={"class": "greeting", "href": "https://localhost:8888"})
        node3 = HTMLNode()
        node4 = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' class="greeting" href="https://localhost:8888"')
        self.assertEqual(node.props_to_html(), node2.props_to_html())
        self.assertNotEqual(node.props_to_html(), node3.props_to_html())
        self.assertNotEqual(node.props_to_html(), node4.props_to_html())

    def test_values(self):
        node = HTMLNode(
            "div",
            "hello world",
            [HTMLNode(), HTMLNode(value="text")],
            {"class": "greeting"}
        )
        node2 = HTMLNode(
            "div",
            "hello world",
            [HTMLNode(), HTMLNode(value="text")],
            {"class": "greeting"}
        )
        node3 = HTMLNode()
        node4 = HTMLNode(props={"href": "https://www.google.com"})
        node5 = HTMLNode()
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertEqual(node3, node5)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        node1 = HTMLNode(
            "p",
            "What a strange world"
        )

        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )
        self.assertNotEqual(node.__repr__, node1.__repr__)