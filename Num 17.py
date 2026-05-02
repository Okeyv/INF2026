## Перебор пар идущий подряд
## a=[3,4,2,3,4,4]
# a = [int(x) for x in open("17-3.txt")]
# for i in range(len(a)-1):
#     x,y= a[i],a[i+1]
#     print(x,y)


# a =   [5,  35,-15,7,5]
#   #    |   |   |  | 
#   #    v   v   v  v 
# #a[:1][35,-15, 7, 5]
# for x,y in zip(a,a[1:]):
#     print(x,y)

# ------------------------------------------------------------------

# a = [int(x) for x in open("17-3.txt")]
# ans = []
# for i in range(len(a)-1):
#     x,y= a[i],a[i+1]
#     if x*y>0 and (x+y)%7==0:
#         ans.append(x*y)
# print(len(ans),min(ans))

# 359 115022

# a = [int(x) for x in open("17-5.txt")]
# ans = []

# for x,y in zip(a,a[1:]):
#     if abs(x)%10==5 and abs(y)%10==5:
#         ans.append(x+y)
# print(len(ans),max(ans))

# 1 40

# a = [int(x) for x in open("17-5.txt")]
# avg = sum(a)/len(a) # Среднее арифметическое 
# ans = []
# for x,y in zip(a,a[1:]):
#     if x<avg and y<avg and (x+y)%100==19:
#         ans.append(x+y) 
# print(len(ans),min(ans))

# 6 4519


# a = [int(x) for x in open("17-243.txt")]
# mx = max([x for x in a if x%71==0])
# ans = []
# for x,y in zip(a,a[1:]):
#     if x<mx and y<mx and(x%13==0 or y%13==0):
#         ans.append(x+y)
# print(len(ans),min(ans))

# 1445 2447


# a = [int(x) for x in open("17-282.txt")]
# m = min([x for x in a if x%17==0])
# ans = []
# for x,y in zip(a,a[1:]):
#     if x%m==0 or y%m==0:
#         ans.append(x+y)
# print(len(ans),max(ans))

# 24 17613

# a = [int(x) for x in open("17-339.txt")]
# m = min([x for x in a if x>0 and x%19==0])
# ans = []
# for x,y in zip(a,a[1:]):
#     if (x+y)<m:
#         ans.append(x+y)
# print(len(ans),abs(max(ans)))

# 4969 696

# a = [int(x) for x in open("17-3.txt")]
# ans = []
# for x,y,z in zip(a,a[1:],a[2:]):
#     if x*y*z%7==0 and abs(x+y+z)%10==5:
#         ans.append(x+y+z)
# print(len(ans),max(ans))

# 153 19285

# a = [int(x) for x in open("17-380.txt")]
# ans = []
# m = max([x for x in a if abs(x)%100==25])
# for x,y,z in zip(a,a[1:],a[2:]):
#     if (1000<=abs(x)<10000)+(1000<=abs(y)<10000)+(1000<=abs(z)<10000)<=2 and x+y+z<=m:
#         ans.append(x+y+z)
# print(len(ans),max(ans))

# 6315 84523

# a = [int(x) for x in open("17-407.txt")]
# k = len([x for x in a if x%32==0])
# ans = []
# for x,y in zip(a,a[1:]):
#     if (x<0 or y<0) and x+y<k:
#         ans.append(x+y)
# print(len(ans),max(ans))

# 4969 299

# a = [int(x) for x in open("17-426.txt")]
# def check(n):
#     return 10000<=abs(n)<=100000 and abs(n)%100==43

# m = max([x for x in a if check(x)])
# ans = []
# for x,y,z in zip(a,a[1:],a[2:]):
#     if (check(x) or check(y) or check(z)) and (x**2+y**2+z**2) <= m**2:
#         ans.append(x**2+y**2+z**2)
# print(len(ans),min(ans))

# 92 838850571

# a = [int(x) for x in open("17-433.txt")]
# m =min([x for x in a if 100<=abs(x)<=1000 and abs(x)%100==15])
# ans = []
# for x,y,z in zip(a,a[1:],a[2:]):
#     mn = min(x,y,z)
#     mx = max(x,y,z)
#     # b1,b2,b3 = sorted([x,y,z])
#     if (x>=0 and y>=0 and z>=0 or x<0 and y<0 and z<0) and mn*mx>m**2:
#         ans.append(mn*mx)
# print(len(ans),min(ans))

