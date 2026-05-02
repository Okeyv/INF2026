# def f(curr,end):
#     if curr<end or curr == 73:return 0
#     if curr==end:return 1
#     if curr>end:return f(curr-3,end)+f(curr-8,end)+f(curr//2,end)
# print(f(76,41)*f(41,12))

# 80

# def f(c,e):
#     if c>e or c==7:return 0
#     if c==e:return 1
#     if c<e:return f(c+1,e)+f(c+3,e)+f(c*2,e)
# print(f(2,15)*f(15,25))

#  2716

# def f(c,e):
#     if c<e:return 0
#     if c==e:return 1
#     if c>e:return f(c-1,e)+f(c//2,e)
# print(f(40,16)*f(16,6))

# 60

# def f(c,e):
#     if c<e:return 0
#     if c==e:return 1
#     if c>e:return f(c-1,e)+f(c//2,e)
# print(f(40,17)*f(17,6))

# 56

# def f(c,e):
#     if c>e:return 0 
#     if c==e:return 1
#     if c<e:return f(c+1,e)+f(c+5,e)+f(c*3,e)
# for i in range(2,100):
#     if f(1,i) == 175:
#         print(i)

# 19

# def f(c,e,s):
#     if c>e:return 0
#     if c==e and s==6:return 1
#     if c==e and s!=6:return 0
#     if c<e:return f(c+1,e,s+1)+f(c+2,e,s+1)+f(c*2,e,s+1)
# print(f(1,20,0))

# 36

# from functools import *
# @lru_cache(None)
# def f(c,e,s):
#     if c>e:return 10**8
#     if c==e:return s
#     if c<e:return min(f(c+1,e,s+1),f(c+5,e,s+1),f(c*3,e,s+1))
# print(f(1,227,0))

# 7

# d = set()
# def f(c,s):
#     if s == 4: d.add(c)
#     else:
#         f(c+1,s+1)
#         f(c+5,s+1)
#         f(c*3,s+1)
# f(1,0)
# print(len(d))

# 43

# d = set()
# def f(c):
#     if c>=100:return 0
#     if c<100 and c%2==0: d.add(c)
#     if c<100:
#         f(c+3)
#         f(c*3)
# f(3)
# print(len(d))

#  OR

# def f(c,e):
#     if c>e:return 0
#     if c==e:return 1
#     if c<e:return f(c+3,e)+f(c*3,e)
# k = 0
# for i in range(4,100,2):
#     if f(3,i)!=0:
#         k+=1
# print(k)

# 16

# Подсчёт чисел

# def f(c,e,k):
#     if c%2!=0: k+=1
#     if c>e:return 0
#     if c==e:return k <=7
#     if c<e:return f(c+2,e,k)+f(c*2,e,k)+f(c*3,e,k)
# print(f(1,214,0))

# 69408


# def f(c,e):
#     if c>e  or c == 14: return 0
#     if c==e:return 1
#     if c<e: return f(c+1,e)+f(c*2,e)+f(c*3,e)
# print(f(2,39))

# 188

# def f(c,e):
#     if c<e or c == 73:return 0 
#     if c==e :return 1
#     if c>e: return f(c-3,e)+f(c-8,e)+f(c//2,e)
# print(f(76,41)*f(41,12))

# 80

# def f(c,e):
#     if c>e or c == 7:return 0
#     if c==e :return 1
#     if c<e:return f(c+1,e)+f(c+3,e)+f(c*2,e)
# print(f(2,15)*f(15,25))

# 2716

# def f(c,e):
#     if c<e:return 0
#     if c==e:return 1
#     if c>e:return f(c-1,e)+f(c//2,e)
# print(f(40,16)*f(16,6))

# 60

# def f(c,e):
#     if c<e:return 0
#     if c==e:return 1
#     if c>e:return f(c-1,e)+f(c//2,e)
# print(f(40,17)*f(17,6))

# 56

# def f(c,e):
#     if c>e or c ==28 or c == 36:return 0
#     if c==e:return 1
#     if c<e:return f(c+1,e)+f(c+5,e)+f(c*3,e)
# p18 =f(2,18)*f(18,49)
# p30 =f(2,30)*f(30,49)
# Pmerget = f(2,18)*f(18,30)*f(30,49)
# # Формула включений-исключений: A ∪ B = A + B - A ∩ B
# result = p18+p30-Pmerget
# print(result)

# 76978

# def f(c,e):
#     if c>e or c==20 or c==33:return 0
#     if c==e:return 1
#     if c<e:return f(c+3,e)+f(c+4,e)+f(c*2,e)
# p15 = f(3,15)*f(15,63)
# p26 = f(3,26)*f(26,63)
# merget = f(3,15)*f(15,26)*f(26,63)
# print(p15+p26-merget)

# 23570

# def f(c,e):
#     if c<e:return 0
#     if c==e:return 1
#     if c>e:return f(c-1,e)+f(c//2,e)+f(c//3,e)
# p48 = f(106,48)*f(48,6)
# p61 = f(106,61)*f(61,6)
# merget = f(106,61)*f(61,48)*f(48,6)
# print(p48+p61-2*merget)

