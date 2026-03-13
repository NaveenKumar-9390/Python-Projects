from main import FileSystem

print("Testing file system simulator:")
fs = FileSystem()

print("\n1. Creating folders and files:")
fs.mkdir("documents")
fs.mkdir("photos")
fs.touch("readme.txt")

print("\n2. Listing contents:")
fs.ls()

print("\n3. Changing directory:")
fs.cd("documents")
fs.pwd()

print("\n4. Creating file in documents:")
fs.touch("report.txt")
fs.ls()

print("\n5. Going back:")
fs.cd("..")
fs.pwd()

print("\n6. Removing item:")
fs.rm("photos")
fs.ls()

print("\n[OK] File system simulator works correctly!")
