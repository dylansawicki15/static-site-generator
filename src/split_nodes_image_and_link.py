from textnode import TextNode, TextType
from extract_images_and_links import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.IMAGE:
            images = extract_markdown_images(node.text)
            for image in images:
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.LINK:
            links = extract_markdown_links(node.text)
            for link in links:
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        else:
            new_nodes.append(node)
    return new_nodes