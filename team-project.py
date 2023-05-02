# 두명의 player가 서로 번갈아가면서 교대로 4자리의 숫자를 맞춘다
import random

# 1번
userNum = [] # 사용자로부터 입력받아 append하는 1차원 int형 리스트 4개입
baseNum = [] # 랜덤으로 뽑아내는 1차원 int형 리스트 4개입

# 2번:
# strike와, ball count용 변수 선언 -> global var로 선언해야 누적된다
# 반복문 안에 local var로 선언하면 반복문을 돌때마다 초기화된다
strike = 0
ball = 0

# 10번의 기회가 주어졌다
for game in range(10):
    userNum = []
    baseNum = []
    # 사용자로부터 1부터 9까지의 범위를 4개의 수를 입력받는 반복 범위
    for i in range(4):
        an = int(input("1 ~ 9 범위 내의 있는 숫자 4개를 중복되지 않게 
입력: "))
        userNum.append(an)

    # 랜덤으로 1부터 9까지의 범위를 4개의 수를 출력하는 반복 범위
    for i in range(4):
        bn = random.randrange(1, 10)
        baseNum.append(bn)

    print("사용자가 입력한 수 4개입: ", userNum)
    print("컴퓨터가 제시한 수 4개입: ", baseNum)

    for i in range(4):
        # "Strike 개수 증가, Ball 개수 증가" 조건 들어가야 한다
        # Strike는 위치와 숫자가 전부 맞을 경우
        if baseNum[i] == userNum[i]:
            strike += 1
        # Ball은 숫자는 맞췄으나 위치만 틀린 경우
        elif userNum[i] in baseNum:
            ball += 1
    
    print("strike: ", strike, "ball: ", ball)
