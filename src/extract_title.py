def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("#"):
            return line.strip()[1:].strip()
    return ""

if __name__ == "__main__":
    md = """
# This is a title

This is a paragraph

## This is a subheading
"""
    print(extract_title(md))