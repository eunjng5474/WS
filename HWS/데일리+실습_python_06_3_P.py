
def count_vowels(string):
    cnt = 0         # 초기값
    for str in string:      # string의 모든 글자를 순회하면서
        if str in ['a', 'e', 'i', 'o', 'u']:    # str이 모음 리스트 안에 있다면
            cnt += 1    # cnt + 1
    return cnt


print(count_vowels('apple')) # 2
print(count_vowels('banana')) # 3




## sol 2
def count_vowels(words):
    vowels = 'aeiou'
    result = 0

    for vowel in vowels:
        for char in words:
            if char == vowel:
                result += 1
    return result


## sol 3
def count_vowels(words):
    vowels = 'aeiou'
    result = 0

    for vowel in vowels:
        result += words.count(vowel)
    return result