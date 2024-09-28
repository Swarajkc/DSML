import re
pattern = r"(\w+[\w.-]*)(@gmail.com)"
with open(r'C:\Users\shree\hello\emails.txt', 'r', encoding='utf-8') as file:
    for line in file:
        match = re.match(pattern, line.strip())
        if match:
            print(match)
            print(match.groups())