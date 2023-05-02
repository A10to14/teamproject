while count:
    checkDict['S'] = 0
    checkDict['B'] = 0
    a = str(input())

    # "Strike 개수 증가, Ball 개수 증가" 조건 들어가야 한다   
    for i in range(len(a)):
        # Strike는 위치와 숫자가 전부 맞을 경우
        if a[i] == baseNum[i]:
            checkDict['S'] += 1
        # Ball은 숫자는 맞췄으나 위치만 틀린 경우
        elif a[i] in baseNum:
            checkDict['B'] += 1
    
    # strike, ball 카운트를 출력한다
    print(f"{checkDict['S']}S, {checkDict['B']}B")

    # strike 횟수가 4를 넘으면 out
    if checkDict['S'] == 4:
        break
    count -= 1 # 위 조건이 모두 실행되면 count 하나씩 감소한다
