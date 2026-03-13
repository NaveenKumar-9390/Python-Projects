import os
import shutil
import time

REPO_DIR = "repo"
STAGE_DIR = "repo/staging"
COMMITS_DIR = "repo/commits"


def init_repo():

    os.makedirs(STAGE_DIR, exist_ok=True)
    os.makedirs(COMMITS_DIR, exist_ok=True)

    print("Repository initialized")


def add_file(filename):

    if not os.path.exists(filename):
        print("File not found")
        return

    shutil.copy(filename, STAGE_DIR)

    print(filename, "added to staging area")


def commit(message):

    if not os.listdir(STAGE_DIR):
        print("Nothing to commit")
        return

    commit_id = str(int(time.time()))
    commit_path = os.path.join(COMMITS_DIR, commit_id)

    os.makedirs(commit_path)

    for file in os.listdir(STAGE_DIR):
        shutil.copy(os.path.join(STAGE_DIR, file), commit_path)

    print("Committed:", message)

    for file in os.listdir(STAGE_DIR):
        os.remove(os.path.join(STAGE_DIR, file))


def log_commits():

    commits = os.listdir(COMMITS_DIR)

    if not commits:
        print("No commits yet")
        return

    print("Commit history:")

    for c in sorted(commits, reverse=True):
        print("Commit", c)


def status():

    files = os.listdir(STAGE_DIR)

    if not files:
        print("No files staged")

    else:
        print("Staged files:")
        for f in files:
            print("-", f)


def main():

    while True:

        cmd = input("mini-git> ").split()

        if not cmd:
            continue

        command = cmd[0]

        if command == "init":
            init_repo()

        elif command == "add":
            add_file(cmd[1])

        elif command == "commit":
            message = " ".join(cmd[1:])
            commit(message)

        elif command == "log":
            log_commits()

        elif command == "status":
            status()

        elif command == "exit":
            break

        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
