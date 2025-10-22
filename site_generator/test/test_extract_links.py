from site_generator import extract_markdown_images, extract_markdown_links


def test_image():
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
    assert extract_markdown_images(text) == [
        ("rick roll", "https://i.imgur.com/aKaOqIh.gif")
    ]

    text = "This is text with a ![](https://i.imgur.com/aKaOqIh.gif)"
    assert extract_markdown_images(text) == [("", "https://i.imgur.com/aKaOqIh.gif")]

    text = "This is text with a !(https://i.imgur.com/aKaOqIh.gif)"
    assert extract_markdown_images(text) == []

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![not](pentagon)"
    assert extract_markdown_images(text) == [
        ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
        ("not", "pentagon"),
    ]


def test_link():
    text = "This is [link](http://localhost:8888)"
    assert extract_markdown_links(text) == [("link", "http://localhost:8888")]

    text = "This is link(http://localhost:8888)"
    assert extract_markdown_links(text) == []

    text = "This is [link](http://localhost:8888) [too](google.com)"
    assert extract_markdown_links(text) == [
        ("link", "http://localhost:8888"),
        ("too", "google.com"),
    ]
