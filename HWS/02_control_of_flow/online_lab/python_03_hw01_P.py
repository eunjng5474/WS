# 2월이 29일까지 있는 해를 윤년이라고 한다. 
# 어떤 해가 입력되면 그 해가 윤년인지 아닌지 판별하시오.
# 윤년 판단 조건
    # 해(year)가 4의 배수이면서 100의 배수가 아니면 윤년.
    # 400의 배수이면 윤년
    # 위 두 조건 중 하나라도 맞으면 윤년이다.
year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('윤년입니다.')
else:
    print('윤년이 아닙니다.')
