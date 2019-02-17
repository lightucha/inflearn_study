import sys
import io

# base line
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

'''
클래스는 필드(변수)와 메소드()로 이루어진다.
'''
class UserInfo:

    # 객체를 초기화 / 초기화 될 때 단 한 번만 실행
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    '''
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone
    '''

    def print_info(self):
        print("--------------")
        print('Name: ' + self.name)
        print('Phone: ' + self.phone)
        print("--------------")

    # 객체가 메모리에서 사라질 때 단 한번 실행
    def __del__(self):
        print('delete!')

# 인스턴스
user1 = UserInfo('kim', '010-9874-2123') # UserInfo라는 클래스를 재사용
user2 = UserInfo('park', '010-1234-0988')

print(id(user1))
print(id(user2))

#user1.set_info('kim', '010-9874-2123')
#user2.set_info('park', '010-1234-0988')

user1.print_info()
user2.print_info()

print(user1.__dict__) # 인스턴스화 된 네임스페이스
print(user2.__dict__)

print(user1.phone, user2.name) # 메모리에 올라가 있기 때문에 바로 접근 가능
