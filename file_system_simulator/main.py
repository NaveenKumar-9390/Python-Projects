class FileSystem:
    
    def __init__(self):
        self.fs = {"root": {}}
        self.current = self.fs["root"]
        self.path = ["root"]

    def mkdir(self, folder):
        if folder not in self.current:
            self.current[folder] = {}
            print("Folder created:", folder)
        else:
            print("Folder already exists")

    def touch(self, filename):
        if filename not in self.current:
            self.current[filename] = "file"
            print("File created:", filename)
        else:
            print("File already exists")

    def ls(self):
        for item in self.current:
            print(item)

    def cd(self, folder):
        if folder == "..":
            if len(self.path) > 1:
                self.path.pop()
                temp = self.fs
                for p in self.path:
                    temp = temp[p]
                self.current = temp
        elif folder in self.current and isinstance(self.current[folder], dict):
            self.current = self.current[folder]
            self.path.append(folder)
        else:
            print("Folder not found")

    def rm(self, name):
        if name in self.current:
            del self.current[name]
            print(name, "deleted")
        else:
            print("File/Folder not found")

    def pwd(self):
        print("/".join(self.path))


def run():

    fs = FileSystem()

    print("Simple File System Simulator")
    print("Commands: mkdir, touch, ls, cd, rm, pwd, exit")

    while True:

        cmd = input(">> ").split()

        if not cmd:
            continue

        command = cmd[0]

        if command == "mkdir":
            fs.mkdir(cmd[1])

        elif command == "touch":
            fs.touch(cmd[1])

        elif command == "ls":
            fs.ls()

        elif command == "cd":
            fs.cd(cmd[1])

        elif command == "rm":
            fs.rm(cmd[1])

        elif command == "pwd":
            fs.pwd()

        elif command == "exit":
            break

        else:
            print("Invalid command")


if __name__ == "__main__":
    run()