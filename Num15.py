# ------------------------------------------------------------------

# 15 задание ЕГЭ. Алгебра логики.

# MOD(100,A) - % (остаток от деления)
# DIR(x,25) - первая цифра числа (В данном услучае 2)
# ДЕЛ(x,A) - деление числа

# ------------------------------------------------------------------

# 1:52:42
# vkvideo.ru/video-205865487_456239697

# def f(x):
#     return (x&a!=0)<=(((x&17==0)and(x&5==0))<=(x&3!=0))
# for a in range(100):
#     if all(f(x) == 1 for x in range(10000)):
#         print(a)

# 23

# ------------------------------------------------------------------

# 12:25
# vkvideo.ru/video-205865487_456240494

# def f(x):
#     return ((x%19!=0)or(x%15!=0)) <= (x%a!=0)
# for a in range(1,10000):
#     if all(f(x)==1 for x in range(1,1000000)):
#         print(a)
#         bre 
# 285

# ------------------------------------------------------------------

# 14:39

# def f(x):
#     return ((x%12==0)<=(x%90!=0))or (x+2*a>=512)
# for a in range(1,10000):
#     if all(f(x)==1 for x in range(1,1000000)):
#         print(a)
#         break

# 166

# ------------------------------------------------------------------

# 16:23

# def f(x):
#     return (x%a == 0) or ((70<=x<=80)<= (x%18!=0))
# for a in range(10000,1,-1):
#     if all(f(x)==1 for x in range(1,100000)):
#         print(a) 
#         break

# 72

# ------------------------------------------------------------------

# 22:15

# def f(x):
#     return (a%35==0)and((730%x==0)<=((a%x!=0)<=(110%x!=0)))
# cnt = 0
# for a in range(1,1001):
#     if all(f(x)==1 for x in range(1,1000000)):
#         cnt += 1
# print(cnt)

# 14

# ------------------------------------------------------------------

# 24:30

# def f(x):
#     return(x&29!=0)<=((x&12==0)<=(x&a!=0))
# for a in range(1,1000):
#     if all(f(x)==1 for x in range(1000000)):
#         print(a)
#         break

# 17

# ------------------------------------------------------------------

# 26:00

# def f(x):
    # return((x&673!=0)or(x&189!=0))<=(x&a>0)
# for a in range(1,1000):
    # if all(f(x)==1 for x in range(10**6)):
        # print(a)
        # break

# 701

# ------------------------------------------------------------------

# 30:00

# def f(x,y):
#     return(x*y<3*a)or (x>=31) or(x<5*y)
# for a in range(1,1000):
#     if all(f(x,y) == 1 for x in range(1,1000) for y in range(1,1000)):
#         print(a)
#         break

# 61

# ------------------------------------------------------------------

# 34:40

# def f(x,y):
#     return (x+2*y>a)or(y<x)or(x<30)
# for a in range(1000,1,-1):
#     if all(f(x,y)==1 for x in range(1000)for y in range(1000)):
#         print(a)
#         break

# 89

# ------------------------------------------------------------------

# 38:00

# def f(x,y):
#     return (x>=27)or(2*x<3*y)or(a>(x+2)*(y-3))
# for a in range(1000):
#     if all(f(x,y)==1 for x in range(1000) for y in range(1000)):
#         print(a)
#         break 

# 393

# ------------------------------------------------------------------

# 40:30 

# def poz(n,m):
#     return n-m>0

# def f(x,y):
#     return not poz(x+y,73) or not poz(37,x-y) or poz(y,a)
# for a in range(1000,1,-1):
#     if all(f(x,y)==1 for x in range(1000)for y in range(1000)):
#         print(a)
#         break

# 18

# ------------------------------------------------------------------

# 47:14
  
# def tr(n,m,k):
#     return n+m>k and n+k>m and m+k>n # Формула треугольника
# def f(x):
#     return(tr(a,7,x))<=((max(x+5,14)<=27) == (not tr(36,21,x)))
# for a in range(1000,1,-1):
#     if all(f(x)==1 for x in range(1,10**6)):
#         print(a)
#         break

# 50

# ------------------------------------------------------------------

# 1:07:44

# def f(x):
#     P = 2<=x<=20
#     Q = 15<=x<=25
#     A = a1<=x<=a2
#     return ((not A)<=(not P)) or Q

# ox = [dx for x in (2,15,20,25) for dx in (x,x+0.1,x-0.1)]

# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# Округляем в большую сторону
# 13

# ------------------------------------------------------------------

# 1:13:40

# def f(x):
#     P = 10<=x<=29
#     Q = 13<=x<=18
#     A = a1<=x<=a2
#     return (A<=P)or Q
# ox = [dx for x in(10,29,13,18)for dx in (x,x-0.01,x+0.01)]

# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(max(m))

# 19

# ------------------------------------------------------------------

# 1:17:00

# def f(x):
#     P = 135<=x<=218
#     Q = 174<=x<=308
#     R = 246<=x<=382
#     A = a1<=x<=a2
#     return (not(Q<=(P or R))) <= ((not(A))<= (not(Q)))

