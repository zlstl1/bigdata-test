from random import random

data=set({})
while True:
    hidden_num = int(random() * 45)
    data.add(hidden_num)
    if len(data)==6:
        break
print(data,sep=", ")