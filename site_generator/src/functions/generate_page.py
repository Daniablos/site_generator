import os

from .markdown_to_htmlnode import markdown_to_htmlnode 
from .extract_title import extract_title

def generate_page(from_path: str, template_path: str, dest_path: str):
    """
    Функция преобразует MD файл из `from_path` в HTML файл на основе HTML образца из `template_path` и 
    помещает его по пути назначения `dest_path`. Оригинальный MD файл не изменяется. 
    """
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'")

    print(f"  Reading Markdown from: {from_path}")
    with open(from_path, 'r') as md_file:
        markdown_content = md_file.read()

    print(f"  Reading template from: {template_path}")
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    print("  Converting Markdown to HTML...")
    html_node_root = markdown_to_htmlnode(markdown_content)
    page_html_content = html_node_root.to_html()

    print("  Extracting page title...")
    page_title = extract_title(markdown_content)

    print("  Replacing placeholders in template...")
    final_html_content = template_content.replace("{{ Title }}", page_title)
    final_html_content = final_html_content.replace("{{ Content }}", page_html_content)

    print(f"  Writing final HTML to: {dest_path}")
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, 'w') as output_file:
        output_file.write(final_html_content)

    print(f"Successfully generated page: '{dest_path}'")