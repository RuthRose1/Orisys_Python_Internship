import re

text = """
Elon musk's phone number is 9991116666,
call him if you have any questions on dodgecoin.
Tesla's revenue is 40 billion.
Tesla's CFO number (999)-333-7777.
""" #Multiline text

pattern = re.compile("Elon")
print(pattern.match("The Elon Musk")) #Matches the 1st word of the text[Here, The Elon Musk]
print(pattern.match("Elon Musk"))
print(pattern.findall("The Elon Musk Elon  Elon  Elon  Elon  Elon "))#Finds all the Elon