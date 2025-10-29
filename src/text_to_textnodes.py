from textnode import TextNode, TextType
from split_nodes_image_and_link import split_nodes_image, split_nodes_link
from split_delimiter import split_delimiter

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Use split_delimiter for comma splitting
    nodes = split_delimiter(nodes, ",", TextType.TEXT)
    
    # Process markdown delimiters with alternating behavior
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
                    part = part.strip()
                    if part == "":
                        continue
                    if i % 2 == 0:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, text_type))
        nodes = new_nodes
    
    # Process images and links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes