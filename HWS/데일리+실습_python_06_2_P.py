# 작물과 가격이 함께 있는 리스트가 존재할 때, 
# 가장 높은 가격을 가지고 있는 작물의 이름을 출력하라. 
# 단, 작물의 이름을 직접 입력하여 출력하지 않는다.

grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]


# max_p = 0
# for i in range(len(grain_lst)):
#     if grain_lst[i][-1] > max_p:
#         max_p = grain_lst[i][-1]
        
    

# #################### sol 
# # print(grain_lst.sort()) # None 반환
# # print(grain_lst) # 정렬된 리스트 확인
# grain_dict = dict(grain_lst)
# key = list(grain_dict.keys())
# value = list(grain_dict.values())
# # print(key, value)
# # print(value.index(4500))
# # print(value.index(max(value))) # 2
# max_idx = value.index(max(value))
# print(key[max_idx])



# 2
grain_lst.sort(key=lambda x : x[1])
print(grain_lst[-1][0])

grain_lst.sort(key=lambda x : x[1], reverse=True)
print(grain_lst[0][0])