import pytest
from site_generator import TextNode, TextType, split_nodes_delimiter, split_nodes_image, split_nodes_link

def test_codetype():
    node = TextNode("text `code` text", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" text", TextType.TEXT)
    ]

    node = TextNode("`code` text", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    assert nodes == [
        TextNode("code", TextType.CODE),
        TextNode(" text", TextType.TEXT)
    ]

    node = TextNode("`code``code`", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    assert nodes == [
        TextNode("code", TextType.CODE),
        TextNode("code", TextType.CODE)
    ]

    node = TextNode("text `italic`` text", TextType.TEXT)
    with pytest.raises(ValueError) as exit_info:
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    assert "Invalid markdown syntax: unmatched delimiter '`' found in text: 'text `italic`` text'" == str(exit_info.value)


def test_text():
    node = TextNode("text text", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    assert nodes == [TextNode("text text", TextType.TEXT)]

def test_bold():
    node = TextNode("text **bold** text", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text", TextType.TEXT)
        ]
    
    node = TextNode("text **bold*** text", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode("* text", TextType.TEXT)
        ]

    node = TextNode("text ***bold*** text", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("*bold", TextType.BOLD),
        TextNode("* text", TextType.TEXT)
        ]
    
    node = TextNode("text **italic**** text", TextType.TEXT)
    with pytest.raises(ValueError) as exit_info:
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    assert "Invalid markdown syntax: unmatched delimiter '**' found in text: 'text **italic**** text'" == str(exit_info.value)

    
def test_italic():
    node = TextNode("text _italic_ text", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" text", TextType.TEXT)
        ]
    
    node = TextNode("text __italic__ text", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("italic", TextType.TEXT),
        TextNode(" text", TextType.TEXT)
        ]

    node = TextNode("text _italic___ text", TextType.TEXT)
    nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" text", TextType.TEXT)
        ]
    
    node = TextNode("text _italic__ text", TextType.TEXT)
    with pytest.raises(ValueError) as exit_info:
        nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    assert "Invalid markdown syntax: unmatched delimiter '_' found in text: 'text _italic__ text'" == str(exit_info.value)

def test_image():
    node = TextNode("text ![alt](img) text", TextType.TEXT)
    nodes = split_nodes_image([node])
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("alt", TextType.IMAGE, "img"),
        TextNode(" text", TextType.TEXT)
    ]
    
    node = TextNode("text [alt](img) text", TextType.TEXT)
    nodes = split_nodes_image([node])
    assert nodes == [
        TextNode("text [alt](img) text", TextType.TEXT)
    ]

    node = TextNode("text ![](img) text", TextType.TEXT)
    nodes = split_nodes_image([node])
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("", TextType.IMAGE, "img"),
        TextNode(" text", TextType.TEXT)
    ]

    node = TextNode("text ![alt]() text", TextType.TEXT)
    nodes = split_nodes_image([node])
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("alt", TextType.IMAGE, ""),
        TextNode(" text", TextType.TEXT)
    ]

    node = TextNode("text ![alt]()", TextType.TEXT)
    nodes = split_nodes_image([node])
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("alt", TextType.IMAGE, ""),
    ]

    node = TextNode("![alt]()", TextType.TEXT)
    nodes = split_nodes_image([node])
    assert nodes == [
        TextNode("alt", TextType.IMAGE, "")
    ]

    node = TextNode("![]() ![alt](url)", TextType.TEXT)
    nodes = split_nodes_image([node])
    assert nodes == [
        TextNode("", TextType.IMAGE, ""),
        TextNode(" ", TextType.TEXT),
        TextNode("alt", TextType.IMAGE, "url")
    ]




def test_link():
    node = TextNode("text [link](url) text", TextType.TEXT)
    nodes = split_nodes_link([node])
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("link", TextType.LINK, "url"),
        TextNode(" text", TextType.TEXT)
    ]

    node = TextNode("text ![link](url) text", TextType.TEXT)
    nodes = split_nodes_link([node])
    assert nodes == [
        TextNode("text ![link](url) text", TextType.TEXT)
    ]

    node = TextNode("text [](url) text", TextType.TEXT)
    nodes = split_nodes_link([node])
    assert nodes == [
        TextNode("text ", TextType.TEXT),
        TextNode("", TextType.LINK, "url"),
        TextNode(" text", TextType.TEXT)
    ]

    node = TextNode("[link](url)", TextType.TEXT)
    nodes = split_nodes_link([node])
    assert nodes == [
        TextNode("link", TextType.LINK, "url")
    ]

    node = TextNode("[]()", TextType.TEXT)
    nodes = split_nodes_link([node])
    assert nodes == [
        TextNode("", TextType.LINK, "")
    ]

    node = TextNode("[link](url)", TextType.TEXT)
    nodes = split_nodes_link([node])
    assert nodes == [
        TextNode("link", TextType.LINK, "url")
    ]

    node = TextNode("[]()[link](url)", TextType.TEXT)
    nodes = split_nodes_link([node])
    assert nodes == [
        TextNode("", TextType.LINK, ""),
        TextNode("link", TextType.LINK, "url")
    ]


    

def test_multiple():
    node = TextNode("![alt text](img url) text [link text](url) **bold** text _italic_ `code`text![img](url)", TextType.TEXT)
    nodes = split_nodes_link(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([node], "`", TextType.CODE), "**", TextType.BOLD), "_", TextType.ITALIC)))
    assert nodes == [
        TextNode("alt text", TextType.IMAGE, "img url"),
        TextNode(" text ", TextType.TEXT),
        TextNode("link text", TextType.LINK, "url"),
        TextNode(" ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode("text", TextType.TEXT),
        TextNode("img", TextType.IMAGE, "url")
    ]





