#!/usr/bin/python3
def search_replace(original_list, target, replacement):
    modified_list = list(original_list)
    for index in range(len(modified_list)):
        if modified_list[index] == target:
            modified_list[index] = replacement
    return modified_list

