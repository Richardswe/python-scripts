# Rickard Andersson rickard.johan.a@protonmail.com
# syntax in cli: python3 loganalyzer.py test.log statistics/error/notice
import sys
import re

#   The variable to store the output
statistics = []

# Using the try statement to see if the arg ect are correct
try:
    arg1_file = sys.argv[1]
    arg2_action = sys.argv[2]
    with open(arg1_file, "r") as file_object:
        file = file_object.readlines()
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
        for line in file:
            statistics.append(line)
            sub_s = "notice"
            sub_s2 = "error"
            res = [x for x in statistics if re.search(sub_s, x)]
            res2 = [x for x in statistics if re.search(sub_s2, x)]
            nl_1 = len(res)
            nl_2 = len(res2)
        print("Error: " + str(nl_2) + "\nNotice: " + str(nl_1))
