import os
from src.markdown_html_nodes import markdown_to_html_node
from src.extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath ):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}"
    )

    # Read markdown
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    # Read template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Convert markdown → HTML STRING (CRITICAL)
    html_node = markdown_to_html_node(markdown)
    content_html = html_node.to_html()  # ← THIS WAS MISSING

    # Extract title
    title = extract_title(markdown)

    # Replace placeholders
    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", content_html)
     # ✅ BASEPATH FIX
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)
