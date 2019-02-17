import sys
import io
import urllib.request

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Practice
imgUrl = "http://post.phinf.naver.net/20160930_44/1475223463172cN5PK_JPEG/IrcmE-neMSV5ftXDoKjNZg0Ec_4s.jpg"
htmlUrl = "http://google.com"

savePath1 = "c:/Users/Chris/workspace/Pyscript/Inflearn/test.jpg"
savePath2 = "c:/Users/Chris/workspace/Pyscript/Inflearn/index.html"

f = urllib.request.urlopen(imgUrl).read()
f2 = urllib.request.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb') # w: write, r: read, a: add
saveFile1.write(f)
saveFile1.close() # 메모리에 읽고 쓴 resource 반납을 해줘야 함.

with open(savePath2, 'wb') as saveFile2: # with문은 with문을 나가게 되면 close됨.
    saveFile2.write(f2)

print("finish download!")

'''
urlopen vs. urlretrieve
> urlretrieve(direct 저장)
: 저장 -> open('r') -> 변수 할당 -> 파싱 -> 저장
#ex> 여러 문서를 한 번에 다운로드 받을 때(구글에서 사진 1000장을 다운로드 just 반복문)

> urlopen(memory 저장)
: 변수 할당 -> 파싱 -> 저장(db..)
'''
