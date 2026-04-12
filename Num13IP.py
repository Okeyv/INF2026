# from ipaddress import *
# ip_net = ip_network("142.108.56.118/255.255.255.240", False)
# cnt = 0
# for ip_ad in ip_net:
#     if bin(int(ip_ad))[-16:].count("1") > bin(int(ip_ad))[:-16].count("1"):
#         cnt += 1
#         print(cnt)

# ------------------------------------------------------------------

# from ipaddress import *
# for A in range(0,256):
#     ip = ip_network(f"127.254.{A}.10/255.255.224.0",False)
#     for ip_ad in ip:
#         if (bin(int(ip_ad))[-16:].count("1") <= bin(int(ip_ad))[:-16].count("1")) == False:
#             break
#     else:
#         print(A)

# ------------------------------------------------------------------

# from ipaddress import *
# ip_add = ip_address("244.55.138.100")
# for mask in range(33):
#     try:
#         ip_net = ip_network(f"244.55.138.96/{mask}")
#         if ip_add in ip_net:
#             print(ip_net.netmask)
#     except:
#         continue

# ------------------------------------------------------------------

# from ipaddress import *
# ip_add = ip_address("244.55.138.100")
# for mask in range(33):
#     try:
#         ip_net = ip_network(f"240.0.0.0/{mask}")
#         if ip_add in ip_net:
#             print(ip_net.netmask)
#     except:
#         continue

# ------------------------------------------------------------------

# from ipaddress import *
# ip_add = ip_address("42.118.219.133")
# for mask in range(33):
#     try:
#         ipnet = ip_network(f"42.118.216.0/{mask}")
#         if ip_add in ipnet:
#             print(bin(int(ipnet.netmask)).count("1"))
#     except:
#         continue

# ------------------------------------------------------------------

# from ipaddress import * 
# ip1 = ip_network("123.206.97.128/255.255.255.224",False) 
# cnt = 0
# for ipadd in ip1: 
#     if bin(int(ipadd))[-3:] == "101" or bin(int(ipadd))[-3:] == "010": 
#         cnt +=1 
# print(cnt)

# ------------------------------------------------------------------

# for i in range(100,1000):
#     x = str(i)
#     a1 = int(x[0])**2 + int(x[1])**2
#     a2 = int(x[1])**2 + int(x[2])**2
#     maxa = max(a1,a2)
#     mina = min(a1,a2)
#     result = str(mina) + str(maxa)
#     if result == "9010":
#         print(i)
#         break

# ------------------------------------------------------------------
