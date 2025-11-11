import os
from .functions import copy_directory_contents, generate_page


def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))  # site_generator/
    static_path = os.path.join(base_dir, "static")
    content_path = os.path.join(base_dir, "content/index.md")
    template_path = os.path.join(base_dir, "template.html")
    destination_path = os.path.join(base_dir, "public")
    index_path = os.path.join(destination_path, "index.html")
    copy_directory_contents(static_path, destination_path)
    generate_page(content_path, template_path, index_path)
    



if __name__ == "__main__":
    main()
