def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    for line in markdown.split('\n\n'):
        if line.strip() == "" or line.strip() == "\n":
            continue
        blocks.append(str(line.strip()))
    return blocks