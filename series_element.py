import pandas as pd

# 튜플을 시리즈로 변환 (인덱스 옵션 지정)
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)

print(sr[0])
print(sr['이름'])

print(sr[[1, 2]])
print('\n')
print(sr[['생년월일', '성별']])

print(sr[1:4])
print('\n')
print(sr['생년월일':'학생여부'])