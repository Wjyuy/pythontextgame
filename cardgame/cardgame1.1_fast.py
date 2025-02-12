import random
import time
import os
num=0
data=[]

def readfile():
    f=open("scores_Wjy.txt","r",encoding="utf-8")
    playername=input("이름을 입력해 주세요! : ")
    lines=f.readlines()
    best=0
    best_name=""
    for line in lines:
        data=line.split()
        if int(best)<int(data[1]):
            best=data[1]
            best_name=data[0]
    for line in lines:
        data=line.split()
        f.close()
        if playername==data[0]:
            return [data,best,best_name]
    data=[[playername,0,0],best,best_name]
    return data

def writefile(data): 
    with open("scores_Wjy.txt",'a') as f:
        f.write("\n"+data[0][0]+" ")
        f.write(str(data[0][1])+" ")
        f.write(str(data[0][2]))

def Playerbestprint(data):
    print("***명예의 전당***")
    print(data[2],"님이",data[1],"점으로 1등입니다 !!!!")
    print("*****************")

class Table:
    turn=10
    def __init__(self,name):
        self.score=0
        self.name=name
        self.card=[1,2,3,4,5,6,7,8,9,10]
    def print(self):
        print(self.name,"가 사용가능한 카드:",self.card)
    def userchoice(self):
        uc=0
        while uc<=0 or uc>10:
            print("1부터 10까지의 카드 중 무엇을 내겠습니까?")
            print("사용하지 않은 카드\n")
            if len(self.card)==10:
                print("┌--┐┌--┐┌--┐┌--┐┌--┐\n│%2d││%2d││%2d││%2d││%2d│\n└--┘└--┘└--┘└--┘└--┘\n"%(self.card[0],self.card[1],self.card[2],self.card[3],self.card[4]),end="")
                print("┌--┐┌--┐┌--┐┌--┐┌--┐\n│%2d││%2d││%2d││%2d││%2d│\n└--┘└--┘└--┘└--┘└--┘\n"%(self.card[5],self.card[6],self.card[7],self.card[8],self.card[9]),end="")
            if len(self.card)==9:
                print("┌--┐┌--┐┌--┐┌--┐┌--┐\n│%2d││%2d││%2d││%2d││%2d│\n└--┘└--┘└--┘└--┘└--┘\n"%(self.card[0],self.card[1],self.card[2],self.card[3],self.card[4]),end="")
                print("┌--┐┌--┐┌--┐┌--┐\n│%2d││%2d││%2d││%2d│\n└--┘└--┘└--┘└--┘\n"%(self.card[5],self.card[6],self.card[7],self.card[8]),end="")
            if len(self.card)==8:
                print("┌--┐┌--┐┌--┐┌--┐┌--┐\n│%2d││%2d││%2d││%2d││%2d│\n└--┘└--┘└--┘└--┘└--┘\n"%(self.card[0],self.card[1],self.card[2],self.card[3],self.card[4]),end="")
                print("┌--┐┌--┐┌--┐\n│%2d││%2d││%2d│\n└--┘└--┘└--┘\n"%(self.card[5],self.card[6],self.card[7]),end="")
            if len(self.card)==7:
                print("┌--┐┌--┐┌--┐┌--┐┌--┐\n│%2d││%2d││%2d││%2d││%2d│\n└--┘└--┘└--┘└--┘└--┘\n"%(self.card[0],self.card[1],self.card[2],self.card[3],self.card[4]),end="")
                print("┌--┐┌--┐\n│%2d││%2d│\n└--┘└--┘\n"%(self.card[5],self.card[6]),end="")
            if len(self.card)==6:
                print("┌--┐┌--┐┌--┐┌--┐┌--┐\n│%2d││%2d││%2d││%2d││%2d│\n└--┘└--┘└--┘└--┘└--┘\n"%(self.card[0],self.card[1],self.card[2],self.card[3],self.card[4]),end="")
                print("┌--┐\n│%2d│\n└--┘\n"%(self.card[5]),end="")
            if len(self.card)==5:
                print("┌--┐┌--┐┌--┐┌--┐┌--┐\n│%2d││%2d││%2d││%2d││%2d│\n└--┘└--┘└--┘└--┘└--┘\n"%(self.card[0],self.card[1],self.card[2],self.card[3],self.card[4]),end="")
            if len(self.card)==4:
                print("┌--┐┌--┐┌--┐┌--┐\n│%2d││%2d││%2d││%2d│\n└--┘└--┘└--┘└--┘\n"%(self.card[0],self.card[1],self.card[2],self.card[3]),end="")
            if len(self.card)==3:
                print("┌--┐┌--┐┌--┐\n│%2d││%2d││%2d│\n└--┘└--┘└--┘\n"%(self.card[0],self.card[1],self.card[2]),end="")
            if len(self.card)==2:
                print("┌--┐┌--┐\n│%2d││%2d│\n└--┘└--┘\n"%(self.card[0],self.card[1]),end="")
            if len(self.card)==1:
                print("┌--┐\n│%2d│\n└--┘\n"%(self.card[0]),end="")
            uc=int(input("\n***당신의 선택 : "))
            if uc in self.card:
                self.card.remove(uc)
            return uc
    def comchoice(self):
        waittime=random.randint(1,3)
        print("컴퓨터가 카드를 고르고 있습니다")
        # for i in range(0,waittime):
        #     print(".")
        #     time.sleep(1)
        # print("컴퓨터가 카드를 정했습니다!")
        # time.sleep(2)
        cc=random.choice(self.card)
        self.card.remove(cc)
        return cc 
    def dual(self,num,cum):
        os.system('cls')
        printscreen()
        print("You  Com\n┌--┐ ┏┳┳┓\n│%2d│ ┣╋╋┫\n└--┘ ┗┻┻┛\n"%(num),end="")
        # time.sleep(2)
        os.system('cls')
        printscreen()
        print("You  Com\n┌--┐ ┌--┐\n│%2d│ │%2d│\n└--┘ └--┘\n"%(num,cum),end="")
        # time.sleep(2)
        if num>cum:
            print("You Win!")
            Table.turn-=1
            user.score+=1
        if num<cum:
            print("Com Win!")
            com.score+=1
            Table.turn-=1
        if num==cum:
            print("비겼어요!")
            Table.turn-=1
        print("")
        # for i in range(0,3):
        #     print("%d초 후 넘어갑니다."%(3-i))
        #     time.sleep(1)

