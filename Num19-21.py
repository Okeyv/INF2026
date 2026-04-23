# ------------------------------------------------------------------

# Базовый код для одной куче камней

def f(s,m):
    if s<16 :return m%2==0
    if m == 0:return 0
    h = [f(s-3,m-1),f(s-8,m-1),f(s//3,m-1)]
    return any(h) if m%2!=0 else all(h)
print("19",*[s for s in range(16,300)if f(s,2)])
print("20",*[s for s in range(16,300)if not f(s,1)and f(s,3)])
print("21",*[s for s in range(16,300)if not f(s,2)and f(s,4)])

# Меняется только значения в 'h', но в ней переменная 'm-1', всегда такая.
# А так же меняется условие if "s<16"
# И подстраивается вывод под определенные значения , все это в списке, тоесть из print, меняется только range

# ------------------------------------------------------------------

# 2 КУЧИ

# def f(a,b,m):
#     if a*b >= 63: return m%2==0
#     if m == 0 :return 0
#     h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#     return any(h) if m%2 != 0 else all(h)
# print("19",[s for s in range(1,32)if f(2,s,2)])
# print("20",[s for s in range(1,32)if not f(2,s,1) and f(2,s,3)])
# print("21",[s for s in range(1,32)if not f(2,s,2) and f(2,s,4)])

# В некоторых заданиях просят произведение куч, тоесть мы пишем if a*b>= 63
# А обычно мы просто складываем кучи, то есть if a+b>= 63
# Первая буква в f(2,s,2) это буквально переменная "a". почему 2? Потому что нам в условии сказали, что в первоначальный момент в куче было 2 камня
# a - первая куча
# b - вторая куча

# ------------------------------------------------------------------

# ДВЕ КУЧИ / НЕУДАЧНЫЙ ХОД В 19

# from math import ceil
# def f(a,b,m):
#     if a+b<=108:return m%2 ==0
#     if m == 0:return 0 
#     h = [f(a-2,b,m-1),f(a,b-2,m-1),f(ceil(a/2),b,m-1),f(a,ceil(b/2),m-1)]
#     # return any(h) if m%2!=0 else any(h) # ДЛЯ 19 НЕУДАЧНЫЙ ХОД
#     return any(h) if m%2!=0 else all(h) # ДЛЯ 20-21 ОБЫЧНЫЙ ХОД 

# print("19",max([s for s in range(49,200)if f(60,s,2)]))
# print("20",[s for s in range(49,200)if not f(60,s,1) and f(60,s,3)])
# print("21",max([s for s in range(49,200)if not f(60,s,2) and f(60,s,4)]))

# ------------------------------------------------------------------

# def f(s, m):
#     if s >= 231: return m % 2 == 0  # Если достигли или превысили порог — выигрывает тот, кто последний ходил
#     if m == 0: return 0             # Если ходы закончились — проигрыш
#     h = []                          # Массив возможных ходов
#     if m % 2 != 0:                  # Ходит Петя (1 и 3 ход)
#         h.append(f(s + 3, m - 1))
#         h.append(f(s * 3, m - 1))
#     else:                           # Ходит Ваня (2 и 4 ход)
#         h.append(f(s + 5, m - 1))
#         h.append(f(s * 3, m - 1))
#     return any(h) if m % 2 != 0 else all(h)  # Для нечётного m — хотя бы один ход, для чётного — все ходы

# print("19)", [s for s in range(10, 121) if not f(s,1) and f(s,2)])  # 19 задание: Ваня выигрывает первым ходом, а Петя не может своим первым
# print("20)", [s for s in range(10, 121) if not f(s,1) and f(s,3)]) # 20 задание: Петя выигрывает своим вторым ходом, не выигрывая первым
# print("21)", [s for s in range(10, 121) if not f(s,2) and f(s,4)]) # 21 задание: Ваня не выигрывает за два, но выигрывает за четыреot f(s,2) and f(s,4)]))

# ------------------------------------------------------------------
# from functools import *
# def moves(s):
#     return s+2,s+4,s*2
# @lru_cache(None)
# def game(s):
#     if s>=125: return "w"
#     if any(game(i)=="w" for i in moves(s)): return "p1"
#     if all(game(i)=="p1" for i in moves(s)): return "v1"
#     if any(game(i)=="v1" for i in moves(s)): return "p2"
#     if all(game(i) in ["p1", "p2"] for i in moves(s)): return "v2"
# print(19,[s for s in range(1,125) if game(s) == "v1"])
# print(20,[s for s in range(1,125)if game(s) == "p2"])
# print(21,[s for s in range(1,125)if game(s) == "v2"])

# ------------------------------------------------------------------

# def moves(s): return s+2,s+4,s*2
# def w(s): return s>=125
# def p1(s): return not w(s) and any(w(i) for i in moves(s))
# def v1(s): return all(p1(i) for i in moves(s))
# def p2(s): return any(v1(i) for i in moves(s))
# def v2(s): return not v1(s) and all(p2(i) or p1(i) for i in moves(s))

# print("p1",[s for s in range(1,125) if p1(s)])
# print("v1",[s for s in range(1,125) if v1(s)])
# print("p2",[s for s in range(1,125)if p2(s)])
# print("v2",[s for s in range(1,125)if v2(s)])

# ------------------------------------------------------------------

# def f(s,m):
#     if s >= 51: return m%2==0
#     if m == 0 :return 0
#     h = [f(s+1,m-1),f(s+4,m-1),f(s*2,m-1)]
#     return any(h) if m%2 != 0 else all(h)
# print("19",[s for s in range(1,51)if f(s,2)])
# print("20",[s for s in range(1,51)if not f(s,1) and f(s,3)])
# print("21",[s for s in range(1,51)if not f(s,2) and f(s,4)])


# def f(a,b,m):
#     if a+b>=131:return m%2==0
#     if m==0:return 0
#     h = [f(a+2,b,m-1),f(a,b+2,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#     return any(h) if m%2!=0 else any(h)

# print("19",[s for s in range(1,119) if f(11,s,2)])
# # print("20",[s for s in range(1,119) if not f(11,s,1) and f(11,s,3)])
# # print("21",[s for s in range(1,119) if not f(11,s,2) and f(11,s,4)])

# ------------------------------------------------------------------

# def f(a,b,m):
#     if a+b>=122:return m%2 ==0
#     if m == 0:return 0
#     h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#     return any(h) if m%2!=0 else all(h)

# # print(19,[s for s in range(1,100) if f(22,s,2)])
# print(20,[s for s in range(1,100) if not f(22,s,1) and f(22,s,3)])
# print(21,[s for s in range(1,100) if not f(22,s,2) and f(22,s,4)])

# ------------------------------------------------------------------

# def f(s,m):
#     if s == 42: return m % 2 == 0
#     if s > 42: return m % 2 != 0
#     if m == 0:return 0
#     h = [f(s+1,m-1),f(s+3,m-1),f(s+7,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(19,[s for s in range(1,43)if f(s,2)])
# print(20,[s for s in range(1,43)if not f(s,1)and f(s,3)])
# print(21,[s for s in range(1,43)if not f(s,2)and f(s,4)])

# ------------------------------------------------------------------

# def f(s,m):
#     if s > 125 :return m%2==0
#     if s ==125 :return m%2!=0
#     if m == 0 :return 0
#     h = [f(s+2,m-1),f(s+4,m-1),f(s*2,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(19,[s for s in range(1,125)if f(s,2)])
# print(20,[s for s in range(1,125)if not f(s,1)and f(s,3)])
# print(21,[s for s in range(1,125)if not f(s,2)and f(s,4)])

# ------------------------------------------------------------------

# def f(s, m):
#     if s <= 15: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s - 3, m - 1), f(s - 8, m - 1), f(s // 3, m - 1)]    
#     return any(h) if m % 2 != 0 else all(h)

# print(19,[s for s in range(16, 100) if f(s, 2)])
# print(20,[s for s in range(16, 100) if not f(s, 1) and f(s,3)])
# print(21,[s for s in range(16, 100) if not f(s, 2) and f(s,4)])

# ------------------------------------------------------------------

# def f(s,m):
#     if s <= 27 : return m%2==0
#     if m == 0: return 0
#     h = [f(s-3,m-1),f(s-6,m-1),f(s//3,m-1)] 
#     return any(h) if m%2!=0 else all(h)
# print((19),[s for s in range(28,150)if not f(s,1) and f(s,2)])  
# print((20),[s for s in range(28,150)if not f(s,1) and f(s,3)])
# print((21),[s for s in range(28,150)if not f(s,2) and f(s,4)])

# ------------------------------------------------------------------

# from math import ceil
# def f(a,b,m):
#     if a+b<=200:return m%2==0
#     if m==0:return 0
#     h = [f(a-3,b-4,m-1),f(a-8,b//2,m-1),f(ceil(a//2),b-10,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print("19)", [s for s in range(100, 301) if not f(110, s, 1) and f(110, s, 2)])
# print("19)", [s for s in range(100, 301) if not f(110, s, 1) and f(110, s, 3)])
# print("19)", [s for s in range(100, 301) if not f(110, s, 2) and f(110, s, 4)])

# ------------------------------------------------------------------

# def f(a,b,m):
#     if a*b>=516:return m%2==0
#     if m==0:return 0
#     h = [f(a+3,b,m-1),f(a,b+3,m-1),f(a+13,b,m-1),f(a,b+13,m-1)]
#     return any(h) if m%2!=0 else all(h)
#     # return any(h) # Для 19 номера отдельно
# print(19,len([s for s in range(1,74)if f(7,s,2)]))
# print(20,[s for s in range(1,74)if not f(7,s,1) and f(7,s,3)])
# print(21,[s for s in range(1,74)if not f(7,s,2) and f(7,s,4)])

# ------------------------------------------------------------------

# def f(a,b,m):
    # if a+b>=207:return m%2==0
    # if m == 0:return 0
    # h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
    # return any(h) if m%2!=0 else all(h)
    # return any(h)
# print(19,[s for s in range(1,190) if f(17,s,2)])
# print(20,[s for s in range(1,190) if not f(17,s,1) and f(17,s,3)])
# print(21,[s for s in range(1,190) if not f(17,s,2) and f(17,s,4)])

# 19   48
# 20   86 94
# 21   85 

# ------------------------------------------------------------------

# def f(a,b,m):
#     if a+b>=211:return m%2==0
#     if m == 0:return 0
#     h = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
#     # return any(h) if m%2!=0 else all(h)
#     return any(h) 
# print(19,[s for s in range(1,194)if f(17,s,2)])
# # print(20,[s for s in range(1,194)if not f(17,s,1)and f(17,s,3)])
# # print(21,[s for s in range(1,194)if not f(17,s,2)and f(17,s,4)])

# 19 49
# 20 88 96
# 21 87

# ------------------------------------------------------------------

# №  ЕГКР 13.12.25 (Уровень: Базовый) 

# def f(s,m):
#     if s>125:return m%2==0
#     if m==0:return 0
#     h = [f(s+2,m-1),f(s+4,m-1),f(s*2,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(19,[s for s in range(1,125) if f(s,2)])
# print(19,[s for s in range(1,125) if not f(s,1)and f(s,3)])
# print(19,[s for s in range(1,125) if not f(s,2)and f(s,4)])

# 61
# 31 57
# 55

# ------------------------------------------------------------------

# def f(s,m):
#     if s<31:return m%2==0
#     if m==0:return 0
#     h = [f(s-3,m-1),f(s-5,m-1),f(s//4,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(19,[s for s in range(31,200) if not f(s,1) and f(s,2)])
# print(19,[s for s in range(31,300) if not f(s,1) and f(s,3)])
# print(19,[s for s in range(31,300) if not f(s,2) and f(s,4)])

# 124
# 127 128
# 132

# ------------------------------------------------------------------

# def f(s,m):
#     if s<16 :return m%2==0
#     if m == 0:return 0
#     h = [f(s-3,m-1),f(s-8,m-1),f(s//3,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(19,[s for s in range(16,300)if f(s,2)])
# print(20,[s for s in range(16,300)if not f(s,1)and f(s,3)])
# print(21,[s for s in range(16,300)if not f(s,2)and f(s,4)])

# 48
# 51 52
# 54

# ------------------------------------------------------------------

# def f(s,m,step):
#     if s>=231:return m%2==0
#     if m==0:return 0
#     if step == "P":
#         h = [f(s+3,m-1,'V'),f(s*3,m-1,'V')]
#     else:
#         h = [f(s+5,m-1,'P'),f(s*3,m-1,'P')]

#     return any(h) if m%2!=0 else all(h)
# print('19)',min(i for i in range(10,121) if f(i,2,'P')))
# print('20)',*[i for i in range(10,121) if f(i,3,'P') and (not(f(i,1,'P')))][:2])
# print('21)',max(i for i in range(10,121 ) if f(i,4,'P') and (not(f(i,2,'P')))))

#  74
#  24 25
#  68

# ------------------------------------------------------------------

# def f(s,m):
#     if s<=27:return m%2==0
#     if m==0:return 0
#     h = [f(s-3,m-1),f(s-6,m-1),f(s//3,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(min([s for s in range(28,300)if f(s,2)]))
# print(*[s for s in range(28,300)if not f(s,1) and f(s,3)][:2])
# print(min([s for s in range(28,300)if not f(s,2) and f(s,4)]))

# 84
# 87 88
# 93

# ------------------------------------------------------------------

# from math import *
# def f(a,b,m):
#     if a+b<=200:return m%2==0
#     if m==0:return 0
#     h = [f(a-3,b-4,m-1),f(a-8,b//2,m-1),f(ceil(a/2),b-10,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(min([s for s in range(100,400)if f(110,s,2)]))
# print(*[s for s in range(100,400)if not f(110,s,1) and f(110,s,3)][:2])
# print(min([s for s in range(100,400)if not f(110,s,2) and f(110,s,4)]))

# 198
# 208 209
# 218

# ------------------------------------------------------------------

# Какие ещё простые числа??? Отстань.

# from math import *
# def is_simple(n):
#     if n == 1:
#         return False
#     for i in range(2,int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# def f(a,m):
#     if is_simple(a): return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a * 2,m - 1),f(a + 3,m - 1),f(a + 1,m - 1)]
#     return any(h) if m % 2 else all(h)


# print('19)', min([i for i in range(1,101) if f(i,2) and not(f(i,0))])) #так как число изначально
# #может оказаться простым и тогда победа на 0-м ходе зачтётся как победа на 2-м, то пишем not(f(i,0))
# print('20)', *[i for i in range(1,101) if f(i,3) and (not f(i,1))][-2:])
# print('21)', max([i for i in range(1,101) if f(i,4) and (not f(i,2)) and not(f(i,0))]))

# ------------------------------------------------------------------

# def f(s,m):
#     if s<=16:return m%2==0
#     if m==0:return 0 
#     h = [f(s-3,m-1),f(s-8,m-1),f(s//3,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(min([s for s in range(17,400)if f(s,2)]))
# print(*[s for s in range(17,400)if not f(s,1) and f(s,3)][:2])
# print(min([s for s in range(17,400)if not f(s,2) and f(s,4)]))

# 51
# 54 55
# 57

# ------------------------------------------------------------------

# def f(s,m):
#     if s<=11:return m%2==0
#     if m==0:return 0
#     h = [f(s-3,m-1),f(s-7,m-1),f(s//3,m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(min([s for s in range(12,300)if f(s,2)]))
# print(*[s for s in range(12,300)if not f(s,1) and f(s,3)][:2])
# print(min([s for s in range(12,300)if not f(s,2) and f(s,4)]))

# 36
# 39 40
# 42

# -----------------------------------------------------------------

# from math import *
# def f(s,m):
#     if s<=23:return m%2==0
#     if m==0:return 0
#     h = [f(s-3,m-1),f(s-5,m-1),f(ceil(s/2),m-1)]
#     return any(h) if m%2!=0 else all(h)
# print(max([s for s in range(24,400)if f(s,2)]))
# print([s for s in range(24,400)if not f(s,1) and f(s,3)])
# print(max([s for s in range(24,400)if not f(s,2) and f(s,4)]))

# 49
# 50 98
# 101