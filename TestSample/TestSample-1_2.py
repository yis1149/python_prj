


def is_multiple_of_10(num):
    return num % 10 == 0


i = 0

while i <= 100: # while 1, while True 사용시 break 없으면 무한루프
    
    i += 1

    if is_multiple_of_10(i) and i>1:
        print(str(i) + " 는 10의 배수")
        print("I 의 나머지 : " + str(i%10))
    else:
        print(str(i) + " 는 10의 배수가 아닙니다.")
        print("I 의 나머지 : " + str(i%10))

        



