from copy_directory_to_directory import copy_directory_to_directory
from generate_page import generate_page

if __name__ == "__main__":
    copy_directory_to_directory("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page("content/contact/index.md", "template.html", "public/contact.html")
    generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel.html")
    generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom.html")
    generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty.html")