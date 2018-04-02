import sys
import os
import subprocess

initial_layout = [
    "---",
    "layout: default",
    "permalink: 'reviews/{}.html'",
    "title: '{}'",
    "---\n",
    "# {}",
    "---\n",
    "## Idea\n\n",
    "## Method\n\n",
    "## Observations\n\n"
]


def main():
    paper_name = sys.argv[1]
    formatted_name = subprocess.check_output(
        ["filename-formatter", paper_name]).decode("utf-8").strip()
    file_contents = "\n".join(initial_layout)

    with open("_reviews/{}.md".format(formatted_name), 'w') as f:
        f.write(file_contents.format(formatted_name, paper_name, paper_name))


if __name__ == '__main__':
    main()
