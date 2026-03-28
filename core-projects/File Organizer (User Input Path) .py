# File Organizer

import os
import shutil

path = input("Enter folder path: ")

for file in os.listdir(path):
    full_path = os.path.join(path, file)

    if os.path.isfile(full_path):
        ext = file.split('.')[-1]

        folder = os.path.join(path, ext)
        os.makedirs(folder, exist_ok=True)

        shutil.move(full_path, os.path.join(folder, file))

print("Files Organized Successfully!")