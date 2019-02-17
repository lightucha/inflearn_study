import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
'''
Rest:
- POST 서버로 보내는 것
- GET 서버에서 가져오는 것
- PUT(FETCH) 보내는 것 >> UPDATE, REPLACE (UPDATE, MODIFY)
- DELETE 삭제하는 것
>> POST / GET / DELETE 만 알아도 됩니다.
'''
payload1 = {'key1':'value1', 'key2':'value2'} # dict
payload2 = (('key1','value1'), ('key2','value2')) # tuple 도 가능하다.
payload3 = {'some':'nice'}

#r = requests.put('http://httpbin.org/user/delete', data = payload1) # URL만 봐도 무엇을 할지 알 수 있음
#print(r.text)

#r = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=payload1)
#print(r.text)

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text) # {} 삭제 되었다.

# 실습(과제)
# https://www.apistore.co.kr/main.do 의 REST API 이용하여 정보 txt로 저장 혹은 출력
