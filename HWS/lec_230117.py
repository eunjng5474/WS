num = int(input())
if num % 2 == 1:
    # if num % 2: 가능
    print("홀수")
else:
    print("짝수")



for num in range(10):
    if num == 5:
        continue
    print(num)