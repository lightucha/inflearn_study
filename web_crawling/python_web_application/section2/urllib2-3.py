import sys
import io
import urllib.request as req
from urllib.parse import urlencode

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# Get 방식 API 사이트에서 받아서 반환
# https://www.ipify.org/

api = 'http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp' # 서비스를 제공하는 사이트만 찾으면 됨.

values = {
    'ctxCd': '1012'
}

print('before', values)
params = urlencode(values) # 동적 활용을 위해
print('after', params)

url = api + "?" + params # 형식을 맞추는 작업
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print('출력', reqData) # 사이트에서 제공하는 ip를 확인 할 수 있음.

# 주기적으로 정보를 받아 볼 수 있다.
