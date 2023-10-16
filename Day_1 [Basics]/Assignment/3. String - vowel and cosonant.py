s = input('Enter string: ')
v = 0
c = 0
for i in s:
    s = s.lower()
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        v += 1
    elif i != ' ':
        c += 1
print('Vowel:', v)
print('Consonant:', c)