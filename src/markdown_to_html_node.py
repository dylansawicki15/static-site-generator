from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from conversion import text_node_to_html_node
from textnode import TextNode, TextType

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_html_node(block, block_type)
        html_nodes.append(html_node)
    return ParentNode("div", html_nodes)

def _intersperse_missing_spaces(children: list[HTMLNode]) -> list[HTMLNode]:
    if not children:
        return children
    new_children: list[HTMLNode] = [children[0]]
    for next_child in children[1:]:
        prev_child = new_children[-1]
        def _ends_with_space(node: HTMLNode) -> bool:
            if isinstance(node, str):
                return len(node) > 0 and node[-1].isspace()
            if isinstance(node, LeafNode) and node.tag is None and isinstance(node.value, str):
                return len(node.value) > 0 and node.value[-1].isspace()
            if isinstance(node, LeafNode) and isinstance(node.value, str):
                return len(node.value) > 0 and node.value[-1].isspace()
            return False
        def _starts_with_space(node: HTMLNode) -> bool:
            if isinstance(node, str):
                return len(node) > 0 and node[0].isspace()
            if isinstance(node, LeafNode) and node.tag is None and isinstance(node.value, str):
                return len(node.value) > 0 and node.value[0].isspace()
            if isinstance(node, LeafNode) and isinstance(node.value, str):
                return len(node.value) > 0 and node.value[0].isspace()
            return False
        if not _ends_with_space(prev_child) and not _starts_with_space(next_child):
            new_children.append(LeafNode(None, " "))
        new_children.append(next_child)
    return new_children

def block_to_html_node(block: str, block_type: BlockType) -> HTMLNode:
    if block_type == BlockType.HEADING:
        stripped = block.lstrip()
        level = 0
        for ch in stripped:
            if ch == '#':
                level += 1
            else:
                break
        text = stripped[level:].lstrip()
        children = _intersperse_missing_spaces(text_to_children(text))
        return ParentNode(f"h{level}", children)
    elif block_type == BlockType.PARAGRAPH:
        text = " ".join(line.strip() for line in block.splitlines())
        children = _intersperse_missing_spaces(text_to_children(text))
        return ParentNode("p", children)
    elif block_type == BlockType.CODE:
        inner = block.strip()
        inner = inner[3:-3]
        if inner.startswith("\n"):
            inner = inner[1:]
        lines = inner.splitlines(keepends=True)
        leading_spaces = None
        for line in lines:
            stripped_line = line.lstrip('\n')
            content = line.rstrip('\n')
            if content.strip() == "":
                continue
            count = len(content) - len(content.lstrip(' '))
            if leading_spaces is None or count < leading_spaces:
                leading_spaces = count
        if leading_spaces and leading_spaces > 0:
            dedented_lines = []
            for line in lines:
                if line.strip() == "":
                    dedented_lines.append(line)
                else:
                    has_newline = line.endswith('\n')
                    without_nl = line[:-1] if has_newline else line
                    removal = min(leading_spaces, len(without_nl) - len(without_nl.lstrip(' ')))
                    new_content = without_nl[removal:]
                    dedented_lines.append(new_content + ("\n" if has_newline else ""))
            inner = "".join(dedented_lines)
        # trim trailing spaces/tabs at end while preserving final newline
        if inner.endswith(" ") or inner.endswith("\t"):
            inner = inner.rstrip(" \t")
        return ParentNode("pre", [LeafNode("code", inner)])
    elif block_type == BlockType.QUOTE:
        lines = [line.lstrip()[1:].lstrip() if line.lstrip().startswith('>') else line for line in block.splitlines()]
        text = " ".join(lines)
        children = _intersperse_missing_spaces(text_to_children(text))
        return ParentNode("blockquote", children)
    elif block_type == BlockType.UNORDERED_LIST:
        items = []
        for line in block.splitlines():
            if line.lstrip().startswith("- "):
                item_text = line.lstrip()[2:]
                items.append(ParentNode("li", _intersperse_missing_spaces(text_to_children(item_text))))
        return ParentNode("ul", items)
    elif block_type == BlockType.ORDERED_LIST:
        items = []
        for line in block.splitlines():
            stripped = line.lstrip()
            parts = stripped.split('. ', 1)
            if len(parts) == 2 and parts[0].isdigit():
                item_text = parts[1]
                items.append(ParentNode("li", _intersperse_missing_spaces(text_to_children(item_text))))
        return ParentNode("ol", items)
    else:
        children = _intersperse_missing_spaces(text_to_children(block))
        return ParentNode("p", children)

def text_to_children(text: str) -> list[HTMLNode]:
    if text.startswith("```") and text.endswith("```"):
        inner = text.strip()
        inner = inner[3:-3]
        if inner.startswith("\n"):
            inner = inner[1:]
        return [text_node_to_html_node(TextNode(inner, TextType.CODE))]

    textnodes = text_to_textnodes(text)
    return [text_node_to_html_node(textnode) for textnode in textnodes]

if __name__ == "__main__":
    md = """
    # This is a heading

    This is a paragraph

    This is another paragraph
    """
    node = markdown_to_html_node(md)
    print(node)