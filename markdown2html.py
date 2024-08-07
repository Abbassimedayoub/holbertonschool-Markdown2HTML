#!/usr/bin/python3
import sys
import os


def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        sys.stderr.write(f"missing {markdown_file}\n")
        sys.exit(1)

    # If all checks pass, exit with status code 0
    sys.exit(0)


if __name__ == "__main__":
    main()
