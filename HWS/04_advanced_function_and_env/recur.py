# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4)) # 24


# def sum(n):
#     if n == 5:
#         return True
#     else:
#         sum(n+1)
# print(sum(0))   # None

# n == 5일 때 sum(n+1)에 True 반환했지만 저장 안 함 -> True 값 사라짐
# 반환하고 함수 끝(return)
# n == 4, 3, ...일 때 None 반환


def sum(n):
    if n == 5:
        return True
    else:
        return sum(n+1) 
print(sum(5))   # True




################# TRY

def fn_d(n):
    # 최종 결과값
    result = n  #result를 n으로 설정해놓고 나머지들을 더해나감
    while n != 0:
        result += n % 10   # 4, 3, 2, 1
        n = n // 10
    return result
print(fn_d(91))

# -> 재귀함수로 만들어보기
