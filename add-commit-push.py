import os
import sys

print()
print("Add, Commit, and Push Commands with Python")
print()
print("git status:")
print()
os.system("git status")
print()
print("Would you like to continue with add, commit, and push commands? Type y or n.")
userInput = input()
print()
if userInput == "y":
    print("git add -A")
    print()
    os.system("git add -A")
    print()
    print("What would you like your commit message to be?")
    message = input()
    commitMessage = 'git commit -m "' + message + '"'
    print(commitMessage)
    print()
    os.system(commitMessage)
    print()
    print("git push")
    print()
    os.system("git push")
    print()
else:
    print("Commands not sent.")
print()