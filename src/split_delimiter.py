from textnode import TextType, TextNode

def split_delimiter(old_nodes, delimiter, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if delimiter in node.text:
            parts = node.text.split(delimiter)
            for part in parts:
                new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes
