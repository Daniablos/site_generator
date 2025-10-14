import unittest

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





if __name__ == "__main__":
    unittest.main()