import random

m = [[random.randint(0, 20) for i in range(3)] for i in range(8)]
print("value of the factors at the points of the experiment:") #Значення факторів у точках експерименту
for i in m:
    print(i)

a0 = random.randint(0, 20)
a1 = random.randint(0, 20)
a2 = random.randint(0, 20)
a3 = random.randint(0, 20)

Y_list = []
for x in m:
    Y = a0 + a1*x[0] + a2*x[1] + a3*x[2]
    Y_list.append(Y)
print(f"\nFunctions of the feedback at each point of the experiment:\n{Y_list}\n")  #Функції відгуку у кожній точці експерименту

Yc = (max(Y_list) + min(Y_list)) / 2

x0_1_list = {m[i][0] for i in range(8)}
x0_2_list = {m[i][1] for i in range(8)}
x0_3_list = {m[i][2] for i in range(8)}

x0_1 = (max(x0_1_list) + min(x0_1_list)) / 2
dx_1 = x0_1 - min(x0_1_list)

x0_2 = (max(x0_2_list) + min(x0_2_list)) / 2
dx_2 = x0_2 - min(x0_2_list)

x0_3 = (max(x0_3_list) + min(x0_3_list)) / 2
dx_3 = x0_3 - min(x0_3_list)

print(f"Zero level for the first factor:\nX0 = {x0_1}\ndx = {dx_1}\n\nZero level for the second factor:\nX0 = {x0_2}\ndx = {dx_2}\n\nZero level for the third factor:\nX0 = {x0_3}\ndx = {dx_3}\n")

x0_list = [x0_1, x0_2, x0_3]
dx_list = [dx_1, dx_2, dx_3]

normalization = []
print("Values of the factors at the points of the experiment after normalization:")  #Значення факторів у точках експерименту після нормалізації
for i in range(8):
    normalization.append([])
    for j in range(3):
        normalization[i].append(round(((m[i][j] - x0_list[j]) / dx_list[j]), 5))
        if j == 2:
            print(normalization[i])

Yet = a0 + a1*x0_1 + a2*x0_2 + a3*x0_3

print(f"\nThe function of the zero level of the factors:\nYет = {Yet}")  #Ф-ція відгуку від нульових рівнів факторів

distinc = []  #(Yi - Yет)

for Y in Y_list:
    distinc.append(Y - Yet)
print(f"\nDifferences of the feedback function and the feedback function from the zero level of factors:\n{distinc}")  #Різниця ф-цій відгуку і ф-ції відгуку від нульових рівнів факторів

min_d = distinc[0]
for d in distinc:
    if d < 0:
        continue
    else:
        if min_d < 0:
            min_d = d
        elif d < abs(min_d):
            min_d = d
print(f"\nValue of the function of the feedback, which is closest to the value of the reference function of the feedback:\n{min_d + Yet}")  #Значення функції відгуку, яке найблище до значення еталонної ф-ції відгуку

k=0
for i in range(len(Y_list)):
    if (Yc == Y_list[i]):
        print(f"\nPlan point that satisfies the criterion of optimality (Y <--):\n{m[i]}")  #Точка плану, що задовольняє критерій оптимальності (Y <--)
        k+=1

if k==0:
    print(f"\nThere is no plan point that satisfies the criterion of optimality")  #Точки плану, що задовольняє критерій оптимальності не існує

