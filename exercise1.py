from pathlib import Path

root_dir = Path('files2')
file_paths = root_dir.iterdir()

for path in file_paths:
    list = path.iterdir()
    # print(path)
    for item in list:
        # print(item)
        # new_foldername = path.name+"-" + item.name+ item.suffix
        # new_filepath = f"{item}\{new_foldername}"
        # print(new_filepath)
        list_file = item.iterdir()
        for file in list_file:
            # print(file)
            new_filename = path.name+"-"+item.name+"-"+file.name
            new_filepath = f"{item}\{new_filename}"
            print(new_filepath)




            file.rename(new_filepath)