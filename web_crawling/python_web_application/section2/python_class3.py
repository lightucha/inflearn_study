import sys
import io

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 클래스 변수 vs. 인스턴스 변수

class Warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('kim')
user2 = Warehouse('park')

print(user1.name)
print(user2.name)

# 네임스페이스 확인
print(user1.__dict__)
print(user2.__dict__)
# stock_num 이 존재하지 않음

print(Warehouse.__dict__)
# stock_num = 2
# user1, user2 인스턴스를 생성할 때, 생성자에 의해서 +1씩 증가 된 것

print(user1.stock_num)
print(user2.stock_num)
# stock_num 이 자신(인스턴스)의 네임스페이스에 없기 때문에
# 클래스의 네임스페이스로 올라가서 호출 and 공유가 됨
# 즉, 인스턴스 네임스페이스 -> 클래스 네임스페이스 -> 그래도 없으면. Error가 날 것
# 클래스 변수는 공유가 된다 !!
