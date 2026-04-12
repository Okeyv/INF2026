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
# for mask in range(33):
#     ip1 = ip_network(f"10.227.3.113/{mask}",False)
#     ip2 = ip_network(f"10.235.127.7/{mask}",False)
#     if ip1 != ip2:
#         print(mask)

# ------------------------------------------------------------------

# from ipaddress import *
# cnt = 0
# for mask in range(33):
#     ip_net = ip_network(f"158.116.11.146/{mask}", False)
#     if str(ip_net.network_address) == "158.116.0.0":
#         cnt += 1
# print(cnt)

# ------------------------------------------------------------------

# from ipaddress import *
# cnt = 0
# ip1 = ip_network("171.128.0.0/255.128.0.0", False)
# for ip_add in ip1:
#     if bin(int(ip_add))[:-16].count("1") < bin(int(ip_add))[-16:].count("1"):
#         cnt += 1
# print(cnt)

# ------------------------------------------------------------------

# from ipaddress import *
# for mask in range(33):
#         ip1 = ip_network(f"174.213.57.95/{mask}",False) 
#         if ip1 == "174.213.0.0":
#             print(mask)

# ------------------------------------------------------------------

# from ipaddress import *
# for mask in range(33):
#     ip1 = ip_network(f"111.81.93.127/{mask}",False)
#     if str(ip1.network_address) == "111.81.80.0":
#         print(bin(mask)[2:])

# ------------------------------------------------------------------

# from ipaddress import *
# ip1 = ip_network("235.86.56.0/255.255.248.0",False)
# cnt = 0
# for ipadd in ip1:
#     if bin(int(ipadd))[-2:] == "11":
#         cnt += 1
# print(cnt)

# ------------------------------------------------------------------

# from ipaddress import *
# ip1 = ip_network("172.16.160.0/255.255.240.0",False)
# cnt = 0 
# for ipadd in ip1:
#     if bin(int(ipadd))[2:].count("1") % 3 !=0:
#         cnt += 1
# print(cnt)

# ------------------------------------------------------------------

# from ipaddress import *
# cnt = 0
# for mask in range(33):
#     ip1 = ip_network(f"76.155.48.2/{mask}",False)
#     if str(ip1.network_address) == "76.155.48.0":
#         cnt += 1
# print(cnt)

# ------------------------------------------------------------------

# from ipaddress import *
# ip1 = ip_network("191.128.66.83/255.192.0.0",False)
# cnt = 0
# for ipadd in ip1:
#     cnt += 1
# print(ipadd)
# Из результата вычесть 1, получиться 191.191.255.254
# Ответ 191191255254

# ------------------------------------------------------------------

# from ipaddress import *
# for A in range(1,256):
#     ip1 = ip_network(f"183.192.{A}.0/255.255.252.0",False)
#     ok = True
#     for ip in ip1:
#         if bin(int(ip))[2:].zfill(32)[-16:].count("1") <= 3:
#             ok = False
#             break
#     if ok:
#         print(A)
#         break

# ------------------------------------------------------------------

# from ipaddress import *
# ip1 = ip_network("172.16.168.0/255.255.248.0",False)
# cnt = 0
# for ipadd in ip1:
#     if bin(int(ipadd))[2:].count("1") % 5 != 0:
#         cnt += 1
# print(cnt)

# ------------------------------------------------------------------

# from ipaddress import *
# ip1 = ip_network("192.168.63.0/255.255.255.128",False)
# cnt = 0
# for ipadd in ip1:
#     if bin(int(ipadd))[2:].count("0") % 5 != 0:
#         cnt += 1
# print(cnt)

# ------------------------------------------------------------------

# from ipaddress import *
# ip1 = ip_network("122.159.136.144/255.255.255.248",False)
# cnt = 0
# for ipadd in ip1:
#     if bin(int(ipadd))[2:].count("1") % 4 != 0:
#         cnt += 1
# print(cnt)

# ------------------------------------------------------------------

# from ipaddress import *
# ip1 = ip_network("102.162.200.51/255.255.255.0",False)
# for ipadd in ip1:
    # print(ipadd)
# print(102+162+200+254)

# print(bin(138)[2:])
# print(bin(136)[2:])
# print(int("11111000",2))

# ------------------------------------------------------------------

# from ipaddress import *
# ip1 = ip_network("172.16.8.0/255.255.252.0")
# cnt= 0
# for ipadd in ip1:
#     cnt +=1
# print(cnt)

# ------------------------------------------------------------------

