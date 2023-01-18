# 입력을 2번 받는다.
# 하나하나 쓰는 것은 스마트하지 못해...
# 변수를 선언하는 행위를 마치 몰상식한 것처럼 생각하는 경우가 있는데
# 안됩니다....
# num1 = input() # input 함수의 실행 결과를 num1에 할당한다.
# num2 = input() # 사용자가 입력한 값을 문자열로 반환한다.

# print(int('1234') + int('5678'))
# print(int(num1) + int(num2))

# {key: value}
# key에 들어갈 수 있는 값은 immutable (불변형) -> string
# value에 들어갈 수 있는 값은? -> 상관 없음
menu = {'김치찌개': 10000, '라면': 20000}

# 평균 구하기 : 평균(모든 값의 합을 모든 값의 길이만큼 나눈 값)
# sum_value = menu['김치찌개'] + menu['라면']
# while 조건 (종료될 조건) : 언제 끝나야 할지 알 수 없다.
result = 0 
count = 0
for some_value in menu:
    print(menu[some_value]) # 이렇게 출력만하고 사라지면 안된다.. 저장...해야한다...
    # dust = menu[some_value] # 얘도 반복하면서 실행이 된다...
    result = result + menu[some_value]
    count = count + 1
print(result//count)


