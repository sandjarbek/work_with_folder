from pathlib import Path

root_dir = Path("files3")
path = root_dir.iterdir()

for txt in path:
    parts = txt.parts

    new_file = txt.stem+".csv"
    # print(txt)
    new_filepath = txt.with_name(new_file)
    print(new_filepath)
    txt.rename(new_filepath)
