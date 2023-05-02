import random
num = random.sample(range(10), 4)
baseNum = ''.join(map(str, num))
checkDict = dict()
count = 10                        #10번까지 반복
while count:
    checkDict['S'] = 0
    checkDict['B'] = 0
    a = str(input())
    for i in range(len(a)):                            #검증
        if a[i] == baseNum[i]:
            checkDict['S'] += 1
        elif a[i] in baseNum:
            checkDict['B'] += 1
    print(f"{checkDict['S']}S, {checkDict['B']}B")
    if checkDict['S'] == 4:
        break
    count -= 1
print(f'축하합니다 {10 - count + 1}번의 도전으로 {baseNum}을 맞추셨네요 추카포카룽')