import re

webs = [
    'http://www.test.co.kr',
    'ftp://www.test.co.kr',
    'http:////www.test.co.kr',
    'https:///www.test.co.kr',
    'htp://www.test.co.kr',
    'ttp://www.test.co.kr',
    'htt://www.test.co.kr',
]

web_reg = re.compile(r'https?://[\w.]+\w+$')
result = list(map(lambda w:web_reg.search(w) != None, webs))
print(result)