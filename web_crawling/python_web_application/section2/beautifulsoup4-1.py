from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os # os의 명령어를 실행할 수 있게 하는 모듈

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
quote = rep.quote_plus('연예인')
url = base + quote

res = req.urlopen(url)
savePath = "C:/Users/Chris/workspace/Pyscript/Inflearn/image/"

try:
    if not os.path.isdir(savePath):
        os.makedirs(os.path.join(savePath)) # save path에 image 폴더가 없으면 만들어라.
except OSError as e: # 윈도우 OS 에러
    if e.errno != errno.EEXIST: # 윈도우 에러코드가 '파일이 존재하는 메세지'는 아니어야 한다.
        print('폴더 만들기 실패') # 그 때, 에러 메세지를 팝업
        raise

soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select('div.img_area > a.thumb._thumb > img')

for i, img_list in enumerate(img_list,1):
    #print(img_list['src']) # http 통신 방식으로 직접 요청하기 때문에 렌더링 될 때 브라우저에서 보이는 것과 다를 수 있다.
    #print(img_list['data-source'])
    fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    req.urlretrieve(img_list['data-source'], fullFileName)

print('다운로드 완료!')
