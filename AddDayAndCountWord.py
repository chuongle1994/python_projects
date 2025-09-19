import os
from datetime import datetime

directory = 'files'
filenames = os.listdir(directory)
for filename in filenames:
    full_path = os.path.join(directory, filename)
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read()

        word_count = len(content.split())
    new_filename = f'{filename[:-4]}_{word_count}_{datetime.now().strftime("%A")}.txt'
    new_full_path = os.path.join(directory, new_filename)
    os.rename(full_path, new_full_path)
    print(f'Renamed {filename} to {new_filename}')

