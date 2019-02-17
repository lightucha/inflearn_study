from bs4 import BeautifulSoup
import sys
import io

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = '''
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
'''
# 태그 선택자의 사용
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')
#print('links', type(links))

a = soup.find_all("a", string = 'daum')
print('a', a)

b = soup.find('a') # 가장 상위 태그만 출력
print('b', b)

c = soup.find_all('a', limit = 2)
print('c', c)

d = soup.find_all(string=['naver', 'daum']) # 보통은 정규표현식을 사용해서 문자를 불러올 때 사용
print('d', d)

for a in links:
    #print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    # print('txt >> ', txt, 'href >> ', href)

###########################################################################
#### self-practice
###########################################################################

import re
import requests

def not_lacie(href):
    return href and not re.compile("lacie").search(href)

url = 'https://www.naver.com/'
html1 = requests.get(url).text
soup2 = BeautifulSoup(html1, 'html.parser')
e = soup.find_all(href=not_lacie)
print('e', e)
print('====================================================================================')
f = soup.find_all(re.compile('<a.*href="(.*)".*a>'))
print('f', f)

for ex in soup.find_all(re.compile('<a.*href="(.*)" ')):
    print('111')
    print(ex)

print('====================================================================================')
