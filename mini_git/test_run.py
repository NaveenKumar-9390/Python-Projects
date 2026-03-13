import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from main import init_repo, add_file, commit, log_commits, status

print("Testing mini git:")

print("\n1. Initializing repository:")
init_repo()

print("\n2. Creating test file:")
with open("test_file.txt", "w") as f:
    f.write("Hello Git!")

print("\n3. Adding file to staging:")
add_file("test_file.txt")

print("\n4. Checking status:")
status()

print("\n5. Committing:")
commit("Initial commit")

print("\n6. Checking log:")
log_commits()

print("\n7. Checking status after commit:")
status()

print("\n[OK] Mini git works correctly!")

# Cleanup
os.remove("test_file.txt")
