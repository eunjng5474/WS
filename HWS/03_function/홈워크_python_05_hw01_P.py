# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

year = int(input())
month = int(input())
day = int(input())

print(calendar.calendar(year))

# if calendar.isleap(year) == True:
#     print('윤년입니다. 연도를 다시 입력해주세요.')
#     year = int(input())
# else:
#     print(calendar.calendar(year))