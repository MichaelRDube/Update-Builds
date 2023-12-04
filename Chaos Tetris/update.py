import urllib.request, sys, os

if not os.path.isdir("Assets"):
    os.mkdir("Assets")
    
urllib.request.urlretrieve('https://raw.github.com/MichaelRDube/ChaosTetris/main/Assets/update%20script.py', 'Assets/update script.py')


file_path = "Assets/update script.py"
try:
    with open(file_path, 'r') as file:
        python_code = file.read()
        exec(python_code)
except FileNotFoundError:
    print(f"Error:  The file '{file_path}' does not exist.")
