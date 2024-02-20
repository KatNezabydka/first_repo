import pickle

def save_credentials_users(path, users_info):
    with open(path, 'wb') as file:
        for username, password in users_info.items():
            line = f"{username}:{password}\n"
            file.write(line.encode())

# Example usage:
users_info = {'andy': 'uyro18890D', 'steve': 'oppjM13LL9e'}
save_credentials_users('user_credentials.dat', users_info)