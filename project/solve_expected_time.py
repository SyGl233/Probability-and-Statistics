import math
def p(x):
    return math.exp(x-1)
n = 10000000 # 轮数
prob = []
prob.append(p(0))
for i in range(n):
    prob.append(p(prob[i]))
sum = prob[n]
for i in range(n):
    sum += prob[n] - prob[i]
print(sum)