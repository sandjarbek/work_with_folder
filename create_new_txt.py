from pathlib import Path

root_dir = Path("files4")

for i in range(10,21):
    new_file = str(i)+"."+"txt"
    filepath = root_dir/new_file
    print(filepath)
    filepath.touch()
