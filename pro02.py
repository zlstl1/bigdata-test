data = input("숫자 5개를 , 로 구분하여 입력하세요: ")

datas = data.split(",")
sum=0
avg=0

for i in datas:
    sum+=int(i)
avg=sum/5

print("평균은 %.1f 입니다." % avg)