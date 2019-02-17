from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os # os의 명령어를 실행할 수 있게 하는 모듈

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = 'https://www.inflearn.com/'
quote = rep.quote_plus('추천-강좌')
url = base + quote

res = req.urlopen(url)
savePath = "C:/Users/Chris/workspace/Pyscript/Inflearn/image_inf/"

try:
    if not os.path.isdir(savePath):
        os.makedirs(os.path.join(savePath)) # save path에 image 폴더가 없으면 만들어라.
except OSError as e: # 윈도우 OS 에러
    if e.errno != errno.EEXIST: # 윈도우 에러코드가 '파일이 존재하는 메세지'는 아니어야 한다.
        print('폴더 만들기 실패') # 그 때, 에러 메세지를 팝업
        raise

soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select('ul.slides')[0]

for i, k in enumerate(img_list,1):
    with open(savePath+'text_'+str(i)+'.txt', 'wt') as f:
        f.write(k.select_one('h4.block_title > a').text)
    fullFileName = os.path.join(savePath, savePath + str(i) + '.png') # jpg
    req.urlretrieve(k.select_one('div.block_media > a > img')['src'], fullFileName)

print('다운로드 완료!')
