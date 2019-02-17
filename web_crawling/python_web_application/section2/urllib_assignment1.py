# Practice Assignment
# 네이버 홈페이지 (상단, 우측 배너 광고 - 사진/동영상) 저장해보기
import sys
import io
import urllib.request as req

# base line for korean on atom
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

upImgUrl = 'https://ssl.pstatic.net/tveta/libs/1192/1192443/00fca4eb78af04a1cf23_20180619135006987.jpg'
dwImgUrl = 'https://ssl.pstatic.net/tveta/libs/1201/1201581/b582e89aba2d94752942_20180619114818397.jpg'

savePathUp1 = 'c:/Users/Chris/workspace/Pyscript/Inflearn/naver_up.jpg'
savePathUp2 = 'c:/Users/Chris/workspace/Pyscript/Inflearn/naver_down.jpg'

req.urlretrieve(upImgUrl, savePathUp1)
req.urlretrieve(dwImgUrl, savePathUp2)

print('Naver Finish!!')
# Test 변경 사항
