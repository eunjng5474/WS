entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']


entry_dict = {}
n_list = []
for name in entry_record:
    if name not in entry_dict:
        entry_dict[name] = 1
    else:
        entry_dict[name] += 1
# # for i in range(len(entry_dict)):
#     # n_list.append(entry_dict[i][name])
# # print(entry_dict[name])
# # n_list.append(entry_dict[name])
# # print(n_list)



print('입장 기록 많은 TOP3')
print(*sorted(entry_dict.items(),
            key=lambda item: item[1],
            reverse= True
            )[:3])

exit_count_dict = {name: 0 for name in set(exit_record)}
# print(exit_count_dict)
for name in exit_record:
    exit_count_dict[name] += 1
# print(exit_count_dict)

print('출입 기록이 수상한 사람')
for name, count in entry_dict.items():
    # print(name, count)
    # print(name, exit_count_dict[name])
    diff = count - exit_count_dict[name]
    # print(diff)
    if diff > 0:
        print(f'{name}은 입장 기록이 {diff}회 더 많아 수상합니다.')
    elif diff < 0:
        print(f'{name}은 퇴장 기록이 {-diff}회 더 많아 수상합니다.')




# # print(entry_dict)
# # # new_dict = sorted(entry_dict.items(), key = lambda item: item[1], reverse=True)
# # # # print(new_dict)

# # # print('입장 기록 많은 Top3')
# # # for i in range(3):
# # #     print(f'{new_dict[i]} {new_dict[i][name]}회')






# ## sol 2
# # entry_record에 등장한 횟수를 각 사람마다 기록
# # -> 각각 고유한 사람마다 특정한 value를 가지고 있어야 한다
# entry_count_dict = {}
# for name in entry_record:
#     # entry_count_dict.setdefault(name, 0) + 1
#     entry_count_dict[name] = entry_count_dict.get(name, 0) + 1
# # print(entry_count_dict)

# print('입장 기록 많은 TOP3')
# print(*sorted(entry_count_dict.items(),
#             key=lambda item: item[1],
#             reverse= True
#             )[:3])

# exit_count_dict = {name: 0 for name in set(exit_record)}
# # print(exit_count_dict)
# for name in exit_record:
#     exit_count_dict[name] += 1
# # print(exit_count_dict)

# print('출입 기록이 수상한 사람')
# for name, count in entry_count_dict.items():
#     # print(name, count)
#     # print(name, exit_count_dict[name])
#     diff = count - exit_count_dict[name]
#     # print(diff)
#     if diff > 0:
#         print(f'{name}은 입장 기록이 {diff}회 더 많아 수상합니다.')
#     elif diff < 0:
#         print(f'{name}은 퇴장 기록이 {-diff}회 더 많아 수상합니다.')
        




### sol 3
from collections import Counter

a = Counter(entry_record)
b = Counter(exit_record)

print(a, b)
a.subtract(b)
print(a)