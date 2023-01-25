# 주민등록번호 앞의 6자리는 생년월일이고, 뒤 7자리는 성별, 지역, 오류검출코드이다. 
# 주민등록번호를 입력받아 주민등록번호 뒷자리를 비식별화하는 함수 de_identify 를 만들어라.


def de_identify(number):
    # num = number.replace(number[-7:-1], '*')
    # return num
    # num = number.strip('-')
    # num = num.replace(num[-7], '*', 7)
    # return num
    for n in range(-7, 0):
        num = number.replace(number[n], '*')
    return num
    #     # print(number[-n])
    # return 

# A. 입력예시
print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

