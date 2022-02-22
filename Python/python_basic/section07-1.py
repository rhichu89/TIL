# Section07-01
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수


# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도 존재, 인스턴스 생성 후 사용


# 선언
# class 클래스명:
#     속성, 메소드


# 예제 1 


class UserInfo:
    # 속성 , 메소드
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스
user1 = UserInfo("Python")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)



# 예제 2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called!')
    def function2(self):
        print('function2 called!')

self_test = SelfTest()
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)


# 예제 3
# 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) # nameSpace에 없으면 Class nameSpace에 가서 찾음
print(user2.stock_num)
print(user3.stock_num)

print()
del user1

print(user2.stock_num)
print(user3.stock_num)