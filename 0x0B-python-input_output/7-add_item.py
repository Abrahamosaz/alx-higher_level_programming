#!/usr/bin/python3
"""
    function that save commands line arguments to a .json file
"""
if __name__ == "__main__":
    import sys
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file =\
        __import__("6-load_from_json_file").load_from_json_file

    filename = "add_item.json"
    try:
        my_obj = load_from_json_file(filename)
    except FileNotFoundError:
        my_obj = []
    my_obj.extend(sys.argv[1:])
    save_to_json_file(my_obj, filename)
