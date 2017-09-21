#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""DirectoryTreeRenamer_1.0
   Removes special characters from every subdirectory and file
   name in the directory structure, including final "." in the
   folders' name.
"""
import os

forbidden_chars = ["/", "\\", "<", ">", ":", "*", "\"", "?", "|"]


def remove_forbid_chars(current_dir):
    dirs_and_files = os.scandir(current_dir)

    for entry in dirs_and_files:
        # Get dir or file name
        entry_path_list = entry.path.split('/')
        entry_name = entry_path_list[len(entry_path_list) - 1]

        # Ignore macOS files
        if entry_name == '.DS_Store':
            pass
        else:
            # Remove file's extension
            if entry.is_file() is True:
                extension = entry_name.split('.')[
                                                  len(entry_name.split('.'))
                                                  - 1
                                                  ]
                entry_name = entry_name.split('.')[0]

            # Remove forbidden chars from files' and dirs' name
            string_index = 0
            """ string_index increases every iteration
                except if a char from entry_name is suppresed
            """
            for c in entry_name:
                if c in forbidden_chars:
                    entry_name = entry_name[:string_index] + ''\
                                 + entry_name[string_index+1:]
                else:
                    string_index += 1

            # Remove "." from last position in folders' name
            if entry.is_dir() is True:
                if entry_name[len(entry_name) - 1] == '.':
                    entry_name = entry_name[:len(entry_name) - 1]
            # Recover file's extension
            else:
                entry_name = entry_name + '.' + extension

            # Rename fields and folders accordingly
            os.rename(entry.path, os.path.join(current_dir, entry_name))

            # # Act recursively for found folders
            if entry.is_dir() is True:
                remove_forbid_chars(os.path.join(current_dir, entry_name))


remove_forbid_chars(os.getcwd())
