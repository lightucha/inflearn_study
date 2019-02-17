from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

'''
https://www.inflearn.com/추천-강좌/
url에 한글이 들어가 있으면 Python에서는 Error 발생
한글이 포함된 url은 유니코드 형식으로 변환 해줘야 함
'''
# Bootstrap으로 만들어진 사이트!
# 복잡하다..
base = 'https://www.inflearn.com/' # Atop Editor에서는 한글을 유니코드로 자동으로 변환
quote = rep.quote_plus('추천-강좌') # 유니코드 변환할 수 있는 방법

url = base + quote

res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')

recommand = soup.select('ul.slides')[0]
for i, e in enumerate(recommand, 1):
    print(i, ', ',e.select_one('h4.block_title > a').text)
