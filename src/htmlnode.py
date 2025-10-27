class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag if tag is not None else None
        self.value = value if value is not None else None
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError("We aint done this yet")
    
    def props_to_html(self) -> str:
        string = ""
        for prop, value in self.props.items():
            string += f"{prop}=\"{value}\" "
        return string.strip()
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{' ' if self.props else ''}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if len(self.children) == 0:
            raise ValueError("ParentNode must have at least one child")
        return f"<{self.tag}{' ' if self.props else ''}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
    