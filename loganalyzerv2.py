#   Rickard Andersson rickard.johan.a@protonmail.com
import sys
import re

# Using the try statement to see if the arg ect are correct
try:
    arg1_file = sys.argv[1]
    arg2_action = sys.argv[2]
    with open(arg1_file, "r") as file_object:
        file = file_object.read()
        actions = ["error", "notice", "statistics"]
        if arg2_action not in actions:
            raise IndexError
except (FileNotFoundError, IndexError):
    print("Sorry, file not found")
    print("Index or typo error")

# The code starts if the args are correct
else:
    if arg2_action == "notice":
        for line in file:
            sub_str = "notice".lower()
            if line.lower().find(sub_str) != -1:
                print(line.rstrip())
    
    elif arg2_action == "error":
        for line in file:
            sub_str = "error".lower()
            if line.lower().find(sub_str) != -1:
                print(line.rstrip())
    
    elif arg2_action == "statistics":
        notices = file.count("[notice]")
        errors = file.count("[error]")
    print("Error: " + str(errors) + "\nNotice: " + str(notices))