# 3507 863808

 
# a = [int(x) for x in open("17-428.txt")]
# mn = min(a)
# mx = max(a)
# def ch1(x,y,z):
#     return 1000<=x<=10000 or  1000<=y<=10000 or 1000<=z<=10000
# def ch2(x,y,z):
#     return (x%11==mn%11)+(y%11==mn%11)+(z%11==mn%11)<=1
# def ch3(x,y,z):
#     return (x%7==mx%7)+(y%7==mx%7)+(z%7==mx%7)<=2
# ans = []
# for x,y,z in zip(a,a[1:],a[2:]):
#     if ch1(x,y,z) and ch2(x,y,z) and ch3(x,y,z):
#         ans.append(x+y+z)
# print(len(ans), sum(ans)/len(ans))

# sum(ans)/len(ans) # Среднее арифмитическое сумм троек

# 589 38508

# a = [int(x) for x in open("17-243.txt")]
# s = sum([int(d) for x in a for d in str(x) if x%61==0])
# ans = []
# for x,y in zip(a,a[1:]):
#     if (x>s)+(y<s) == 1 and (x>s and y%100==33 or y>s and x%100==33): 
#         ans.append(x+y)
# print(len(ans),min(ans))

# 41 5182

# a = [int(x) for x in open("17-199.txt")]
# ans = []
# def ch(n):
#     return n>0 and 10<=n<100 and n%2==0
# for x,y,z in zip(a,a[1:],a[2:]):
#     if not(ch(x)) and ch(y) and not(ch(z)):
#         ans.append(x+y+z)
# print(len(ans),max(ans))

# 7 12441

# a = [int(x) for x in open("17-Files/29349.txt")]
# min_val = min(x for x in a if x > 0 and x % 123 == 0)
# ans = []
# for x, y in zip(a, a[1:]):
#     if x + y < min_val:
#         ans.append(x + y)
# print(len(ans), abs(max(ans)))

# 5001 962

# a = [int(x) for x in open("17-Files/28938.txt")]
# def ch(n):
#     return 100<=abs(n)<=999     
# mx = max([x for x in a if abs(x)%100==28])
# ans = []
# for x,y,z in zip(a,a[1:],a[2:]):
#     if ch(x) or ch(y) or ch(z):
#         if (x+y+z)/3 > 0 and (x+y+z)/3 < mx:
#             ans.append(x+y+z)
# print(len(ans),max(ans))

# 1290 193483

# a = [int(x) for x in open("17-Files/28762.txt")]
# mn = min([x for x in a if x%23==0])
# ans = []
# for x,y in zip(a,a[1:]):
#     if x%mn==0 or y%mn==0:
#         ans.append(x+y)
# print(len(ans),max(ans))

# 113 168437

# a = [int(x) for x in open("17-Files/27629.txt")]
# def ch(n):
#     return 1000<=abs(n)<10000
# mx = max([x for x in a if ch(x) and abs(x)%100==43])
# ans = []
# for x,y in zip(a,a[1:]):
#     if ch(x) or ch(y):
#         if (x+y)**2< mx**2:
#             ans.append((x+y)**2)
# print(len(ans),max(ans))

# 1218 98843364

# a = [int(x) for x in open("17-Files/27301.txt")]
# mx = max([x for x in a if str(abs(x)).startswith('45')])
# num1 = [] 
# num2 = []
# for x, y, z in zip(a, a[1:], a[2:]):
#     if (x < 0) + (y < 0) + (z < 0) == 1:
#         s = x + y + z
#         if s >= mx:
#             num1.append(s)
#             if abs(s) % 100 == 45:
#                 num2.append(s)
# print(len(num1), min(num2))
# 1588 49345

# a = [int(x) for x in open("17-Files/27300.txt")]
# ans = []
# mx = max([x for x in a if abs(x)%100==11])
# for x,y,z in zip(a,a[1:],a[2:]):
#     if x>0 and y>0 and z>0:
#         if (x+y+z) >= mx:
#             ans.append(x+y+z)
# print(len(ans),min(ans))

# 879 97103

# a = [int(x) for x in open("17-Files/27299.txt")]
# def ch(n):
#    return 100<=abs(n)<1000 and abs(n)%2==0
# mn = min([x for x in a if 1000<=x<10000])
# ans = []
# for x,y,z in zip(a,a[1:],a[2:]):
#     if (ch(x))+(ch(y))+(ch(z))>=2:
#         if (x+y+z)>=mn:
#             ans.append(x+y+z)
# print(len(ans),min(ans))

