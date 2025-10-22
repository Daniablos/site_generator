import re


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """
    This function is designed to find and extract all Markdown-style image syntax
    from a given string of text.
    """
    #![alt text](url)
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """
    This function is designed to find and extract all Markdown-style link syntax
    from a given string of text.
    """
    #[text](url)
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
