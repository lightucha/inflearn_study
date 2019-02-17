import sys
import io
import urllib.request as req
from urllib.parse import urlparse

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = 'http://www.encar.com'

mem = req.urlopen(url) # url open해서 반환(아래 print문)
'''
# httpResponse Attribute
print('geturl', mem.geturl())
print('status', mem.status) # 200(정상), 404(없음), 403(거절), 500(서버 자체 에러), ....
print('headers', mem.getheaders())
print('info', mem.info())
print('code', mem.getcode())
print('read', mem.read(50).decode('utf-8')) #euc-kr(old site), ...
'''
print(urlparse('http://www.encar.com'))
print(urlparse('http://www.encar.com?test=test'))
