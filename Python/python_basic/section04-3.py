# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서 O, 중복 O, 수정 O, 삭제 O )

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Bnana', 'Orange']]\

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])


#슬라이싱
print(d[0:3])
print(e[2][1:3])


# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')


# 리스트 수정, 삭제
# 삭제 : del, remove, pop
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)

del c[-1]
print(c)


# 리스트 함수
y = [5, 2, 3, 1, 5]
print(y)

y.append(6)
print(y)

y.sort()
print(y)

y.reverse()
print(y)

y.insert(2,7)
print(y)

# del = 인덱스 번호를 사용하여 제거
# remove = 값을 찾아서 제거 
y.remove(2)
print(y)

y.pop()
print(y)

# extend는 값이 들어감
ex = [88,77]
y.extend(ex)
print(y)

# append는 자체가 들어감
ex2 = [88,77]
y.append(ex2)
print(y)



# 튜플 (순서 O, 중복 O, 수정 X, 삭제 X)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][2])
print(d[2 : ])
print(d[2][0:2])

print(c + d)
print(c * 3)
print()


# 튜플 함수

z = (5, 2, 1, 3, 1)

print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))