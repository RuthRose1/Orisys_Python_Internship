dictionary = {'apply': 'to put to use, especially for a particular purpose',
        'bask': 'to lie in or be exposed to a pleasant warmth',
        'luminous' : 'radiating or reflecting light; shining; bright.'}
w = input('Enter word: ')
if w in dictionary.keys():
    print('Meaning:', dictionary[w])
else:
    print('Word is not found in dictionary.')
    m = input('Enter meaning of '+ w + ': ')
    dictionary[w]=m
    for i in dictionary:
        print(i + ': ' + dictionary[i])