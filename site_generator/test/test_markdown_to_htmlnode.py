import pytest
from site_generator import markdown_to_htmlnode

def test_paragraphs():
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    node = markdown_to_htmlnode(md)
    html = node.to_html()
    assert html == "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"


def test_codeblock():
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_htmlnode(md)
    html = node.to_html()
    assert html == "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"

@pytest.mark.parametrize(
    "markdown_input, expected_html",
    [
        # --- Параграфы ---
        (
            "This is a paragraph.\nAnother line of text.\n",
            "<div><p>This is a paragraph. Another line of text.</p></div>"
        ),
        (
            "Just a single line paragraph.",
            "<div><p>Just a single line paragraph.</p></div>"
        ),
        (
            "Paragraph with **bold** and _italic_.",
            "<div><p>Paragraph with <b>bold</b> and <i>italic</i>.</p></div>"
        ),
        (
            "paragragh with [url](google.com) and ![image](path)",
            "<div><p>paragragh with <a href=\"google.com\">url</a> and <img src=\"path\" alt=\"image\"></p></div>"
        ),

        # --- Заголовки ---
        (
            "# Heading 1",
            "<div><h1>Heading 1</h1></div>"
        ),
        (
            "### Heading 3",
            "<div><h3>Heading 3</h3></div>"
        ),
        (
            "###### Heading 6",
            "<div><h6>Heading 6</h6></div>"
        ),
        (
            "#No space after hash", 
            "<div><p>#No space after hash</p></div>"
        ),

        # --- Блоки кода ---
        (
            "```python\nprint('Hello')\n```",
            "<div><pre><code class=\"language-python\">print('Hello')\n</code></pre></div>"
        ),
        (
            "```\nconsole.log('No lang')\n```",
            "<div><pre><code>console.log('No lang')\n</code></pre></div>"
        ),
        (
            "```java\npublic static void main(){}\n\n// Multi-line code\n```",
            "<div><pre><code class=\"language-java\">public static void main(){}\n\n// Multi-line code\n</code></pre></div>"
        ),
        (
            "```\n```", 
            "<div><pre><code></code></pre></div>"
        ),
         (
            "```python\n```", 
            "<div><pre><code class=\"language-python\"></code></pre></div>"
        ),

        # --- Цитаты ---
        (
            ">This is a quote.\n>Second line of quote.",
            "<div><blockquote><p>This is a quote. Second line of quote.</p></blockquote></div>" 
        ),
        (
            ">A single-line quote.",
            "<div><blockquote><p>A single-line quote.</p></blockquote></div>"
        ),

        # --- Неупорядоченные списки ---
        (
            "- Item 1\n- Item 2",
            "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        ),

        # --- Упорядоченные списки ---
        (
            "1. First item\n2. Second item",
            "<div><ol><li>First item</li><li>Second item</li></ol></div>"
        ),
        (
            "10. Ten item\n11. Eleven item",
            "<div><p>10. Ten item 11. Eleven item</p></div>"
        ),

        # --- Комбинированный сценарий ---
        (
            "# Главный заголовок\n\nThis is a paragraph.\n\n```python\nprint(1)\n```",
            "<div><h1>Главный заголовок</h1><p>This is a paragraph.</p><pre><code class=\"language-python\">print(1)\n</code></pre></div>"
        ),
    ]
)
def test_markdown_to_htmlnode(markdown_input, expected_html):
    node = markdown_to_htmlnode(markdown_input)
    assert node.to_html() == expected_html
    


