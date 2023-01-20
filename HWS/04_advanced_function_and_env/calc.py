# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     try:
#         return a / b
#     except:
#         return "'0'으로는 나눌 수 없습니다."




## sol2

# 사칙연산을 각각 함수로 만들어라
# 더하기
def add(a, b):
    # 함수가 하는 가장 중요한 역할
    # code block 작성된 특정한 로직을 '호출시마다' 실행하는데 있다.
    # 만약 그 결과를 반환해야 한다면,
    # return 뒤에는 표현식이 올 수 있고, 반드시 하나의 객체만 반환해야 하는데,
    # 만약 2개 이상의 객체를 반환하려고 한다면? -> 튜플로 묶어서 반환
    return a + b

# 빼기
def sub(a, b):
    return a - b

# 곱하기
def mul(a, b):
    return a * b

# 나누기
# 단, 0으로 나눌 시 0으로는 나눌 수 없습니다. 라는 문자를 출력해야 한다.
def div(a, b):
    return a / b

# 함수 호출을 해보자.
# 정의한 함수 이름 + (인자)
# print(div(10, 0))   # print(10/0)

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")


try: 
    print(10/'ㅁ')
except ZeroDivisionError: 
    # except 뒤에 예외 상황 적지 않으면 모든 예외 상황에 아래 내용 출력
    print('0으로 나눌 수 없습니다.')
except TypeError:
    print('정수 이외의 값으로 나눌 수 없습니다.')
