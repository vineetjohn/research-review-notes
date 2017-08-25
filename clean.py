#!/usr/bin/env python

import sys
import os

extensions_to_delete = [
    "log",
    "out",
    "blg",
    "synctex.gz",
    "fdb_latexmk",
    "aux",
    "bbl",
    "fls",
]


def is_useless_file(filename):
    for extension in extensions_to_delete:
        if filename.endswith(extension):
            return True

    return False


def clean_dir(directory_path):
    files_to_delete = set()

    for root, dirs, files in os.walk(directory_path):
        files = [root + "/" + f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        filtered_files = list(filter(is_useless_file, files))

        for filename in filtered_files:
            files_to_delete.add(filename)

    if len(files_to_delete) == 0:
        print("No files to delete")
    else:
        for filename in files_to_delete:
            absolute_file_path = os.path.abspath(filename)
            print("Deleting " + absolute_file_path)
            os.remove(absolute_file_path)


clean_dir(sys.argv[1])
