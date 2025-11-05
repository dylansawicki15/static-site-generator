from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')
    with open(dest_path, "w") as file:
        file.write(html)