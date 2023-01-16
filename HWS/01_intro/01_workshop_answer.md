# Workshop

### 1. 문자 print
`It’s SSAFY 8` 을 출력하는 프로그램을 작성하시오. (중간에 작은따옴표가 있다 .)
```python
# 문자열 내부에 작은 따음표가 있어
# 큰 따옴표로 감싸 주었다.
print("It's SSAFY 9")

# escape sequence를 사용하여 작은 따옴표를 작성하였다.
print('It\'s SSAFY 9')
```


### 2. 숫자 print
`458345 + 623576` 를 계산하여 출력하는 프로그램을 작성하시오.
```python
# 바로 숫자값으로 입력
print(458345 + 623576)

# str으로 입력 받고 int로 변경
num1 = int(input())
num2 = int(input())
print(num1 + num2)
```


### 3. 변수를 사용해서 데이터 출력하기
두 변수 greeting, month를 사용해서 Hello July 를 출력하는 프로그램을 작성하시오.
```python
# 변수 greeting, month 
greeting = 'Hello'
month = 'July'
# f-strings 통해서 `Hello July` 출력
print(f'{greeting} {month}')
```



### 4. 문자형의 입력과 출력
입력 받은 문자를 출력하는 프로그램을 작성하시오.
(힌트 : `input()` 함수를 활용하여 데이터를 입력받을 수 있다.)

```python
# 입력 받은 문자를 hello로 설정하고 출력
hello = input()
print(f'{hello}')
```