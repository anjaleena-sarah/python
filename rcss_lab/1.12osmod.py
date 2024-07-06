import os

# 1.12. Using the OS Module 

# 1.12.1. Create a directory
def create_directory(directory_name):
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory '{directory_name}' created successfully.")
    except OSError as e:
        print(f"Error: {e}")

# 1.12.2. Directory Listing
def list_directory(directory_name):
    try:
        with os.scandir(directory_name) as entries:
            for entry in entries:
                print(entry.name)
    except OSError as e:
        print(f"Error: {e}")

# 1.12.3. Search for ".py" files
def search_py_files(directory_name):
    try:
        py_files = [f for f in os.listdir(directory_name) if f.endswith('.py')]
        for file in py_files:
            print(file)
    except OSError as e:
        print(f"Error: {e}")

# 1.12.4. Remove a particular file
def remove_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' removed successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except OSError as e:
        print(f"Error: {e}")

# Example usage of OS module functions
create_directory('new_directory')
list_directory('new_directory')
search_py_files('.')
remove_file('example.py')
