from copy_directory_to_directory import copy_directory_to_directory
from generate_pages_recursive import generate_pages_recursive

if __name__ == "__main__":
    copy_directory_to_directory("static", "public")
    generate_pages_recursive("content", "template.html", "public")