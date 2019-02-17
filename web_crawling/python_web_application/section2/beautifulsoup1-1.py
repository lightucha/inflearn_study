from bs4 import BeautifulSoup
import sys
import io

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = '''
<html>
<body>
<h1>파이썬 ButifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
#print('soup', type(soup))
#print('prettify', soup.prettify())

h1 = soup.html.body.h1 # 바로 접근이 가능
print('h1', h1)

p1 = soup.html.body.p # p tag가 두개인데 어떻게 출력되나?
print('p1', p1)

p2 = p1.next_sibling
print('p2', p2) # \n 가 존재하기 때문에 아무것도 안나오는 것처럼 보인다
print('p22', p2.next_sibling)

p3 = p1.previous_sibling.previous_sibling
print('p3', p3)

print('h1 >> ', h1.string)
print('p >> ', p1.string)
print('p >> ', p2.next_sibling.string)
'''
태그 이동은 많이 사용되지는 않는다.
사이트가 퍼블리싱 될 때 변경사항이 생기면, 소스 코드가 정상 작동하지 않는다.
하지만, 기본 명령어이므로 알고 있을 필요는 있다.
'''
