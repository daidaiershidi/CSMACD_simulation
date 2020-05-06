# -*- coding: utf-8 -*-
"""
@author: 刘铠源
"""
import random
import numpy as np
#ong = 1#ong<tao
def fun(N):
    node = []
    T2 = 10
    T1 = 20#距离taoT1/2
    n0 = []
    n1 = []
    n2 = []
    n3 = []
    n4 = []
    n5 = []
    n6 = []
    n7 = []
    #每个节点【0index，1状态（0空闲，1发送），2发送时序，3监听位，4冲突位，5时序,6上次碰撞时间,7重传次数】
    def init_node():
        for i in range(N):
            n0.append(i)
            n1.append(0)
            n2.append(0)
            n3.append(0)
            n4.append(0)
            n5.append(0)
            n6.append(0)
            n7.append(0)
    def random_pick(some_list,probabilities):
        #[0,1][0.5,0.5]
        x=random.uniform(0,1)
        cumulative_probability=0.0
        for item,item_probability in zip(some_list,probabilities):
            cumulative_probability+=item_probability
            if x < cumulative_probability: break
        return item 
    def addtime(num):
        for i in range(N):
            n5[i]+=1
        for i in num:
            n2[i]+=1    
    t = k = 0
    num = []
    l = []
    flag = 0
    init_node()
    while(1):
        for i in range(N):
            if (n4[i]==0 and n1[i]==0):
                n1[i] = random_pick([1,0], [0.35,0.65])
                if n1[i]==1:
                    l.append(i)
            if n1[i]==2:
                if n7[i]==16:
                    n1[i]=n3[i]=n4[i]=n7[i]=0
                if (t-n6[i]>=n3[i]*T1):
                    n1[i]=n3[i]=0
                    n7[i]+=1
                    n4[i] = 0
        addtime(l)
        #listen
        ll = []
        for i in range(N):
            ll.append(n2[i])
        m1 = max(ll)
        ll.remove(m1)
        m2 = max(ll)
        print(m1,m2)
        if m2+m1>=int(T1/2) and m1!=0 and m2!=0:
            for i in range(N):
                if n2[i]==m1:
                    a=i
            for i in range(N):
                if n2[i]==m2 and i!=a:
                    b=i
#            a = int(ll[0][0])
#            b = int(ll[1][0])
#            random.shuffle(ll)
            print(a,b,'发生碰撞')
            for i in range(N):
                n1[i]=n2[i]=0
            n4[a] = n4[b] = 1
            n1[a] = n1[b] = 2
            n6[a] = n6[b] = t
            n2[a] = n2[b] = 0
            n3[a] = int(random.randint(1, 2**(min(n7[a],10))))
            n3[b] = int(random.randint(1, 2**(min(n7[b],10))))
#            print('!!!!!!!!!!!!!!!!!!!!!!!!',a,b)
#            print(l,b)
            l.remove(a)
            l.remove(b)
#        print('time:',t,'######','当前在发送:',l)
#        print(n0)
#        print(n1,'是否发送n1')
#        print(n2,'发送时序n2')
#        print(n3,'2k时间')
#        print(n4,'是否冲突n4')
#        print(n5,'时序n5')
#        print(n6,'上次碰撞时间n6')
#        print(n7,'重传次数n7')
        for i in range(N):
            if n2[i]==T2:
                k = i
                flag = 1
        if flag == 1:
#            print(k)
#            print(n2[k])
            break
        t+=1
    return t
#aa = fun(10)
#print(aa)
y = []
for i in range(1,10):
    sum_ = 0
    for j in range(10):
#        print(j,'//100',end='\r')
        sum_+=fun(i*10)
    y.append(sum_/10)
print(y)
import matplotlib.pyplot as plt
import numpy as np
 
x = []
for i in range(9):
    x.append(i)
    y[i] = 10/y[i]
print(y)
plt.plot(x,y)
plt.show()

