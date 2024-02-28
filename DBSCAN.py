import random
import math
import matplotlib.pyplot as plt


points_list = []
for i in range(0,100):
    x= random.randint(5,10)
    y = random.randint(70,100)
    points_list.append([x,y])

for i in range(0,100):
    x= random.randint(-10,0)
    y = random.randint(1,40)
    points_list.append([x,y])


l_p=[-1 for i in range(0,len(points_list))]
eps = 20
nr_min = 4

C = 0

def RangeQuery(points_list,P,eps):
    N = []
    for p in points_list:
        if math.dist(P,p) <= eps:
            N.append(p)
    return N


for P in points_list:
    if l_p[points_list.index(P)] == -1:
        N=RangeQuery(points_list,P,eps)

        if  N == None or len(N) < nr_min:
            l_p[points_list.index(P)] = 0 # 0 - noise
        else:
            C=C+1
            l_p[points_list.index(P)] = C
            S = N
            S.remove(P)
            for Q in S:
                if l_p[points_list.index(Q)] == 0:
                    l_p[points_list.index(Q)] = C
                if l_p[points_list.index(Q)] != -1:
                    l_p[points_list.index(Q)] = C
                    N=RangeQuery(points_list,Q,eps)    
                    if len(N) >= nr_min:
                        S = S + N

# print(l_p)

# x=[]
# y=[]
# for elem in points_list:
#     if l_p[points_list.index(elem)] < 150 :
#         x.append(elem[0])
#         y.append(elem[1])


# xx=[]
# yy=[]
# for elem in points_list:
#     if l_p[points_list.index(elem)] > 150 :
#         xx.append(elem[0])
#         yy.append(elem[1])
# plt.plot(x,y, 'o', color='black')

# plt.plot(xx,yy, 'o', color='red')
# plt.show()