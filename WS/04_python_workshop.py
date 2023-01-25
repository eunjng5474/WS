# # 1
# N = int(input())
# N_list = []
# for i in range(1, N+1):
#     if N % i == 0:      # 만약 N/i의 나머지가 0이라면(i는 N의 약수)
#         N_list.append(i)    # i를 리스트에 추가
# print(*N_list, end=' ')     # 리스트 채로 출력하는 것이 아니라 내부 값만 추출하기 위해 *List



# # 2
# def list_sum(li):
#     sum_ = 0
#     for i in range(len(li)):
#         sum_ += int(li[i])
#     return sum_

# print(list_sum([1, 2, 3, 4, 5]))



# # 3
# def dict_list_sum(li):
#     age_sum = 0
#     for i in range(len(li)):
#         age_sum += li[i]['age']
#     return age_sum

# print(dict_list_sum([{'name': 'kim', 'age': 12},
#                     {'name': 'lee', 'age': 4}]))



# # 4
# def all_list_sum(li):
#     all_sum = 0
#     for i in range(len(li)):
#         for j in range(len(li[i])):
#             all_sum += li[i][j]
#     return all_sum

# print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))



# # 5
# def get_secret_word(li):
#     ascii = ''              # 문자열로 값을 반환하기 위해 빈 문자열 할당
#     for i in range(len(li)):
#         ascii += chr(li[i])     # 문자열에 각 숫자에 해당하는 아스키 문자 추가
#     return ascii

# print(get_secret_word([83, 115, 65, 102, 89]))



# # 6
# def get_secret_number(s_str):
#     asc_n = 0                   # 아스키 숫자를 더하기 위해 초기값 0 할당
#     for i in range(len(s_str)):
#         asc_n += ord(s_str[i])      # 입력한 문자열의 길이만큼 해당 문자열을 아스키 숫자로 변환하여 asc_n에 더하기
#     return asc_n

# print(get_secret_number('happy'))



# 7
def get_strong_word(a, b):
    asc_a = 0
    asc_b = 0 
    for i in range(len(a)):
        asc_a += ord(a[i])
    for j in range(len(b)):
        asc_b += ord(b[j])  
    # asc_a = ord(a)
    # asc_b = ord(b)
    if asc_a > asc_b:
        return a
    elif asc_a < asc_b:
        return b
    else:
        return a, b

print(get_strong_word('z', 'a'))
print(get_strong_word('delilah', 'dixon5'))
print(get_strong_word('delilah', 'cflilah'))
