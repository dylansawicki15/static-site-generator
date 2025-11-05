from textnode import TextNode, TextType
from extract_images_and_links import extract_markdown_images, extract_markdown_links

def _split_nodes_by_markdown(old_nodes: list[TextNode], extract_func, markdown_format: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        matches = extract_func(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        
        remaining_text = node.text
        for text, url in matches:
            markdown = markdown_format.format(text, url)
            before, _, remaining_text = remaining_text.partition(markdown)
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(text, text_type, url))
        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    return _split_nodes_by_markdown(old_nodes, extract_markdown_images, "![{}]({})", TextType.IMAGE)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return _split_nodes_by_markdown(old_nodes, extract_markdown_links, "[{}]({})", TextType.LINK)