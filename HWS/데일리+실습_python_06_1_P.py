# 주민등록번호 앞의 6자리는 생년월일이고, 뒤 7자리는 성별, 지역, 오류검출코드이다. 
# 주민등록번호를 입력받아 주민등록번호 뒷자리를 비식별화하는 함수 de_identify 를 만들어라.


# def de_identify(number):
#     # num = number.replace(number[-7:-1], '*')
#     # return num
#     # num = number.strip('-')
#     # num = num.replace(num[-7], '*', 7)
#     # return num
#     for n in range(-7, 0):
#         num = number.replace(number[n], '*')
#     return num
#     #     # print(number[-n])
#     # return 




############# sol
# 해당 변수는 인자를 하나만 받는다.
# 함수 정의시 매개변수는 한 개면 된다.
def de_identify(string):
    # 문자열을 받아온 다음, 그 문자열이 가진 내용 중
    # '-'에 해당하는 부분을 없앨 것이다.
    # 반복문을 통해서 넘겨받은 문자열을 하나하나 비교한 뒤,
    # 특정 문자열을 제외한 문자열을 만들어서 반환해야 한다.
    result = ''
    # for char in string:
    #     if char == '-':
    #         continue
    #     else:
    #         result += char
    result = string.replace('-', '')     # 문자열이 가진 특성상 원본을 바꿀 수는 없으니 변경된 값을 반환
    
    # print(result[:6] + '*'*7)     # '970103*******'   # 이런식으로도 가능
    
    result = list(result)
    result[6:] = ['*']*7
    return ''.join(result)
    # print(result)
    # real_result = ''
    # idx = 0
    # for char in result:
    #     idx += 1
    #     if idx >= 6:
    #         real_result += '*'
    #     else:
    #         real_result += char
    #     idx += 1






# A. 입력예시
print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 