user=Table("user")
com=Table("com")
data=readfile()

def printscreen():
    os.system('cls')
    print("="*50)
    print("카드 게임")
    Playerbestprint(data)
    print("현재 스코어 YOU:%d COM:%d"%(user.score,com.score))
    print("남은 턴 : ",Table.turn)
    print("="*50)
    print("")

def printstart():
    num=0
    print("="*20)
    print("")
    print("***카드 게임***")
    print("")
    print("1. 게임 시작")
    print("")
    print("2. 게임 방법")
    print("")
    print("="*20)
    num=int(input("***선택 : "))
    if num==2:
        os.system('cls')
        print("="*20)
        print("")
        print("***게임 방법***")
        print("")
        print("컴퓨터와 1부터 10까지의 카드를 가지고 10번의 대결을 펼칩니다!")
        print("")
        print("서로 한장의 카드를 선택하여, 더 높은 카드를 낸 쪽이 승리합니다!")
        print("")
        print("한번 사용한 카드는 다시 사용할 수 없습니다!")
        print("")
        print("Normal mode: 컴퓨터가 무슨 카드를 사용하였는지 볼 수 없습니다.")
        print("Easy mode: 컴퓨터가 무슨 카드를 사용하였는지 볼 수 있습니다.(구현X)")
        print("")
        print("!!!!!!!!!!!!!!!!!!!!!문자를 쓰시면 튕깁니다!!!!!!!!!!!!!!!!!!!!!")
        print("")
        print("="*20)
        print("")
        os.system("pause")
    print("")
    print("1. Normal mode: 컴퓨터가 무슨 카드를 사용하였는지 볼 수 없습니다.")
    print("2. Easy mode: 컴퓨터가 무슨 카드를 사용하였는지 볼 수 있습니다.")
    print("")
    num=print("난이도를 선택하세요! (1/2)")
    num=int(input("***선택 : "))
    return num

#여기서부터 게임시작
num=printstart()
while Table.turn!=0:
    printscreen()
    while Table.turn==len(user.card):
        if num==2:
            com.print()
        uc=user.userchoice()
        printscreen()
    cc=com.comchoice()
    user.dual(uc,cc)
printscreen()
if user.score>com.score:
    print("\n게임이 종료되었습니다.")
    print("\n당신의 승리입니다!!!")
    data[0][1]=user.score
    data[0][2]=com.score
    writefile(data)
    print("아무 키를 누르면 종료됩니다.")
    os.system("pause")
if user.score<com.score:
    print("\n게임이 종료되었습니다.")
    print("\n당신은 패배하였습니다..")
    data[0][1]=user.score
    data[0][2]=com.score
    writefile(data)
    print("아무 키를 누르면 종료됩니다.")
    os.system("pause")
if user.score==com.score:
    print("\n게임이 종료되었습니다.")
    print("\n비겼습니다!")
    data[0][1]=user.score
    data[0][2]=com.score
    writefile(data)
    print("아무 키를 누르면 종료됩니다.")
    os.system("pause")