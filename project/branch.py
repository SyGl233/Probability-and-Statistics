import random


n = 1000 # 实验组数
m = 100000 # 实验轮数
total_round = 0
initial_n = n
num = [1] * n 

for r in range(m):
    for group in range(n):
        if(group >= n):
            break
        cur = num[group]
        num[group] = 0
        for i in range(cur):
            num[group] += random.randint(0,2)
        if(num[group]==0):
            del num[group]
            n -= 1
            total_round += r + 1
    if(len(num)==0):
        m = r + 1
        break
    print(f"第{r+1}轮")
    print(num)        
    print(f'共{n}个')
    print()

print(f'平均活了{total_round/initial_n}轮')