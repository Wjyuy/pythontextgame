# import random

# randomnum=random.randrange(1,100)
# life=5

# user_num=int(input("1-100사이 정수를 입력하세요 : "))
# while True:
#     if randomnum==user_num:
#         print("축하합니다! 랜덤 숫자는 %d였습니다"%randomnum)
#         break
#     elif randomnum>user_num:
#         print("%d 보다 큽니다.")
#         life -=1
#         print("목숨%d개 남음"%life)
#     elif randomnum<user_num:
#         print("%d 보다 큽니다.")
#         life -=1
#         print("목숨%d개 남음"%life)
# print("목숨이 다 닳았습니다! 랜덤 숫자는 %d였습니다"%randomnum)

import random
import os
number = random.randint(1, 1000)
tries = 0
n = 9 # 시도 횟수(n번까지 허용)

print("1~1000 사이의 숫자를 맞추세요.")

while tries <= n:
    guess = int(input("숫자를 입력하세요: "))
    tries += 1
    if number == guess:
        print("=========================")
        print("정답입니다!!! 시도 횟수는 %d회입니다." % tries)
        print("=========================\n")
        os.system("pause")
        break
    elif number < guess:
        print("더 작은 수를 입력하세요.\n=========================")
        print("기회가 %d번 남았습니다."%(n-tries+1))
    elif number > guess:
        print("더 큰 수를 입력하세요.\n=========================")
        print("기회가 %d번 남았습니다."%(n-tries+1))

if tries > n:
    print("=========================")
    print("주어진 기회를 모두 사용하셨습니다. 정답은 %d입니다." % number)
    print("=========================\n")
    os.system("pause")