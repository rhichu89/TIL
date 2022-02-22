# Section04-1
# 데이터 타입

v_str1 = "Niceman"
v_blol = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_lsit = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8 , 9}



print(type(v_str1))
print(type(v_blol))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_lsit))
print(type(v_tuple))
print(type(v_set))

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10.
result2 = a + b
print(result2)

#형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))


# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7))
n, m = divmod(100, 8)
print(n , m)



import math

print(math.ceil(5.1))
print(math.floor(3.7))