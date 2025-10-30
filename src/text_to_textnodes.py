from textnode import TextNode, TextType
from split_nodes_image_and_link import split_nodes_image, split_nodes_link
from split_delimiter import split_delimiter

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    
    nodes = split_delimiter(nodes, ",", TextType.TEXT)
    normalized_nodes: list[TextNode] = []
    for node in nodes:
        if node.text_type == TextType.TEXT:
            normalized_nodes.append(TextNode(node.text.lstrip(), TextType.TEXT))
        else:
            normalized_nodes.append(node)
    nodes = normalized_nodes
    
    for delimiter, text_type in [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]:
        new_nodes = []
        for node in nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue
            
            parts = node.text.split(delimiter)
            if len(parts) == 1:
                new_nodes.append(node)
            else:
                for i, part in enumerate(parts):
                    if part == "":
                        continue
                    if i % 2 == 0:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, text_type))
        nodes = new_nodes
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    normalized: list[TextNode] = []
    for node in nodes:
        if node.text_type == TextType.TEXT:
            trimmed = node.text.strip()
            if trimmed == "":
                continue
            normalized.append(TextNode(trimmed, TextType.TEXT))
        else:
            normalized.append(node)
    return normalized