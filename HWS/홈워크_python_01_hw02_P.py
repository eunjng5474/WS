# 사용자가 입력한 각 자릿수를 더해 출력하는 코드를 작성하라.

s = input('숫자를 입력해주세요 : ')     # 1234
sum_s = 0
for i in range(len(s)):     # 입력받은 문자열의 모든 자릿수 순회 
    sum_s += int(s[i])      # 입력받은 문자열의 각 자릿수를 int로 변환하여 sun_s에 더하기
print(sum_s)                # 10
