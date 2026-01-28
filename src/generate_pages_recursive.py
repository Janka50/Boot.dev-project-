import os
from src.generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(content_path):
            if item.endswith(".md"):
                html_name = item.replace(".md", ".html")
                dest_file_path = os.path.join(dest_dir_path, html_name)

                generate_page(
                    content_path,
                    template_path,
                    dest_file_path,
                    basepath
                )

        else:
            generate_pages_recursive(
                content_path,
                template_path,
                dest_path,
                basepath
            )
