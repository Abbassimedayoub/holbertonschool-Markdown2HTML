#!/usr/bin/env python3

import sys
import os 
def main():
    # Check if the number of arguments is exactly 2
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # If all checks pass, print nothing and exit with status code 0
    sys.exit(0)

if __name__ == "__main__":
    main()
