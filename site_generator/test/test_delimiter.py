import pytest
from site_generator import TextNode, TextType, nodes_delimiter

def test_codetype():
    node = TextNode("text `code` text", TextType.TEXT)
    nodes = nodes_delimiter([node], "`", TextType.CODE)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" text", TextType.TEXT)
    ]

    node = TextNode("`code` text", TextType.TEXT)
    nodes = nodes_delimiter([node], "`", TextType.CODE)
    assert nodes == [
        TextNode("code", TextType.CODE),
        TextNode(" text", TextType.TEXT)
    ]

    node = TextNode("`code``code`", TextType.TEXT)
    nodes = nodes_delimiter([node], "`", TextType.CODE)
    assert nodes == [
        TextNode("code", TextType.CODE),
        TextNode("code", TextType.CODE)
    ]

    node = TextNode("text `italic`` text", TextType.TEXT)
    with pytest.raises(ValueError) as exit_info:
        nodes = nodes_delimiter([node], "`", TextType.CODE)
    assert "Invalid markdown syntax: unmatched delimiter '`' found in text: 'text `italic`` text'" == str(exit_info.value)


def test_text():
    node = TextNode("text text", TextType.TEXT)
    nodes = nodes_delimiter([node], "**", TextType.BOLD)
    assert nodes == [TextNode("text text", TextType.TEXT)]

def test_bold():
    node = TextNode("text **bold** text", TextType.TEXT)
    nodes = nodes_delimiter([node], "**", TextType.BOLD)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text", TextType.TEXT)
        ]
    
    node = TextNode("text **bold*** text", TextType.TEXT)
    nodes = nodes_delimiter([node], "**", TextType.BOLD)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode("* text", TextType.TEXT)
        ]

    node = TextNode("text ***bold*** text", TextType.TEXT)
    nodes = nodes_delimiter([node], "**", TextType.BOLD)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("*bold", TextType.BOLD),
        TextNode("* text", TextType.TEXT)
        ]
    
    node = TextNode("text **italic**** text", TextType.TEXT)
    with pytest.raises(ValueError) as exit_info:
        nodes = nodes_delimiter([node], "**", TextType.BOLD)
    assert "Invalid markdown syntax: unmatched delimiter '**' found in text: 'text **italic**** text'" == str(exit_info.value)

    
def test_italic():
    node = TextNode("text _italic_ text", TextType.TEXT)
    nodes = nodes_delimiter([node], "_", TextType.ITALIC)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" text", TextType.TEXT)
        ]
    
    node = TextNode("text __italic__ text", TextType.TEXT)
    nodes = nodes_delimiter([node], "_", TextType.ITALIC)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("italic", TextType.TEXT),
        TextNode(" text", TextType.TEXT)
        ]

    node = TextNode("text _italic___ text", TextType.TEXT)
    nodes = nodes_delimiter([node], "_", TextType.ITALIC)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" text", TextType.TEXT)
        ]
    
    node = TextNode("text _italic__ text", TextType.TEXT)
    with pytest.raises(ValueError) as exit_info:
        nodes = nodes_delimiter([node], "_", TextType.ITALIC)
    assert "Invalid markdown syntax: unmatched delimiter '_' found in text: 'text _italic__ text'" == str(exit_info.value)
    

def test_multiple():
    node = TextNode("text **bold** text _italic_ `code`text", TextType.TEXT)
    nodes = nodes_delimiter(nodes_delimiter(nodes_delimiter([node], "`", TextType.CODE), "**", TextType.BOLD), "_", TextType.ITALIC)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode("text", TextType.TEXT)
    ]

    



