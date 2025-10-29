from site_generator import BlockType, block_to_block_type

def test_paragraph():
    block = """- yes
1. This is paragraph
This is paragraph
2. paragraph"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH

def test_heading():
    block = "#"
    assert block_to_block_type(block) == BlockType.PARAGRAPH

    block = "##123"
    assert block_to_block_type(block) == BlockType.PARAGRAPH

    block = "# h1"
    assert block_to_block_type(block) == BlockType.HEADING

    block = "## h2"
    assert block_to_block_type(block) == BlockType.HEADING

    block = "### h3"
    assert block_to_block_type(block) == BlockType.HEADING

    block = "#### h4"
    assert block_to_block_type(block) == BlockType.HEADING

    block = "##### h5"
    assert block_to_block_type(block) == BlockType.HEADING

    block = "###### h6"
    assert block_to_block_type(block) == BlockType.HEADING

    block = "####### h7"
    assert block_to_block_type(block) == BlockType.PARAGRAPH

def test_code():
    block = """```python
Hello world
```"""
    assert block_to_block_type(block) == BlockType.CODE

    block = """``python
Hello world
```"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH

    block = """```python
Hello world```"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH

def test_quote():
    block = """>Some quote
>here too
>same"""
    assert block_to_block_type(block) == BlockType.QUOTE

    block = """>Some quote
here too
>same"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH

    block = """>>Some quote
>here too
>same"""
    assert block_to_block_type(block) == BlockType.QUOTE

    block = """>>Some quote
>here too
same"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH

def test_unordered_list():
    block = """- 1
- 2
- 3"""
    assert block_to_block_type(block) == BlockType.UNORDERED_LIST

    block = """-1
- 2
- 3"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH

    block = """- 1
- 2
3"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH

    block = """- 1"""
    assert block_to_block_type(block) == BlockType.UNORDERED_LIST

def test_ordered_list():
    block = """1. 1
2. 2
3. 3"""
    assert block_to_block_type(block) == BlockType.ORDERED_LIST

    block = """1.1
2. 2
3. 3"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH

    block = """2. 2
3. 3"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH

    block = """1. 1
3. 2
3. 3"""
    assert block_to_block_type(block) == BlockType.PARAGRAPH
    




