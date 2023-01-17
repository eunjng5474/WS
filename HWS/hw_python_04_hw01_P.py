words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]


for i in range(1, len(words)): # 첫번째 사람이 탈락하지 않게 하기 위해 1부터 len(words)까지
    if words[i][0] != words[i-1][-1]:   # 만약 i번째 값의 첫글자 != (i-1)번째 값의 마지막 글자 라면
        print(f'{i +1}번째 사람이 탈락입니다')  # i번째 사람 탈락(텍스트로는 1부터 시작하기 위해 i+1)
    elif words[i] in words[:i]:         # 만약 i번째 값이 그 전까지 값들 중 이미 등장했던 단어라면 탈락
        print(f'{i +1}번째 사람이 탈락입니다')
        