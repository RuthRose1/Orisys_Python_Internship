import re

text = """
Here are some dates: 02/40/2023, 17/31/2022, 12/02/2022, 05/17/2024, 04/31/2023
10/21/2023
21/10/2021
09/28/2021
12/30/2028
"""

pattern = '\b(0[1-9]|1[0-2])\/([012][0-9]|3[01])\/(\d{4})\b' 
#match = re.findall(pattern, text)
print(re.findall(pattern, text))

#Loop is needed as printing re.findall(pattern, text) the date, month and year is separated by comma, i.e., ('10', '21', '2023'), etc.
'''for i in match:
    date = "/".join(i)  # Join the three captured groups with "/"
    print(date)'''