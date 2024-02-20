import sys


def parse_args():
    result = ""
    args_without_script_name = sys.argv[1:]
    return ' '.join(args_without_script_name)


args_string = parse_args()
print("Command line arguments:", args_string)
