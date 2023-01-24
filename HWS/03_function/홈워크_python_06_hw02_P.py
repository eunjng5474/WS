# 문자열 배열을 받아 애너그램 단위로 그룹핑하는 함수 group_anagrams을 작성하여라.

# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 



# input_list = input().split()
# for i in range(len(input_list)):
#     for j in range(len(input_list[i])):
#         print(i, j)


# words = ['eat','tea','tan','ate','nat','bat']
# # print(words[1])
# word_list = []
# word_list_sort = []
# anagram_list = []
# for i in range(len(words)):
#     word_sub_list = []      
#     for j in range(len(words[i])):
#         word_sub_list.append(words[i][j])
#     word_list.append(word_sub_list)
#     word_list_sort.append(sorted(word_list[i]))
# # print(word_list_sort)
# # print(word_list_sort[1] == word_list_sort[0])
#     if word_list_sort[i] == word_list_sort[:i-1]:
#         anagram_list.append(words[i])
# print(anagram_list)

    # if word_list[i]
# print(word_sub_list)
# print(word_list)


# anagrams_list = []
# word_list
# for n in range(len(word_list)):
#     for m in range(len(word_list[n])):
#         if word_list[n][m] in
            



# def group_anagrams(words):
#     word_dict = {}
#     for word in words:
#         wor





# 222
# 애너그램이란, 일종의 말장난으로 어떠한 단어의 문자를 재배열하여 
# 다른 뜻을 가지는 다른 단어로 바꾸는 것을 말한다.
# 애너그램이 형성되는 단어들끼리 묶어서 출력하시오.

words = ['eat','tea','tan','ate','nat','bat', 'haha', 'aahh']
# 애너그램이 형성되는지 안되는지를 판단하기 위한 가장 간단한 방법은 아래와 같다.
# eat과 tea를 예로 들자면,
# eat과 tea는 모두 아래와 같은 단어 구성을 가진다.
# 아래와 같은 형태를 만들기 위해, 각 알파벳의 개수가 몇개인지 세고, 이를 담아둘 dict를 생성한다.
# e : 1개
# a : 1개
# t : 1개 
    # 위 과정을 모든 단어에 대해 실행하고,
    # 모든 단어의 정보를 담아둔 dict를 생성한다
    # 이때, dict로 생성하는 이유는,
    # {'eat' : {'e': 1, 'a': 1, 't': 1}} 과 같이
    # 어느 단어의 정보인지를 확인하기 위해서이다.



def group_anagrams(words):
    # 단어를 수집할 딕셔너리 생성
    word_dict = {}
    # 넘겨받은 모든 단어들을 순회
    for word in words:
        # 현재 조사할 word의 정보를 저장할 dict 생성
        sub_dict = {}
        # 각 단어를 알파벳 기준으로 순회
        for char in word:
            # 만약 순회중인 알파벳이 현재 단어 정보 dict에 이미 있다면
            if char in sub_dict:
                # 해당 알파벳의 개수를 1 증가
                sub_dict[char] += 1
            else:
                # 아니면, sub_dictt에 해당 알파벳을 키로 하는 새로운 값 할당
                # 최초 할당시 1을 할당하는 이유는
                # 지금 처음으로 1개가 발견되었기 때문에 처음부터 1을 할당
                sub_dict[char] = 1
        # word에 대한 조사가 끝나면 단어 수집할 dict에
        # word를 키로하는 단어 정보 dict : sub_dict을 할당
        word_dict[word] = sub_dict

    # 애너그램이 형성되는 단어들끼리 그룹핑할 리스트 생성
    anagram = []
    # 다시 모든 단어들을 순회
    # word_dict의 key로 사용할 예정
    for word in words:
        # anagram 리스트 안에서 또다른 리스트를 만들어 그룹필 할 예정이므로
        # anagram이 가진 모든 리스트 항목을 순회한다
        # 단, 최초 순회시에는 anagram 리스트가 비어있으므로
        # 반복문 내부 코드가 실행되지 않고,
        # break된적 없으므로 for else문이 실행,
        # 최초 순회하는 word를 삽입한다.
        for ana_list in anagram:
            # anagram의 요소들 중 하나인 ana_list에는 
            # word가 1개 이상 포함되어 있으므로 0번째 조회가능
            # 아나그램을 형성할 수 있는 대표 단어를 찾아 할당한다.
            ana_word = ana_list[0]
            # 대표단어 ana_word와 현재 순회중인 단어 word가 
            # 동일한 단어 정보(sub_dict)를 가지고 있다면, 둘은 아나그램이 형성가능하다.
            if word_dict[word] == word_dict[ana_word]:
                # 따라서 현재 순회중인 리스트에 
                # 현재 순회중인 단어를 삽입하고
                # break -> 그래야 for else문이 실행되지 않아, 새로운 그룹이 만들어지지 않는다.
                ana_list.append(word)
                break
        else:
            # word를 anagram에 삽입할 때, 그룹을 만들어야 하므로
            # 단어를 그대로 삽입하는 것이 아닌,
            # 리스트 형태로 삽입한다.
            anagram.append([word])
    return anagram        


print(group_anagrams(words))




# # ############
# # words = ['eat','tea','tan','ate','nat','bat']

# # word_dict = {}
# # for word in words:
# #     sub_dict = {}
# #     for char in word:
# #         if char in sub_dict:
# #             sub_dict[char] += 1
# #         else:
# #             sub_dict[char] = 1
# #     word_dict[word] = sub_dict

# # anagram = []
# # for word in words:
# #     for ana_list in anagram:
# #         ana_word = ana_list[0]
# #         if word_dict[word] == word_dict[ana_word]:
# #             ana_list.append(word)
# #             break
# #         else:
# #             anagram.append([word])