# ------------------------------------------------------------------

# 16 Задание ЕГЭ. Рекурсия.

# ------------------------------------------------------------------

# F = [0]*300000
# for n in range(1,300000):
#     if n <10:
#         F[n] = 3
#     elif n>=10:
#         F[n] = (n+4)*F[n-5]
# print((F[257487]//683+67*F[257477])//F[257472]) # Комп ЕГЭ-шный сгорит нах!

#   OR 

# a = (257487+4)*(257482+4)*(257477+4)
# b = 67*(257477+4)
# print(a//683+b)

# 24994270044009

# ------------------------------------------------------------------

# F = [0] * 1000  
# cnt = 0

# for n in range(1, 1000):  
#     if n <= 3:
#         F[n] = n
#     elif n > 3 and n % 2 == 0:
#         F[n] = F[n - 1] + 2 * F[n // 2]  
#     elif n > 3 and n % 2 != 0:
#         F[n] = F[n - 1] + F[n - 3]
        
#     if F[n] < 10**8:
#         cnt += 1
#     else:
#         break  



# print(cnt)


# from itertools import product
# chet = "1357"
# cnt = 0
# for p in product("012345678", repeat=5):
#     s = "".join(p)
#     if s[0] == '0':
#         continue        
#     if s.count('0') == 1:
#         pos = s.index('0') 
#         left = (pos == 0) or (s[pos-1] not in chet)
#         right = (pos == 4) or (s[pos+1] not in chet)
        
#         if left and right:
#             сnt += 1

# print(cnt)
