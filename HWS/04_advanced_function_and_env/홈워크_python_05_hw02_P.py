# fn_d(91) 
# 출력 예시 
# 101


# ## 1
# def fn_d(n):
#     n = str(n)
#     sum_n = 0
#     for i in range(len(n)):
#         sum_n += int(n[i])
#     sum_n += int(n)
#     return sum_n

# # print(fn_d(3))


# ## 2
# list_n = []
# for i in range(1, 10000):
#     list_n.append(fn_d(i))

# def is_selfnumber(n):
#     if n in list_n:
#         return '셀프넘버가 아닙니다.'
#     else:
#         return '셀프넘버입니다.'
        
# # print(is_selfnumber(25))





### sol 2

# 1234를 언제까지? 모든 자릿수를 다 계산할 때까지
# 1234 % 10 = 4 : 1234 // 10 = 123   
# 123 % 10 = 3  : 123 // 10 = 12
# 12 % 10 = 2   : 12 // 10 = 1
# 1 % 10 = 1    : 1 // 10 = 0   -> 종료조건
# 종료조건이 명확하고, 똑같은 작업을 반복 -> while문
def fn_d(n):
    # 최종 결과값
    result = n  #result를 n으로 설정해놓고 나머지들을 더해나감
    while n != 0:
        result += n % 10   # 4, 3, 2, 1
        n = n // 10
    return result
print(fn_d(91))


def is_selfnumber(m):
    # m의 제네레이터가 될 수 있는 경우는
    # 1부터 m까지의 숫자 중에 있다
    for i in range(1, m+1):
        # 제네레이터인지 아닌지 판별하는 방법은
        # 숫자 i를 fn_d에 집어 넣었을 때,
        # 그 값이 내가 할당받은 m과 동일하다면,
        # i를 m의 제네레이터라고 할 수 있다.
        if fn_d(i) == m:    # fn_d(91) == 101 : 91은 101의 제네레이터
            # 하나라도 제네레이터가 있으면?
            # 셀프넘버가 아니므로 셀프넘버를 판별하는 함수
            # is_selfnumber 함수는 False를 반환하고 종료
            return False
    
    # 모든 후보군을 모두 출력했는데 False가 반환되지 않았다면
    # 셀프 넘버가 맞다.
    return True
print(is_selfnumber(101))   # False
print(is_selfnumber(31))    # True


# for i in range(1, m+1):
#   if fn_d(i) == m:
#       return False
#   else:
#       return True
# 이렇게 해도 같은 결과 나오는 상황 있음
# 하지만 한 번도 False가 아니어야 True여야 하므로 이렇게는 x


def is_selfnumber(M):
    for i in range(1, M+1):
        # lambda [parameter] : expression
        # 모든 자릿수의 합 + 본인을 더한 값
        # while 나머지를 사용해서 더해왔는데
        # 문자열로 바꿔서 각 자리수를 순회하며 더하기
        # '1234' -> '1', '2', '3', '4'
        # [int(char) for char in 'M'] => [1, 2, 3, 4] +[M]
        # => sum([1, 2, 3, 4, M])
        fn_d = lambda n: sum([int(char) for char in str(n)] + [n])
        if fn_d(i) == M:
            return False
    return True