import re

flag = 0
while (flag == 0):
    print("Domain Extraction")
    print("1. Finding domain\n2. Exit")
    ch = int(input("Enter choice:"))
    if ch == 1:
        url = input("Enter url: ")
        pattern = 'http[s]?:\/\/(www\.)?([^\/]+)'
        match = re.search(pattern, url)
        if match != []:
            domain = match.group(2)
            print(f"Domain: {domain}\n")
    elif ch == 2:
        flag = 1
    else:
        print("Invalid input")