# ox = [dx for x in(135,218,174,308,246,382)for dx in (x,x+0.001,x-0.001)]
# m=[]
# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# 28

# ------------------------------------------------------------------

# 1:20:00

# def f(x):
#     B = 36<=x<=75
#     C = 60<=x<=110
#     A = a1<=x<=a2
#     return (not A) <=(B==C)
# ox = [dx for x in(36,75,60,110)for dx in (x,x+0.0001,x-0.0001)]
# m = []
# for a1 in ox: 
#     for a2 in ox: 
#         if a2>=a1 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# 74

# ------------------------------------------------------------------

                        # Множества
            # (Крайне редко встречается на ЕГЭ)

# ------------------------------------------------------------------

# 1:28:30
# Поиск минимального множества

# a = set()

# def f(x):
#     P = x in {2,4,6,8,10,12,14,16,18,20}
#     Q = x in {3,6,9,12,15,18,21,24,27,30}
#     A = x in a
#     return (P<=A) or ((not A)<=(not Q))
# for x in range(1,1000):
#     if f(x)==0:
#         print(x)

# 3

# ------------------------------------------------------------------

# 1:35:00
# Поиск максимального множества

# a = set(range(1,1000))
# def f(x):
#     P = x in {2,4,6,8,10,12,14,16,18,20}
#     Q = x in {5,10,15,20,25,30,35,40,45,50}
#     A = x in a
#     return (A<=P) or ((not Q) <= (not A))
# for x in range(1 ,1000):
#     if f(x)== 0:
#         a.remove(x)
# print(len(a))

# 18

# ------------------------------------------------------------------

# 1:46:00

# def f(x):
#     return(a%5==0) and ((2020%a!=0)<=((x%1718==0)<=(2023%a==0)))

# for a in range(1,10000):
#     if all(f(x)==1 for x in range(1,10**7)):
#         print(a)

#  6

# ------------------------------------------------------------------

# 1:52:00

# from itertools import *

# a = set()

# def f(x):
#     P = x[0]+x[1] =="11"
#     Q = x[-1]=="0"
#     A = x in a
#     return (not A) <= (P or (not Q))
# for x in product("01",repeat=8):
#     if f(x)==0:
#         a.add(x)
# print(len(a))

# 96

# ------------------------------------------------------------------

# 1:55:00

# a = set(range(-1000,1000))
# def f(x):
#     B = x in {-42,-10,-8,2,16}
#     C = x in {-10,-4,2,15,23}
#     A = x in a
#     return (A <= B) or C
# for x in range(-1000,1000):
#     if f(x)==0:
#         a.remove(x)
# print(a)
# print(2+15+16+23)

# 56

# ------------------------------------------------------------------

# Прорешивание не из видео.

# ------------------------------------------------------------------

# def bad(x, y, A):
#     return not ((78125 != y + 4*x) or (A > x and A > y))

# for A in range(1, 100000):
#     ok = True
#     for x in range(1, 20000):
#         y = 78125 - 4*x
#         if y > 0:
#             if x >= A or y >= A:
#                 ok = False
#                 break
#     if ok:
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x):
#     P = 66<=x<=67
#     O = 32<=x<=125
#     T = 30<=x<=491
#     A = a1<=x<=a2
#     return (not A) <= (P or (not O) or (not T))

# ox = [dx for x in(66,67,32,125,30,491) for dx in (x,x+0.0001,x-0.0001)]
# m = []

# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1  and all(f(x) == 1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# ------------------------------------------------------------------
                # Разобрать, не с первого раза понял
# ------------------------------------------------------------------

# def delits(y):  # функция для поиска делителей числа y кроме 1 и y
#     s = set()  # множество делителей
#     for d in range(2, y):  # перебор делителей от 2 до y-1
#         if y % d == 0:  # если d делит y нацело
#             s.add(d)  # добавить d в множество делителей
#     return s  # вернуть множество делителей

# def f(x, y):  # логическая функция
#     C = x in delits(y)  # x принадлежит множеству делителей y кроме 1 и y
#     A = 100 <= x <= 200  # x принадлежит отрезку A
#     B = x in {11, 121}  # B - делители 121 кроме 1 и 121, то есть 11
#     return (not C) or (A and not B)  # импликация по формуле

# for y in range(2, 10**6):  # перебор у по возрастанию
#     if len(delits(y)) > 0 and all(f(x, y) for x in range(1, y+1)):  # проверка требований
#         print(y)  # выводим наименьшее подходящее y
#         break  # завершение поиска

# ------------------------------------------------------------------

# def f(x):
#     P = 25<=x<=64
#     Q = 40<=x<=115
#     A = a1<=x<=a2
#     return (P <=((Q and (not A)) <= (not P)))

# ox = [dx for x in(25,64,40,115) for dx in(x,x+0.001,x-0.001)]
# m = []

# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x)==1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# ------------------------------------------------------------------

