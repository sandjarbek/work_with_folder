from pathlib import Path

root_dir = Path(".")
# print(root_dir.absolute())
search_term = "archive1"


for path in root_dir.rglob("*.zip"):
    # print(path)
    if path.is_file():
        # print(path.absolute())
        if search_term in path.stem:
            print(path.absolute())