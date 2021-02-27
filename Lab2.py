import random
import math

x1max = 50
x1min = -10
x2max = 60
x2min = -20

x1 = (x1max - x1min)/2
x10 = (x1max + x1min)/2
x2 = (x2max - x2min)/2
x20 = (x2max + x2min)/2

maxY = (30 - 16)*10
minY = (20 - 16)*10
my = (maxY + minY)/2
constant = 18
averageOfY = [random.randint(0, (maxY + minY)) for i in range(constant)]

mx1 = -0.33
mx2 = -0.33
a1 = 1.0
a2 = -0.33
a3 = 1.0
a11 = ((-1)*averageOfY[0] + 1*averageOfY[1] + (-1)*averageOfY[2])/3
a22 = ((-1)*averageOfY[0] + (-1)*averageOfY[1] + 1*averageOfY[2])/3

tempDelta = a1*a3* + mx1*a2*mx2 + mx1*a2*mx2 - mx2*mx2*a1 - a2*a2 - mx1*mx1*a3
b0 = (my*a1*a3 + mx1*a2*a22 + a11*a2*mx2 - a22*a1*mx2 - a11*mx1*a3 - a22*a2*my)/tempDelta
b1 = (a11*a3 + my*a2*mx2 + mx1*a22*mx2 - mx2*mx2*a11 - mx1*my*a3 - a22*a2)/tempDelta
b2 = (a1*a22 + mx1*a11*mx2 + mx1*a2*my - my*a1*mx2 - mx1*mx1*a22 - a2*a11)/tempDelta

a0norm = b0 - b1*(x10/x1) - b2*(x20/x2)
a1norm = b1/x1
a2norm = b2/x2




m = 6
dispersion = averageOfY
fUV = [0, 0, 0]
if dispersion[0] >= dispersion[1]:
    fUV[0] = dispersion[0]/dispersion[1]
else:
    fUV[0] = dispersion[1]/dispersion[0]
if dispersion[0] >= dispersion[2]:
    fUV[1] = dispersion[0]/dispersion[2]
else:
    fUV[1] = dispersion[2]/dispersion[0]
if dispersion[1] >= dispersion[2]:
    fUV[2] = dispersion[1]/dispersion[2]
else:
    fUV[2] = dispersion[2]/dispersion[1]

tauUV = [0, 0, 0]
for i in range (0,3):
    tauUV[i] = ((m - 2)*fUV[i])/m

mainDevitation = math.sqrt(2*(2*m - 2))/(m*(m - 4))

rUV = [0, 0, 0]
for i in range(0,3):
    rUV[i] = abs(tauUV[i] - 1)/mainDevitation
print('Romanowsky Check:\nDispersion:',dispersion)
print('major deviation:',mainDevitation)
print('\nFuv:',fUV)
print('Ouv:',tauUV)
print('Ruv:',rUV)

k = 0
for i in range(0,3):
    if rUV[i] <= 2.16:
        k +=1
if k == 3:
    print('\nThe test was successful')
else:
    print('\nCheck failed')

print('\nThe normal regnesion equation: \ny =', round((b0), 3), '+', round((b1), 3),'x1 +', round((b2), 3),'x2')
print('\nNaturalized equation of regnesia: \ny =', round((a0norm), 2), '+', round((a1norm), 2), 'x1 +', round((a2norm), 2), 'x2')
print('\nb0 =',b0)
print('b1 =',b1)
print('b2 =',b2)
print('\nmx1 =',mx1)
print('mx2 =',mx2)
print('my =',my)
print('\na1 =',a1)
print('a2 =',a2)
print('a3 =',a3)
print('a11 =',a11)
print('a22 =',a22)
