from pathlib import Path

p1 = Path('files/dxx.txt')
print(type(p1))

if not p1.exists():
    with open(p1, "w") as file:
        file.write('content4')

print(p1.name)
print(p1.stem)
print(p1.suffix)


# print(p1.name)
# print(p1.stem)
# print(p1.suffix)
#
p2 = Path('files')
print(list(p2.iterdir()))
list=[]
for item in p2.iterdir():
    print(item.name)

