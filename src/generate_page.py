from markdown_to_html_node import markdown_to_html_node
from extract_markdown import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    f = open(from_path, "r")
    f2 = open(template_path,"r")

    md_content = f.read()
    template = f2.read()

    htmlnode = markdown_to_html_node(md_content)
    html = htmlnode.to_html()
    title = extract_title(md_content)

    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",html)

    f3 = open(dest_path,"w")
    f3.write(template)


    f.close()
    f2.close()
    f3.close()