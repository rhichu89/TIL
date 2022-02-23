# section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MINE - text/csv

import csv

# 에제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 하나의 행을 스킵(Header를 스킵할때 사용) 

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) # 타입에 __iter__ 이 있으면 반복문 사용 가능
    print()

    for c in reader:
        print(c)   

print()



# 에제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|') # 구분자가 , 이 아닐경우 설정해 주어야 함

    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader)) # 타입에 __iter__ 이 있으면 반복문 사용 가능
    print()

    for c in reader:
        print(c)   

print()


# 예제3 (Dict변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('------')


# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./resource/sampe3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)



# 예제5
with open('./resource/sampe4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)


# XSL, XLSX
# openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname = '시트명' 또는 숫자, header=숫자, skiprow = 5
xlsx = pd.read_excel('./resource/sample.xlsx', skiprows=5)

# 상위 데이터 확인
print(xlsx.head())

print()

# 데이터 확인
print(xlsx.tail())

print(xlsx.shape) # 행, 열


# 엑셀 or CSV 다시 쓰기

xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.xlsx', index=False)