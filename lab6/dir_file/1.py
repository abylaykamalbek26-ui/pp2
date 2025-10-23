import os

path = r"C:\Users\Abylay\projects\pp2"


all_items = []
folders = []
files = []

for name in os.listdir(path):
    all_items.append(name)
    if os.path.isdir(os.path.join(path, name)):
        folders.append(name)
    elif os.path.isfile(os.path.join(path, name)):
        files.append(name)

print( all_items)
print(folders)
print(files)