from pathlib import Path
from datetime import datetime
import glob


def create_file(month,file):
    path = Path(f"files2/2021/{month}/{file}")
    stats=path.stat()
    second_created = stats.st_ctime
    data_created = datetime.fromtimestamp(second_created)
    data_created_str = data_created.strftime("%Y-%m-%d_%H-%M-%S")
    new_file = f"{data_created_str}_{path.name}"
    return new_file

# print(create_file("a.txt"))
new_path = Path(f"files2/2021")

path_list = new_path.glob("**/*")

#
for file in path_list:
    # print(file)
    if file.is_file():
        file_parts = file.parts
        # print(file_parts)
        # # create_file(file.name)
        new = file.with_name(create_file(file_parts[2],file.name))
        # print(file)
        # print(new)
        file.rename(new)


        # new_file = f"{file_parts[0]}/{file_parts[1]}/{file_parts[2]}/{create_file(file.name)}"
        # print(new_file)
        # create_file(file.name)
        # print(create_file(f"{file.name}"))
        # print(str(file.name))
        # print(create_file(file.name))