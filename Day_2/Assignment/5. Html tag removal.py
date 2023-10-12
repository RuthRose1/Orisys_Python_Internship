import re

text = '''
<h1>The Crushing Bore</h1>
<p>By Chris Mills</p>

<h2>Chapter 1: The dark night</h2>
<p>
  It was a dark night. Somewhere, an owl hooted. The rain lashed down on the…
</p>

<h2>Chapter 2: The eternal silence</h2>
'''

pattern = '[<]\/?\w*[>]'
new_text = re.sub(pattern, '',text) #re.sub() -> to remove string; syntax: re.sub(string to remove, replacement, main text)

print(new_text)