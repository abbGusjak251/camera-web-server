import os, sys

try:
    branch = sys.argv[1]
    commit_message = input("Commit message: ")
except KeyboardInterrupt:
    exit()

os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system(f'git push origin {branch}')