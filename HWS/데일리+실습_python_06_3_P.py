
def count_vowels(string):
    cnt = 0         # 초기값
    for str in string:      # string의 모든 글자를 순회하면서
        if str in ['a', 'e', 'i', 'o', 'u']:    # str이 모음 리스트 안에 있다면
            cnt += 1    # cnt + 1
    return cnt


print(count_vowels('apple')) # 2
print(count_vowels('banana')) # 3
