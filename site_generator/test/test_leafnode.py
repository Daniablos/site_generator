import pytest
from site_generator import LeafNode


def test_to_html():
    node = LeafNode("p", "Hello world")
    node2 = LeafNode("p", "Hello world", {"href": "https://www.google.com"})
    node3 = LeafNode(None, "Hello world")
    node4 = LeafNode(None, None)

    assert node.to_html() == "<p>Hello world</p>"
    assert node2.to_html() == '<p href="https://www.google.com">Hello world</p>'
    assert node3.to_html() == "Hello world"
    
    
    
    with pytest.raises(ValueError) as exit_info:
        node4.to_html() 
    assert "All leaf nodes must have a value!" in str(exit_info.value)