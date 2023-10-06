from pathlib import Path

root_dir = Path("files3")

for path in root_dir.rglob("**/*.txt"):
    print(path)
    if path.is_file():
        new_file = path.with_suffix(".jpeg")
        path.rename(new_file)