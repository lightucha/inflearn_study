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

urllib.request.urlretrieve(imgUrl, savePath1)
urllib.request.urlretrieve(htmlUrl, savePath2)

print("finish download!")
