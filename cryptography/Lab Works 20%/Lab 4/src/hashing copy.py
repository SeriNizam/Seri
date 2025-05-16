import hashlib

# Ask user to enter filename
filename = input("Enter the filename to hash: ")

try:
    with open(filename, "rb") as f:
        file_data = f.read()
        file_hash = hashlib.sha256(file_data).hexdigest()
        print("SHA-256 Hash of File:", file_hash)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
