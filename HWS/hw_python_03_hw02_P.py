year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # 4의 배수이면서 100의 배수가 아니거나
    # 400의 배수이면
    print('윤년입니다.')
else:
    print('윤년이 아닙니다.')