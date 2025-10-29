import re

def extract_markdown_images(text: str) -> tuple[list[str], list[str]]:
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text: str) -> tuple[list[str], list[str]]:
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links