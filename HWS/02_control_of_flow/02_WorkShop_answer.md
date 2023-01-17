# WorkShop

### 숫자의 입력과 출력

- 입력 받은 데이터를 숫자로 변환하고 덧셈해서 출력하는 프로그램을 작성하시오.
  (힌트 : input() 함수를 활용하여 데이터를 입력받을 수 있다.)

```markdown
[입력]
숫자를 2번 입력받는다.
[출력]
입력 숫자를 계산하여 값을 출력한다.
[입력 예시]
6374
8729
[출력 예시]
15103
```

```python
num1 = int(input()) # 6374
num2 = int(input()) # 8729 
print(num1 + num2)  # 15103
print(int(num1) + int(num2))
```

### Dictionary를 활용하여 평균 구하기

좋아하는 점심메뉴를 이용하여 key는 메뉴, value는 가격인 dictionary를 만들고,
점심메뉴의 평균 값을 출력하시오.

```python
lunch = {'버터바지락찜파스타' : 8000, '잡채밥' : 7000, '차돌김치찌개' : 6000, '라면' : 5000}
price_m = (sum(lunch.values()) / len(lunch))    
# dict내의 value를 모두 더하고 dict의 길이로 나눠서 평균 구하기
print(price_m) # 6500
```

```python
# {key: value}
# key에 들어갈 수 있는 값은 immutable(불변형) -> string
# value에 들어갈 수 있는 값은? -> 상관 없음
menu = {'김치찌개': 10000, '라면': 20000}

# 평균 구하기: 평균(모든 값의 합을 모든 값의 길이만큼 나눈 값)
# sum_value = menu['김치찌개'] + menu['라면']
# while 조건 (종료될 조건) : 언제 끝나야 하는지 알 수 없다.
result = 0
for some_value in menu:
  print(menu[some_value]) # 이렇게 출력만 하고 사라지면 안 됨. 저장해야함
  # dust = menu[some_value]
  answer = result + menu[some_value]
  count = count + 1
print(result//count)

# menu[10000] 으로는 key값 찾을 수 없음. 변할 수 있는 값이기 때문
```
