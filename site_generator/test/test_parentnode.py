import pytest

from site_generator import ParentNode, LeafNode

def test_to_html_with_children():
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() == "<div><span>child</span></div>"

def test_to_html_with_grandchildren():
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() == "<div><span><b>grandchild</b></span></div>"

def test_to_html_with_multi_grandchildren():
    grand = LeafNode("b", "grandchild")
    grand2 = LeafNode("i", "italic grandchild")
    grand3 = LeafNode("b", "link", {"href": "https://www.google.com"})
    grand4 = LeafNode(None, "plain text")
    child = ParentNode("div", [grand, grand2, grand3, grand4], {"href": "http://localhost:8888"})
    child2 = LeafNode("mark", "MARK")
    parent = ParentNode("body", [child, child2])

    assert parent.to_html() == '<body><div href="http://localhost:8888"><b>grandchild</b><i>italic grandchild</i><b href="https://www.google.com">link</b>plain text</div><mark>MARK</mark></body>'

def test_to_html_no_tag():
    child = LeafNode("b", "bold")
    parent = ParentNode(None, [child])

    with pytest.raises(ValueError) as exit_info:
        parent.to_html()

    assert "All parent nodes must have a tag!" in str(exit_info)

def test_to_html_no_child():
    parent = ParentNode("body", None)

    with pytest.raises(ValueError) as exit_info:
        parent.to_html()

    assert "All parent nodes must have a child!" in str(exit_info)

def test_eq():
    child = LeafNode("b", "bold")
    child2 = LeafNode("b", "bold")
    parent = ParentNode("body", [child])
    parent2 = ParentNode("body", [child2])

    assert parent == parent2






    