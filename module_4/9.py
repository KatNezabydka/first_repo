from pathlib import Path

def parse_folder(path):
    files = []
    folders = []

    for record in path.iterdir():
        if record.is_file():
            files.append(record.name)
        elif record.is_dir():
            folders.append(record.name)

    return files, folders

path = Path(".")  # Use "." to represent the current directory
files, directories = parse_folder(path)
print("Files:", files)
print("Directories:", directories)