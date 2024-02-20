import pickle

def get_credentials_users(path):
    credentials_list = []
    with open(path, 'rb') as file:
        for line in file:
            credentials_list.append(line.decode().strip())
    return credentials_list

# Example usage:
file_path = 'user_credentials.dat'
result = get_credentials_users(file_path)
print(result)