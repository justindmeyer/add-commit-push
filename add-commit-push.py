import os

print("Add Commit Push with Python")
print("---------------------------")
print("git status:")
os.system("git status")
print()
userInput = input("Would you like to continue with add, commit, and push commands? Type y or n.")
print(userInput)
print()
if userInput == "y":
    print("git add -A")
    os.system("git add -A")
    print()
    print('git commit -m "update files"')
    os.system('git commit -m "update files"')
    print()
    print("git push")
    os.system("git push")
    print()
else:
    print("Commands not sent.")

print()