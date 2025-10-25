from textnode import TextNode, TextType

if __name__ == "__main__":
    text_node = TextNode("Hello, World!", TextType.TEXT, "https://www.google.com")
    print(text_node)