import os

print("Add Commit Push with Python")
print("---------------------------")
print("git status:")
os.system("git status")
print()
message = input("Would you like to continue with add, commit, and push commands? Type y or n.")
print(message)
print("git add -A")
os.system("git add -A")
print()
print('git commit -m "update files"')
os.system('git commit -m "update files"')
print()
print("git push")
os.system("git push")
print()