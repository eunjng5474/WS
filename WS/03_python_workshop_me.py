# name_list = ['신동민', '서재현', '박영서', '이태성', '정예원', '이은석']
# age_list = [17, 18, 22, 24, 25, 19]

# for each in zip(name_list, age_list):
#     print(each)


# # 1
# number = int(input())
# for i in range(1, number+1):
#     print(i)


# # 2
# number = int(input())
# for i in range(1, number+1):
#     print(i, end=' ')


# # 3
# number = int(input())
# for i in range(number, -1, -1):
#     print(i)


# # 4
# number = int(input())
# for i in range(number, -1, -1):
#     print(i, end=' ')


# # 5
# sum_i = 0
# number = int(input())
# for i in range(1, number + 1):
#     sum_i += i
# print(sum_i)


# # 6
# number = int(input())
# for i in range(1, number+1):
#     print(' '*(number - i), '*'*i)


# 7
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
]
numbers.sort()
n = len(numbers)//2
med = numbers[n]
print(med)