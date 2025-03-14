from pathlib import Path


path = Path("ecommerce")

print(path.exists())

path1 = Path("check")

path1.mkdir()

path1.rmdir()

path2 = Path()

for file in path2.glob("*.*"):
    print(file)



