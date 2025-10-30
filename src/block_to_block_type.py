import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    block = block.strip()
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif all(
        re.match(r'^(\d+)\.', line) 
        for line in block.splitlines()
    ):
        lines = block.splitlines()
        numbers = []
        for line in lines:
            match = re.match(r'^(\d+)\.', line)
            if match:
                numbers.append(int(match.group(1)))
            else:
                break
        if numbers == list(range(numbers[0], numbers[0] + len(numbers))):
            return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH