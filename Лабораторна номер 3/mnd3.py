import random
import math

Gt = 0.7679
Ft = 4.5
Tf = 2.306
m = 3
N = 4

x1min = -10
x1max = 50
x2min = -20
x2max = 60
x3min = -20
x3max = 5

ymin = 200 + (x1min + x2min + x3min)/3
ymax = 200 + (x1max + x2max + x3max)/3

x1 = [random.randint(x1min, x1max + 1) for i in range(4)]
x2 = [random.randint(x2min, x2max + 1) for i in range(4)]
x3 = [random.randint(x3min, x3max + 1) for i in range(4)]
y1 = [random.randint(int(ymin), int(ymax) + 1) for i in range(4)]
y2 = [random.randint(int(ymin), int(ymax) + 1) for i in range(4)]
y3 = [random.randint(int(ymin), int(ymax) + 1) for i in range(4)]

averageY = [0, 0, 0, 0]
for i in range(0, len(x1)):
    averageY[i] = (y1[i] + y2[i] + y3[i])/3

mx = [0, 0, 0]
mx[0] = (x1[0] + x1[1] + x1[2] + x1[3])/4
mx[1] = (x2[0] + x2[1] + x2[2] + x2[3])/4
mx[2] = (x3[0] + x3[1] + x3[2] + x3[3])/4
my = (averageY[0] + averageY[1] + averageY[2] + averageY[3])/len(averageY)

a = [0, 0, 0]
a[0] = (x1[0]*averageY[0] + x1[1]*averageY[1] + x1[2]*averageY[2] + x1[3]*averageY[3])/4
a[1] = (x2[0]*averageY[0] + x2[1]*averageY[1] + x2[2]*averageY[2] + x2[3]*averageY[3])/4
a[2] = (x3[0]*averageY[0] + x3[1]*averageY[1] + x3[2]*averageY[2] + x3[3]*averageY[3])/4

k = 0
for i in range(0, len(x1)):
    k += x1[i]**2
a11 = k/4

k = 0
for i in range(0, len(x2)):
    k += x2[i]**2
a22 = k/4

k = 0
for i in range(0, len(x3)):
    k += x3[i]**2
a33 = k/4

k = 0
for i in range(0, len(x1)):
    k += x1[i]*x2[i]
a12 = k/4

k = 0
for i in range(0, len(x1)):
    k += x1[i]*x3[i]
a13 = k/4

k = 0
for i in range(0, len(x2)):
    k += x2[i]*x3[i]
a23 = k/4

a32 = a23

r01 = [1, mx[0], mx[1], mx[2]]
r02 = [mx[0], a11, a12, a13]
r03 = [mx[1], a12, a22, a32]
r04 = [mx[2], a13, a23, a33]
temp0 = [r01, r02, r03, r04]
determ = 1*a11*a22*a33 + mx[0]*a12*a32*mx[2] + mx[1]*a13*mx[1]*a13 + mx[2]*mx[0]*a12*a23 - (mx[2]*a12*a12*mx[2] + a13*a22*a13*1 + a23*a32*mx[0]*mx[0] + a33*mx[1]*a11*mx[1])

r11 = [my, mx[0], mx[1], mx[2]]
r12 = [a[0], a11, a12, a13]
r13 = [a[1], a12, a22, a32]
r14 = [a[2], a13, a23, a33]
temp1 = [r11, r12, r13, r14]
determ1 = my*a11*a22*a33 + a[0]*a12*a32*mx[2] + a[1]*a13*mx[1]*a13 + a[2]*mx[0]*a12*a23 - (a[2]*a12*a12*mx[2] + a13*a22*a13*my + a23*a32*a[0]*mx[0] + a33*a[1]*a11*mx[1])

r21 = [1, my, mx[1], mx[2]]
r22 = [mx[0], a[0], a12, a13]
r23 = [mx[1], a[1], a22, a32]
r24 = [mx[2], a[2], a23, a33]
temp2 = [r21, r22, r23, r24]
determ2 = 1*a[0]*a22*a33 + my*a12*a32*mx[2] + mx[1]*a13*mx[1]*a[2] + mx[2]*mx[0]*a[1]*a23 - (mx[2]*a[1]*a12*mx[2] + a[2]*a22*a13*1 + a23*a32*my*mx[0] + a33*mx[1]*a[0]*mx[1])

r31 = [1, mx[0], my, mx[2]]
r32 = [mx[0], a11, a[0], a13]
r33 = [mx[1], a12, a[1], a32]
r34 = [mx[2], a13, a[2], a33]
temp3 = [r31, r32, r33, r34]
determ3 = 1*a11*a[1]*a33 + mx[0]*a[0]*a32*mx[2] + my*a13*mx[1]*a13 + mx[2]*mx[0]*a12*a[2] - (mx[2]*a12*a[0]*mx[2] + a13*a[1]*a13*1 + a[2]*a32*mx[0]*mx[0] + a33*mx[1]*a11*my)

r41 = [1, mx[0], mx[1], my]
r42 = [mx[0], a11, a12, a[0]]
r43 = [mx[1], a12, a22, a[1]]
r44 = [mx[2], a13, a23, a[2]]
temp4 = [r41, r42, r43, r44]
determ4 = 1*a11*a22*a[2] + mx[0]*a12*a[1]*mx[2] + mx[1]*a[0]*mx[1]*a13 + my*mx[0]*a12*a23 - (mx[2]*a12*a12*my + a13*a22*a[0]*1 + a23*a[1]*mx[0]*mx[0] + a[2]*mx[1]*a11*mx[1])

b = [0, 0, 0, 0]
b[0] = determ1/determ
b[1] = determ2/determ
b[2] = determ3/determ
b[3] = determ4/determ

disperS = [0, 0, 0, 0]
for i in range(0, len(disperS)):
    disperS[i] = ((y1[i] - averageY[i])**2 + (y2[i] - averageY[i])**2 + (y3[i] - averageY[i])**2)/3

Gp = max(disperS)/(disperS[0] + disperS[1] + disperS[2] + disperS[3])
print('Перевірка однорідності дисперсії за критерієм Кохрена:')
print('Gp =',Gp,'\nGt =',Gt)

if Gp <= Gt:
    print('Gp <= Gt Дисперсія однорідна')
else:
    print('Gp > Gt  Дсперсія не однорідна. Потрібно збільшити m')

S_average = (disperS[0] + disperS[1] + disperS[2] + disperS[3])/N
S_2_odnorod = S_average/(N*m)
S_odnorod = math.sqrt(S_2_odnorod)

beta = [0, 0, 0, 0]
beta[0] = (averageY[0]*1 + averageY[1]*1 + averageY[2]*1 + averageY[3]*1)/N
beta[1] = (averageY[0]*(-1) + averageY[1]*(-1) + averageY[2]*1 + averageY[3]*1)/N
beta[2] = (averageY[0]*(-1) + averageY[1]*1 + averageY[2]*(-1) + averageY[3]*1)/N
beta[3] = (averageY[0]*(-1) + averageY[1]*1 + averageY[2]*1 + averageY[3]*(-1))/N

t = [0, 0, 0, 0]
t[0] = abs(beta[0])/S_odnorod
t[1] = abs(beta[1])/S_odnorod
t[2] = abs(beta[2])/S_odnorod
t[3] = abs(beta[3])/S_odnorod

print('\nОцінка значимості коефіцієнтів регресії згідно критерію Стьюдента:')
d = 0
temp = [0, 0, 0, 0]
for i in range(0, N):
    if t[i] <= Tf:
        print('t[',i,'] =',t[i],'<= Tf =',Tf,'>= b[',i,'] =', b[i],'- не значний коефіцієнт')
        temp[i] = 0
    else:
        print('t[',i,'] =',t[i],'> Tf =',Tf,'>= b[',i,'] =', b[i],'- значний коефіцієнт')
        temp[i] = b[i]
        d +=1

y_2 = [0, 0, 0, 0]
for i in range(0,N):
    y_2[i] = temp[0] + temp[1]*x1[i] + temp[2]*x2[i] + temp[3]*x3[i]

print('\nКритерій Фішера:')
print('Кількість значимих коефіцієнтів d =', d)
S_adekv = (m/(N - d))*((y_2[0] - averageY[0])**2 + (y_2[1] - averageY[1])**2 + (y_2[2] - averageY[2])**2 + (y_2[3] - averageY[3])**2)
print(S_adekv, '- S адекватності')

Fp = S_adekv/S_odnorod
print('Fp =', Fp)
if Fp <= Ft:
    print('\nРівняння регресії адекватне щодо оригіналу при рівні значимості 0,05')
else:
    print('\nРівняння регресії НЕадекватне щодо оригіналу при рівні значимості 0,05')

print('y =', b[0],'+',b[1],'* x1 +',b[2],'* x2 +',b[3],'* x3')
