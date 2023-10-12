import re

text = '''
1. Visit our website at https://www.example.com for more information.
2. Check out the latest news on http://news.example.org.
4. Follow us on Twitter: https://twitter.com/ExampleAccount.
5. Watch videos on YouTube: https://www.youtube.com/user/ExampleChannel.
'''

pattern = 'http[s]?\S+(?<!\.)'
print(re.findall(pattern, text))