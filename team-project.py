checkDict = dict()
count = 10

while count:
    checkDict['S'] = 0
    checkDict['B'] = 0
    a = str(input())  

    if checkDict['S'] == 4:
        break

    count -= 1

print(f'축하합니다 {10 - count + 1}번의 도전으로 {baseNum}을 맞추셨습니다')