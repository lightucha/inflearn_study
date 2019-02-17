from bs4 import BeautifulSoup
import sys
import io

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 다양한 선택자를 활용하여,
# food-list.html 구조에서 "양주"를 집중적으로 파헤쳐 보자!

fp = open('./food-list.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

print('1', soup.select_one('li:nth-of-type(8)').text) #li 태그의 8번째에 접근하여 텍스르로 출력
print('2', soup.select_one('#ac-list > li:nth-of-type(4)').text) # '>' 자식 선택자(자식에서만 가져옴) / '>' 없으면, 자손 선택자(조건만 맞으면 자손, 자식 모두)
print('3', soup.select("#ac-list > li[data-lo='cn']")[0].text) # select 는 list로 반환한다는 것을 명심
print('4', soup.select("#ac-list > li.alcohol.high")[0].text)

param = {'data-lo': 'cn', 'class': 'alcohol'}
print('5', soup.find('li', param).string)
print('6', soup.find(id = 'ac-list').find('li', param).text) # 부모부터 자식까지 자세하게 접근, 성능적으로는 5번이 효율적

for ac in soup.find_all('li'):
    if ac['data-lo'] =='us':
        print('data-lo == us', ac.string)
