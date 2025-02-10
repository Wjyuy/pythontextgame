import os
import time

userchoiceanimal=0
howmanysheepchoice=0
howmanywolfchoice=0

sheep=0
wolf=0
left_sheep=3
left_wolf=3

right_sheep=0
right_wolf=0

boat_sheep=0
boat_wolf=0

gameover=0
gameover2=0

def paintscreenl():
    print("="*50)
    print("{0:<5}{1:>7}{2:>30}".format("왼쪽","나룻배","오른쪽"))
    print("{0}{1:<5}{2:>4}{3}{4:>30}{5}".format("늑대:",left_wolf,"늑대:",boat_wolf,"늑대:",right_wolf))
    print("{0}{1:<5}{2:>5}{3}{4:>31}{5}".format("양:",left_sheep,"양:",boat_sheep,"양:",right_sheep))
    print("="*50)

def paintscreenr():
    print("="*50)
    print("{0:<30}{1:<7}{2:>5}".format("왼쪽","나룻배","오른쪽"))
    print("{0}{1:<27}{2}{3}{4:>9}{5}".format("늑대:",left_wolf,"늑대:",boat_wolf,"늑대:",right_wolf))
    print("{0}{1:<29}{2}{3}{4:>10}{5}".format("양:",left_sheep,"양:",boat_sheep,"양:",right_sheep))
    print("="*50)

def check(ls,lw,rs,rw,count):
    if ls!=0:
        if lw>ls:
            count=1
            return count
    if rs!=0:
        if rw>rs:
            count=1
            return count

def checkminus(ls,lw,rs,rw,count):
    if ls<0 or lw<0 or rs<0 or rw<0:
        count=1
        return count
        

print("***강 건너기 게임***\n")
print("당신은 나룻배에 종류 상관 없이 최대 두마리의 동물을 태울 수 있습니다.")
print("한 지역에 남게 되는 늑대의 수가 양보다 많게 되면 게임 오버!")
print("사공이 없으면 배는 움직이지 못합니다. 모두 강을 건너면 당신의 승리!\n")
paintscreenl()

tries=1
while tries<=100:
    print("%d번째 시도!"%tries)
    try:
        if tries%2==1:
            userchoiceanimal=int(input("배에 태울 동물을 선택하세요 (1/2/3)\n1:양만 보낸다\n2:늑대만 보낸다\n3:늑대1마리,양1마리를 보낸다\n***선택:"))
            if(userchoiceanimal==1):
                print("양을 몇마리 보내시겠습니까? (1/2)")
                userchoiceanimalnums=int(input("1: 양1마리\n2: 양2마리\n@: 다른문자 선택 시 돌아갑니다.\n***선택:"))
                if userchoiceanimalnums==1 or userchoiceanimalnums==2:
                    boat_sheep+=userchoiceanimalnums
                    left_sheep-=userchoiceanimalnums
                else:
                    print("-"*30)
                    continue
            elif(userchoiceanimal==2):
                print("늑대를 몇마리 보내시겠습니까? (1/2)")
                userchoiceanimalnumw=int(input("1: 늑대1마리\n2: 늑대2마리\n@: 다른문자 선택 시 돌아갑니다.\n***선택:"))
                if userchoiceanimalnumw==1 or userchoiceanimalnumw==2:
                    boat_wolf+=userchoiceanimalnumw
                    left_wolf-=userchoiceanimalnumw
                else:
                    print("-"*30)
                    continue
            elif(userchoiceanimal==3):
                boat_wolf+=1
                left_wolf-=1
                boat_sheep+=1
                left_sheep-=1
            else:
                print("처음으로 돌아갑니다!")
                print("-"*30)
                continue
            paintscreenl()
            for i in range(3):
                print("%d 초 후 배가 이동합니다!"%(3-i))
                time.sleep(1)
            right_sheep+=boat_sheep
            right_wolf+=boat_wolf
            boat_wolf=0
            boat_sheep=0
    except:
        print("문자가 입력되어 처음으로 돌아갑니다!")
        print("-"*30)
        continue
    
    try:    
        if tries%2==0:
            userchoiceanimal=int(input("배에 태울 동물을 선택하세요(1/2/3)\n1:양만 보낸다\n2:늑대만 보낸다\n3:늑대1마리,양1마리를 보낸다\n***선택:"))
            if(userchoiceanimal==1):
                print("양을 몇마리 보내시겠습니까? (1/2)")
                userchoiceanimalnums=int(input("1: 양1마리\n2: 양2마리\n@: 다른문자 선택 시 돌아갑니다.\n***선택:"))
                if userchoiceanimalnums ==1 or userchoiceanimalnums==2:
                    boat_sheep+=userchoiceanimalnums
                    right_sheep-=userchoiceanimalnums
                else:
                    print("-"*30)
                    continue
            elif(userchoiceanimal==2):
                print("늑대를 몇마리 보내시겠습니까? (1/2)")
                userchoiceanimalnumw=int(input("1: 늑대1마리\n2: 늑대2마리\n@: 다른문자 선택 시 돌아갑니다.\n***선택:"))
                if userchoiceanimalnumw ==1 or userchoiceanimalnumw==2:
                    boat_wolf+=userchoiceanimalnumw
                    right_wolf-=userchoiceanimalnumw
                else:
                    print("-"*30)
                    continue
            elif(userchoiceanimal==3):
                boat_wolf+=1
                right_wolf-=1
                boat_sheep+=1
                right_sheep-=1
            else:
                print("잘못 입력하셨습니다!")
                continue
            paintscreenr()
            for i in range(3):
                print("%d 초 후 배가 이동합니다!"%(3-i))
                time.sleep(1)
            left_sheep+=boat_sheep
            left_wolf+=boat_wolf
            boat_wolf=0
            boat_sheep=0
    except:
        print("문자가 입력되어 처음으로 돌아갑니다!")
        print("-"*30)
        continue

    gameover=check(left_sheep,left_wolf,right_sheep,right_wolf,gameover)
    gameover2=checkminus(left_sheep,left_wolf,right_sheep,right_wolf,gameover2)
    if(gameover2==1):
        print("오류가 감지되어 종료합니다.")
        os.system("pause")
        break
    if(gameover==1):
        if tries%2==1:
            paintscreenr()
        else:
            paintscreenl()
        print("늑대가 양을 잡아먹었습니다! GAME OVER ")
        print("당신의 시도 횟수는 %d 번입니다."%tries)
        print("="*50)
        os.system("pause")
        break
    if left_sheep==0 and left_wolf==0:
        if tries%2==1:
            paintscreenr()
        else:
            paintscreenl()
        print("무사히 강을 건넜습니다!!! ")
        print("당신의 시도 횟수는 %d 번입니다."%tries)
        print("="*50)
        os.system("pause")
        break
    if tries%2==0:
        paintscreenl()
    else:
        paintscreenr()
    os.system("pause")
    tries+=1
            