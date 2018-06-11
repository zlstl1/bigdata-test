total=0
while True:
    print("-"*30)
    print("1.예금 | 2.출금 | 3.잔고 | 4.종료")
    print("-"*30)
    select = int(input("선택>"))

    if select==1:
        money = int(input("예금액>"))
        total+=money
    elif select==2:
        if total<money:
            continue
        money = int(input("출금금액>"))
        total-=money
    elif select==3:
        print("잔고액> %d" % total)
    elif select==4:
        print("프로그램 종료")
        break
    else:
        print("다시입력해 주세요")