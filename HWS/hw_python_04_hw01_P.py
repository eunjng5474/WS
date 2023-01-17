# 끝말잇기 단어의 리스트가 주어졌을 때, 몇 번째 사람이 탈락하는지 확인하는 코드를 작성하시오.
# 조건
    # 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
    # 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우, 지게 됩니다.

words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]


for i in range(1, len(words)): # 첫번째 사람이 탈락하지 않게 하기 위해 1부터 len(words)까지
    if words[i][0] != words[i-1][-1]:   # 만약 i번째 값의 첫글자 != (i-1)번째 값의 마지막 글자 라면
        print(f'{i +1}번째 사람이 탈락입니다')  # i번째 사람 탈락(텍스트로는 1번째부터 시작하기 위해 i+1)
    elif words[i] in words[:i]:         # 만약 i번째 값이 그 전까지 값들 중 이미 등장했던 단어라면 탈락
        print(f'{i +1}번째 사람이 탈락입니다')
# 5번째 사람이 탈락입니다.




# sol 2

# length = 0
# for i in words:
#     print(length)
#     print(words[length][-1] == words[length + 1][0])
#     length += 1

# words[0][-1] == words[1][0]
# words[1][-1] == words[2][0]
# words[2][-1] == words[3][0]


# 처음부터 words의 길이보다 1 작은 위치를 조회할 때까지 반복
duplicated_word = []
idx = 0
while idx < len(words) -1:
    if words[idx][-1] == words[idx + 1][0] and words[idx] not in duplicated_word:
        duplicated_word += [words[idx]]
    else:
        print(f'{idx+1}번째가 탈락했습니다.')
        break
    idx += 1
print(duplicated_word)