# def f(x,A):
#      return (x % 128 == 0) <= ((not (x % A == 0)) <= (not (x % 80 == 0)))
# for A in range(1000,1,-1):
#     if all(f(x,A) for x in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x,y):
#     return (x<A)and(y<3*A)or(2*x+y>128)
# for A in range(1,1000):
#     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x,y):
#     return (2*x+y!=110) or (x<y) or (A<x)
# for A in range(1000,1,-1):
#     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x,y):
#     return (x*y>A) or (x>y) or (11>x)
# for A in range(1000,1,-1):
#     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x,y):
#     return (x**2<=136) or (y<4*x+A-70) or (2*y>51)
# for A in range(1,1000):
#     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x,A):
#     return not ((x & 117 != 0) and (x & 91 == 0)) or (x & A != 0)
# for A in range(1,1000):
#     if all(f(x,A) for x in range(1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x, A):
#     p = str(x)
#     return ((p[0] != '2') and (p[0] == '4')) <= (x > A - 20)

# for A in range(1000, 0, -1):
#     if all(f(x, A) for x in range(1, 10000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x,A):
#     return ((x&52!=0)and(x&48==0)) <= (x&A!=0)
# for A in range(1,1000):
#     if all(f(x,A)for x in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x):
#     B = 36<=x<=75
#     C = 60<=x<=110
#     A = a1<=x<=a2
#     return (not A) <= (B==C)

# ox = [dx for x in (36,75,60,110) for dx in(x,x+0.01,x-0.01)]
# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x) == 1 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# ------------------------------------------------------------------

# def f(x,y,A):
#     return (5<y) or (x>32) or (x+2*y<A)
# for A in range(1,1000):
#     if all(f(x,y,A) for x in range(1,1000)for y in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x) :
#     P = 15<=x<=142
#     Q = 38<=x<=167
#     A = a1<=x<=a2
#     return not(Q <= (((not A) and P) <= (not Q)))
# ox = [dx for x in (15,142,38,167) for dx in(x,x+0.001,x-0.001)] 
# m = []

# for a1 in ox:

#     for a2 in ox:
#         if a2>=a1 and all(f(x)==0 for x in ox):
#             m.append(a2-a1)
# print(min(m))

# ------------------------------------------------------------------

# def f(x):
#     P = 17<=x<=58
#     Q = 29<=x<=80
#     A = a1<=x<=a2
#     return P <= ((Q and not A ) <= (not P))

# ox = [dx for x in(17,58,29,80)for dx in(x,x+0.001,x-0.001)]
# m = []

# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x) for x in ox):
#             m.append(a2-a1)
# print(min(m))

# ------------------------------------------------------------------

# def f(x,A):
#     return  (x&A==0) <= ((x&77==0) and (x&44==0))
# for A in range(1,1000):
#     if all(f(x,A) for x in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

                    # Разобрать ещё раз.

# def d(x, m):
#     return x % m == 0

# def f(x, A):
#     B = 60 <= x <= 80  
#     return d(x, A) or (not B or not d(x, 22))  

# print(max(A for A in range(1, 1001) if all(f(x, A) for x in range(1, 200)))) 

# ------------------------------------------------------------------

# def f(x,A):
#     return (((405%x==0) <=(81%x==0)) or (A-x > 162))
# for A in range(1,1000):
#     if all(f(x,A)for x in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x,y,A):
#     return (9*x + y > A) or (x>=36) or (y>=18)
# for A in range(1000,1,-1):
#     if all(f(x,y,A)for x in range(1,1000)for y in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x,A):
#     return (x&A!=0)<= ((x&698==0) <= (x&321!=0))
# for A in range(10000,1,-1):
#     if all(f(x,A) for x in range(1,10000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x):
#     P = 52<=x<=105
#     Q = 0<=x<=53
#     A = a1<=x<=a2
#     return ((not P) and (not Q) and (not A)) <= (x**2 > 303601)
# ox = [dx for x in (52,105,0,53,551,-551)for dx in(x,x+0.01,x-0.01)]
# m = []
# for a1 in ox:
#     for a2 in ox:
#         if a2>=a1 and all(f(x)for x in ox if x>=0):
#             m.append(a2-a1)
# print(min(m))

# В данном примере необходимо найти корень 303601, и записать как и с остальными точками промежутка
# А так же в конце 445.99 округляем в большую сторону

# 446

# ------------------------------------------------------------------

# def f(x,A):
#     return (A+2*x>400-A) and ((A%100 + 120%A) > 140)
# for A in range(1,1000):
#     if all(f(x,A)for x in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# cnt = 0

# def f(x, A):
#     B = 170<=x<=220
#     return (x % A == 0) or (not B or x % 24 != 0)

# for A in range(1, 300):
#     if all(f(x, A) for x in range(1, 1000)):
#         cnt += 1
# print(cnt)

# ------------------------------------------------------------------

# def f(x,y,A):
#     return (x-3*y<A) or (y>400) or (x>56)
# for A in range(1,1000):
#     if all(f(x,y,A) for x in range(1,1000)for y in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------

# def f(x,y,A):
#     return (y>10) or(x*A>y+x)
# for A in range(1,1000):
#     if all(f(x,y,A) for x in range(1,1000)for y in range(1,1000)):
#         print(A)
#         break

# ------------------------------------------------------------------