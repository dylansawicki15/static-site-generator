import os
from generate_page import generate_page

def generate_pages_recursive(from_path, template_path, dest_path, basepath="/"):
    for root, _, files in os.walk(from_path):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(md_file_path, from_path)
                html_file_path = os.path.join(dest_path, relative_path.replace(".md", ".html"))
                os.makedirs(os.path.dirname(html_file_path), exist_ok=True)
                generate_page(md_file_path, template_path, html_file_path, basepath)