# 16 1571

# a = [int(x) for x in open("17-Files/25356.txt")]
# def ch(n):
#     return 1000<=abs(n)<=10000
# mx = max([x for x in a if abs(x)%100==30])
# ans = []
# for x,y,z, in zip(a,a[1:],a[2:]):
#     if (ch(x))+(ch(y))+(ch(z))==0:
#         if (x+y+z)>=mx:
#             ans.append(x+y+z)
# print(len(ans),max(ans))

# 1032 285423

# a = [int(x) for x in open("17-Files/24892.txt")]
# ans = []
# mx = max([x for x in a if -10000<x<=-1000 and x%9==0])
# for x,y in zip(a,a[1:]):
#     if (x<0)+(y<0)==1:
#         if (x+y)>mx:
#             ans.append(x**2+y**2)
# print(len(ans),min(ans))

# 2627 504410

# a = [int(x) for x in open("17-Files/23757.txt")]
# ans = []
# def ch(n):
#     return 10<=abs(n)<100
# mn = min([x for x in a if ch(x)])
# for x,y in zip(a,a[1:]):
#     if (ch(x))+(ch(y))==1:
#         if (x+y)%mn==0:
#             ans.append(x+y)
# print(len(ans),max(ans))

# 150 9930

# a = [int(x) for x in open("17-Files/23563.txt")]
# mn = min([x for x in a if x>0 and abs(x)%35==0])
# ans = []
# for x,y in zip(a,a[1:]):
#     if x!=y:
#         if (abs(x-y))%mn==0:
#             ans.append(x+y)
# print(len(ans),max(ans))

# 87 184328

# a = [int(x) for x in open("17-Files/23376.txt")]
# def ch(n):
#     return 10000<=abs(n)<100000
# mx = max([x for x in a if ch(x) and abs(x)%100==37])
# ans = []
# for x,y in zip(a,a[1:]):
#     if (ch(x))+(ch(y))==1:
#         if (x+y)**2> mx**2:
#             ans.append(x+y)
# print(len(ans),max(ans))

# 350 107294

# a = [int(x) for x in open("17-Files/23276.txt")]
# def ch(n):
#     return 1000<=abs(n)<10000
# mx = max([x for x in a if abs(x)%100==25])
# ans = []
# for x,y,z in zip(a,a[1:],a[2:]):
#     if ch(x)+ch(y)+ch(z)<=2:
#         if (x+y+z)<=mx:
#             ans.append(x+y+z)
# print(len(ans),max(ans))

# 6315 84523

# a = [int(x)for x in open("17-Files/23201.txt")]
# def ch(n):
#     return 100<=n<1000
# mn = min([x for x in a if ch(x) and x%10==7] )
# ans = []
# for x,y in zip(a,a[1:]):
#     if ch(x)+ch(y)==1:
#         if (x+y)%mn==0:
#             ans.append(x+y)
# print(len(ans),min(ans)) 

# 9 107

# a = [int(x) for x in open("17-Files/21903.txt")]
# mn = min([x for x in a if abs(x)%100==15 and 100<=abs(x)<1000])
# ans = []
# for x,y,z in zip(a,a[1:],a[2:]):
#     if (x>0)+(y>0)+(z>0)==3 or (x<0)+(y<0)+(z<0)==3:
#         minx = min(x,y,z)
#         maxx = max(x,y,z)
#         if (minx*maxx)>=mn**2:
#             ans.append(minx*maxx)
# print(len(ans),min(ans))

# 3507 863808

# a = [int(x) for x in open("17-Files/21712.txt")]
# def ch(n):
#     return 1000<=abs(n)<10000 and abs(n)%10==6
# ans = []
# mn = min([x for x in a if 1000<=x<10000 and x%10==6])
# for x,y,z in zip(a,a[1:],a[2:]):
#     if ch(x)+ch(y)+ch(z) == 1:
#         if (x+y+z)<=mn:
#             ans.append(x+y+z)
# print(len(ans),max(ans))

# 507 1042

# a = [int(x) for x in open("17-Files/21595.txt")]
# ans = []
# m = [x for x in a if 1000<=abs(x)<10000 and abs(x)%10==3]
# for x,y,z in zip(a,a[1:],a[2:]):
#     sorte = [x,y,z]
#     sorte.sort()
#     if int(sorte[1])+int(sorte[2])>m**2:
#         ans.append(x+y+z)
# print(len(ans),max(abs(ans)))

        