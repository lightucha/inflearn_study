import sys
import io

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NameTest:
    total = 0

print(dir()) # NameTest 클래스가 포함되어 있음을 알 수 있다
print('before: ', NameTest.__dict__)
NameTest.total = 1
print('after: ', NameTest.__dict__)

n1 = NameTest()
n2 = NameTest()
print(id(n1), ' vs ', id(n2))
print(dir()) # n1, n2 가 포함
print(n1.__dict__)
print(n2.__dict__) # 자기 자신의 값을 가지고 있지 않기 때문에 아무것도 출력되지 않는다

n1.total = 77
print(n1.__dict__)

print(n1.total)
print(n2.total) # 인스턴스 네임스페이스에 없어서 클래스 네임스페이스 값을 가져옴
print(n1.next) # 인스턴스 네임스페이스 -> 클래스 네임스페이스 -> 에러
