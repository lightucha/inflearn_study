from bs4 import BeautifulSoup
import sys
import io
import re # 정규표현식
'''
Tip>
http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex
'''

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = '''
<html><body>
    <ul>
        <li><a id="naver" href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="naver").text)

# 모두 다른 사이트 주솟값이기 때문에 정규표현식을 이용해서 가져오자!
li = soup.find_all(href = re.compile(r"da")) # compile 안에 정규표현식의 패턴을 입력해주면 끝. ex >> "^https://"
for e in li:
    print(e.attrs['href'])

'''
실제 활용에서는 정규표현식 보다는 CSS Selector를 사용
하지만, 강의를 통해 정규표현식을 알아보는 시간을 가졌으면 좋겠습니다.
'''
