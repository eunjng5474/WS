# 끝말잇기 단어의 리스트가 주어졌을 때, 
# 몇 번째 사람이 탈락하는지 확인하는 코드를 작성하시오.
# 조건
    # 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
    # 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우, 지게 됩니다.



# lenth = 0
# for i in words:
#     print(words[lenth][-1] == words[lenth + 1][0])
#     lenth += 1

# words[0][-1] == words[1][0]
# words[1][-1] == words[2][0]
# words[2][-1] == words[3][0]

# 처음부터 words의 길이보다 1 작은 위치를 조회 할 때까지 반복
words = ["round" , "dream", 
"magnet" , "tweet" , "tweet", 
"trick", "kiwi"]
duplicated_word = []
idx = 0
while idx < len(words) - 1:
    # print(words[idx], words[idx+1])
    # print(duplicated_word)
    if words[idx][-1] == words[idx + 1][0] and words[idx] not in duplicated_word:
        duplicated_word += [words[idx]]
    else:
        print(f'{idx+1}번째가 탈락했습니다.')
        break
    idx += 1
print(duplicated_word)