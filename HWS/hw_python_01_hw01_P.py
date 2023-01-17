score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithm'] = 90 # 항목 추가
score['python'] = 85 # 값 재할당
score.update({'python': 85})
# dict의 update 함수는 한 번에 여러 개의 값을 수정할 수 있다.
# score.update({'python': 85, 'django': 90})


# 1. score가 가진 모든 값을 순회
# 2. 그 값들을 어떤 변수에 계속 더해 총합을 구한다.
# 3. score의 전체 길이를 구해 나눈다.
    # 3-1. 순회시마다 1씩 커지는 변수

total = 0
lenth = 0
# dic 순회시에는 key를 순회한다.
for key in score:
    print(score[key]) # score['python']
    total = total + score[key] 
    lenth = lenth + 1
# 모든 순회가 다 끝나고 난 뒤,
print(total / lenth)

print(sum(score.values()) / len(score.values()))