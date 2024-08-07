#!/usr/bin/env python3

import sys
import os
import markdown

def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    try:
        with open(markdown_file, 'r') as md_file:
            md_content = md_file.read()
            html_content = markdown.markdown(md_content)

        # Write the HTML content to the output file
        with open(html_file, 'w') as out_file:
            out_file.write(html_content)

    except Exception as e:
        sys.exit(1)

    # If all checks pass, print nothing and exit with status code 0
    sys.exit(0)

if __name__ == "__main__":
    main()
