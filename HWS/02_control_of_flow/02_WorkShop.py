# 1. 숫자의 입력과 출력
num1 = int(input())
num2 = int(input())
print(num1 + num2)

# 2. Dictionary를 활용하여 평균 구하기
lunch = {'버터바지락찜파스타' : 8000, '잡채밥' : 7000, '차돌김치찌개' : 6000, '라면' : 5000}
price_m = (sum(lunch.values()) / len(lunch))    # dict내의 value를 모두 더하고 dict의 길이로 나눠서 평균 구하기
print(price_m)