# 4128

# def f(c,e):
#     if c<e:return 0
#     if c==e:return 1
#     if c>e:return f(c-2,e)+f(c-3,e)+f(c//5,e)
# p25 = f(63,25)*f(25,3)
# p47 = f(63,47)*f(47,3)
# merget = f(63,47)*f(47,25)*f(25,3)
# print(p25+p47-2*merget)

# 4715761

# def f(c,e):
#     if c<e:return 0
#     if c==e:return 1
#     if c>e:return f(c-3,e)+f(c-4,e)+f(c//2,e)
# p30= f(78,30)*f(30,2)
# p42= f(78,42)*f(42,2)
# merget = f(78,42)*f(42,30)*f(30,2)

# print(p30+p42-merget)

# 3465397

# def f(c,e):
#     if c<e:return 0
#     if c==e:return 1
#     if c>e:return f(c-3,e)+f(c-5,e)+f(c//3,e)
# p18= f(80,18)*f(18,3)
# p38= f(80,38)*f(38,3)
# merget= f(80,38)*f(38,18)*f(18,3)
# print(p18+p38-merget)

# 206151

# def f(c,e):
#     if c>e :return 0
#     if c==e:return 1
#     if c<e:return f(c*2,e)+f(c**2,e)+f(c**3,e)
# # print(f(2,131072))
# ans1 = f(2,131072)
# ans2 = f(2,4)*f(4,16)*f(16,131072)
# print(ans1-ans2)

# 32

# def f(c,e):
#     if c<e :return 0
#     if c==e:return 1
#     if c>e:return f(c//3,e)+f(c-3,e)
# ans1 = f(68,4)
# ans2 = f(68,22)*f(22,7)*f(7,4)
# print(ans1-ans2)

# 18

# def f(c,e,no):
#     if c>e or c==no:return 0
#     if c==e:return 1
#     if c<e:return f(c+1,e,no)+f(c+2,e,no)+f(c+4,e,no)+f(c+8,e,no)
# ans1 = f(16,24,32)*f(24,48,32)
# ans2 = f(16,32,24)*f(32,48,24)
# print(ans1+ans2)

# 22681617

# def f(c,e,no):
#     if c<e or c==no:return 0
#     if c==e:return 1
#     if c>e:return f(c-1,e,no)+f(c-3,e,no)+f(c//3,e,no)
# ans1 = f(49,40,20)*f(40,30,20)*f(30,12,20)
# ans2 = f(49,40,30)*f(40,20,30)*f(20,12,30)
# ans3 = f(49,30,40)*f(30,20,40)*f(20,12,40)
# ans4 = f(49,40,-1)*f(40,30,-1)*f(30,20,-1)*f(20,12,-1)
# print(ans1+ans2+ans3+ans4)

# 562318

# def f(c,e):
#     if c<e or c==7:return 0
#     if c==e:return 1
#     if c>e:return f(c-1,e)+f(c-4,e)+f(c//3,e)
# print(f(19,13)*f(13,2))

# 68

# def f(c,e):
#     if c>e+100 or c%3==0: return 0
#     if c==e:return 1
#     return f(c-1,e)+f(c+3,e)+f(c*2,e)
# print(f(5,100))

# 21133

# def f(c,e):
#     if c<e:return 0
#     if c==e:return 1
#     if c>e:return f(c-2,e)+f(c//2,e)
# print(f(48,16)*f(16,2))

# 72

# def f(c,e):
#     if c>e or c==10:return 0
#     if c==e:return 1
#     return f(c+1,e)+f(c+2,e)+f(c*2,e)
# print(f(3,7)*f(7,20))

# 792

# def f(c,e):
#     if c<e or c== 8:return 0
#     if c==e:return 1
#     return f(c-1,e)+f(c-4,e)+f(c//3,e)
# print(f(19,14)*f(14,2))

# 69

# def f(c,e):
#     if c<e or c==13:return 0
#     if c==e:return 1
#     return f(c-1,e)+f(c-2,e)+f(c//3,e)
# print(f(19,6)*f(6,4))

# 212

# def f(c,e):
#     if c>e or c==27:return 0 
#     if c==e:return 1
#     return f(c+3,e)+f(c+5,e)+f(c**2,e)
# print(f(3,16)*f(16,51))

# 225

# def f(c,e):
#     if c>e or c==8:return 0
#     if c==e:return 1
#     return f(c+1,e)+f(c+2,e)+f(c*2,e)
# print(f(3,14)*f(14,18))

# 360

# def f(c,e):
#     if c>e or c==56:return 0
#     if c==e:return 1
#     return f(c+3,e)+f(c+7,e)+f(c*3,e)
# print(f(12,40)*f(40,72)*f(72,89))

# 324

# def f(c,e):
#     if c>e or c==35:return 0
#     if c==e:return 1
#     return f(c+1,e)+f(c+2,e)+f(c*2,e) 
# print(f(7,13)*f(13,15)*f(15,51))

# 174034068


