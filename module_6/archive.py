import shutil
import pickle

def create_backup(path, file_name, employee_residence):
    # Step 1: Save the employee_residence dictionary to a binary file
    with open(f"{path}/{file_name}", 'wb') as file:
        for username, residence in employee_residence.items():
            line = f"{username} {residence}\n"
            file.write(line.encode())

    # Step 2: Archive the folder at the specified path
    archive_path = shutil.make_archive(f"{path}/backup_folder", 'zip', path)

    return archive_path

# Example usage:
employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
result = create_backup('./', 'employee_data.dat', employee_residence)
print(result)