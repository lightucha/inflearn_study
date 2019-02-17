import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

'''
r = requests.get('https://api.github.com/events')
r.raise_for_status() # 예외를 발생시켜 주는 것
print(r.text)
'''
jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain = 'httpbin.org', path='/cookies') # 유지보수를 위해서 더 좋음

'''
r = requests.get('http://httpbin.org/cookies', cookies=jar)
r.raise_for_status()
print(r.text)
'''

#r = requests.get('https://github.com', timeout=5) # 서버가 반응할 때까지 대기
#print(r.text)

#r = requests.post('http://httpbin.org/post', data = {'name':'kim'}, cookies=jar)
#print(r.text) # post에 대한 요청이 잘 전달 됐다.

payload1 = {'key1':'value1', 'key2':'value2'} # dict
payload2 = (('key1','value1'), ('key2','value2')) # tuple 도 가능하다.
payload3 = {'some':'nice'}

#r = requests.post('http://httpbin.org/post', data = payload1) # form
#print(r.text)

r = requests.post('http://httpbin.org/post', data = json.dumps(payload3)) # json
print(r.text)
