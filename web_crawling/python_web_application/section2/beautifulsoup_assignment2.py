from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Daum 사이트 실시간 검색어 + link 가져오기
url = 'https://www.daum.net/'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')

keyword = soup.find_all('a', tabindex="-1") # 선택자를 무엇으로 할 것인가? 매우 중요 !!!
for i, e in enumerate(keyword, 1):
    print(i, ', ', e.text, ': ', e.attrs['href'])
