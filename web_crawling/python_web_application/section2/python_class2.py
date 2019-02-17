import sys
import io

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print('function1 called!')

    def function2(self):
        print(id(self))
        print('function2 called!')

f = SelfTest()
print(dir(f))

#f.function1()
# 메소드(함수)를 정의할 때 매개변수를 지정하지 않았는데,
# Error message는 하나의 인자가 넘어왔다고 쓰여져 있음

#f.function2()
# 정상 실행된다

print(id(f)) # 2646736681728; 메모리 주소
f.function2() # 2646736681728
# 주소값이 일치하는 것을 확인 할 수 있음
# 인스턴스의 주소값이 self에 담겨서 넘어감을 알 수 있음

print(SelfTest.function1()) # 클래스의 네임스페이스에 직접 접근하면 실행
# 클래스를 인스턴스화 하지 않았기 때문에 self의 주소값을 받지 않아도 됨
