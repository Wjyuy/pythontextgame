import random
import time
import sys
# import os

score=0
wc=0
lc=0
mc=0
money=10000
doublescore=0
maxwin=0
#1=승리 0=비김 -1=패배
def result(ucr,ccr):
    match ucr:
        case 1:
            if ccr==1:
                print("당신이 고른 것:가위")
                for i in range(2):
                    print(".")
                    time.sleep(1)
                print("컴퓨터가 고른 것: 가위!")
                time.sleep(1)
                return 0
            if ccr==2:
                print("당신이 고른 것:가위")
                for i in range(2):
                    print(".")
                    time.sleep(1)
                print("컴퓨터가 고른 것: 바위!")
                time.sleep(1)
                return -1
            if ccr==3:
                print("당신이 고른 것:가위")
                for i in range(2):
                    print(".")
                    time.sleep(1)
                print("컴퓨터가 고른 것: 보!")
                time.sleep(1)
                return 1     
            
        case 2:
            if ccr==1:
                print("당신이 고른 것:바위")
                for i in range(2):
                    print(".")
                    time.sleep(1)
                print("컴퓨터가 고른 것: 가위!")
                time.sleep(1)
                return 1
            if ccr==2:
                print("당신이 고른 것:바위")
                for i in range(2):
                    print(".")
                    time.sleep(1)
                print("컴퓨터가 고른 것: 바위!")
                time.sleep(1)
                return 0
            if ccr==3:
                print("당신이 고른 것:바위")
                for i in range(2):
                    print(".")
                    time.sleep(1)
                print("컴퓨터가 고른 것: 보!")
                time.sleep(1)
                return -1                
        case 3:
            if ccr==1:
                print("당신이 고른 것:보")
                for i in range(2):
                    print(".")
                    time.sleep(1)
                print("컴퓨터가 고른 것: 가위!")
                time.sleep(1)
                return -1
            if ccr==2:
                print("당신이 고른 것:보")
                for i in range(2):
                    print(".")
                    time.sleep(1)
                print("컴퓨터가 고른 것: 바위!")
                time.sleep(1)
                return 1
            if ccr==3:
                print("당신이 고른 것:보")
                for i in range(2):
                    print(".")
                    time.sleep(1)
                print("컴퓨터가 고른 것: 보!")
                time.sleep(1)
                return 0  
        case 4:
            sys.exit()        
            return 
        case _:  
            print("잘못된 입력입니다!") 
            return 2

def printdoubleresult(resultnum):
    if(resultnum==1):
        print("승리하였습니다!")
    if(resultnum==0):
        print("비겼습니다!")
    if(resultnum==-1):
        print("패배하였습니다!")

def printresult(resultnum):
    if(resultnum==1):
        return 1
    if(resultnum==0):
        return 2
    if(resultnum==-1):
        return 3

# def betting(hadmoney,betmoney):
#     if hadmoney<betmoney:
#         print("현재 보유중인 금액보다 큽니다!")
#         return 0
winsc=0
tries=1
# bet=0
gameresult=0
countnum=3
first=1
print("***가위 바위 보 게임 !!!***")
print("숫자 1,2,3을 이용해 컴퓨터와 가위바위보를 해보세요!")
print("최고 연승 기록은은 저장됩니다!!!\n")
while tries<1000:
    print("%d번째"%tries)
    # print("승리:%d 비김:%d 패배:%d 돈:%d"%(wc,mc,lc,money))
    if countnum==1:
        winsc+=1
        if maxwin<=winsc:
            maxwin=winsc
        if winsc>=5:
            print("*"*30)
            print("!!!!!현재 %d연승 중입니다!!!!!"%winsc)
            print("*"*30)
        else:
            print("현재 %d연승 중입니다!"%winsc)
        # print("현재 %d연승 중입니다!\ny:한번 더 대결해 승리할 시 %d배의 돈을 얻을 수 있습니다!\nn:아니면%d원을 바로 받으시겠습니까?"%(winsc-1,2*(winsc-1),bet*(2*(winsc-1))))
        # dbet=input("(y/n) : ")
        # if dbet=="y":
        #     print("한번더 진행")
        # elif dbet=="n":
        #     print("돈받기")
        #     money+=bet*(2*(winsc-1))
            # winsc=1
            # bet=0
            # countnum==3
            # try:
            #     # bet=int(input("\n베팅 금액을 입력하십시오! : "))
            # except:
            #     print("잘못된 입력입니다!")
            #     continue
            # resultbel=betting(money,bet)
            # if resultbel==0:
            #     continue
            # money-=bet
    elif countnum==2:
        winsc+=0
        if winsc>=5:
            print("*"*30)
            print("!!!!!현재 %d연승 중입니다!!!!!"%winsc)
            print("*"*30)
        else:
            print("현재 %d연승 중입니다!"%winsc)
        # print("현재 %d연승 중입니다!\ny:한번 더 대결해 승리할 시 %d배의 돈을 얻을 수 있습니다!\nn:아니면%d원을 바로 받으시겠습니까?"%(winsc-2,2*(winsc-2),bet))
        # dbet=input("(y/n) : ")
        # if dbet=="y":
        #     print("한번더 진행")
        # elif dbet=="n":
        #     print("돈받기")
        #     money+=bet
        #     winsc=1
        #     bet=0
        #     countnum==3
        #     try:
        #         bet=int(input("\n베팅 금액을 입력하십시오! : "))
        #     except:
        #         print("잘못된 입력입니다!")
        #         continue
        #     resultbel=betting(money,bet)
        #     if resultbel==0:
        #         continue
        #     money-=bet
    if countnum==3:
        winsc=0
        # if first==1:
        #     try:
        #         bet=int(input("\n베팅 금액을 입력하십시오! : "))
        #     except:
        #         print("잘못된 입력입니다!")
        #         continue
        #     resultbel=betting(money,bet)
        #     if resultbel==0:
        #         continue
        #     money-=bet
        #     first=0
        
        # elif first==0:
        #     if money<=0:
        #         print("!당신은 돈을 전부 탕진하였습니다! ")
        #         time.sleep(1)
        #         print("당신의 시도 횟수는 %d 번입니다."%tries-1)
        #         time.sleep(1)
        #         print("="*50)
        #         time.sleep(3)
        #         os.system("pause")
        #         break
            
            # try:
            #     bet=int(input("\n베팅 금액을 입력하십시오! : "))
            # except:
            #     print("잘못된 입력입니다!")
            #     continue
            # resultbel=betting(money,bet)
            # if resultbel==0:
            #     continue
            # money-=bet

    print("최고기록 | %d연승"%maxwin)
    print("전적 | 승리:%d 비김:%d 패배:%d"%(wc,mc,lc))
    # print("승리:%d 비김:%d 패배:%d 돈:%d"%(wc,mc,lc,money))
    try:
        uc=int(input("\n1.가위 \n2.바위 \n3.보\n4.exit\n***선택:"))
    except:
        print("잘못된 입력입니다!")
        continue
    cc=random.randint(1,3)
    gameresult=result(uc,cc)
    print("="*30)
    doublescore=printdoubleresult(gameresult)
    
    print("="*30)
    if gameresult==2:
        continue
    countnum=printresult(gameresult)
    if countnum==1:
        wc+=1
    elif countnum==2:
        mc+=1
    elif countnum==3:
        lc+=1
    
    tries+=1
