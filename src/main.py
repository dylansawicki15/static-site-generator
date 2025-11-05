import sys
from copy_directory_to_directory import copy_directory_to_directory
from generate_pages_recursive import generate_pages_recursive

if __name__ == "__main__":
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_directory_to_directory("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)
