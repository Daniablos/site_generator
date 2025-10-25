from site_generator import markdown_to_blocks

def test_md_to_blocks():
    md = """
# Test Document - Various Markdown Blocks

This is the first paragraph. It should be a single block.


This is the second paragraph,
which includes a manual line break.
It should still be treated as one block.

                    a
"""
    blocks = markdown_to_blocks(md)
    assert blocks == [
        "# Test Document - Various Markdown Blocks",
        "This is the first paragraph. It should be a single block.",
        "This is the second paragraph,\nwhich includes a manual line break.\nIt should still be treated as one block.",
        "a"
    ]
