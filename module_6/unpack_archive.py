import shutil

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)

# Example usage:
archive_path = './backup_folder.zip'
path_to_unpack = './'
unpack(archive_path, path_to_unpack)