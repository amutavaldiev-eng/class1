# with open("text.txt","w") as file:
#     file.write("Salom, jahon!")
#2
# with open("text.txt","r") as file:
#     s=file.read()
#     print(s)
#3
# with open("text.txt","r") as file:
#     for i in file:
#         print(i.strip())
#4
# with open("text.txt","r") as file:
#     a=file.readlines()
#     print(len(a))
#5
# with open("text.txt","a") as file:
#     file.write("orange")
#6
# with open("text.txt","w") as file:
#     file.writelines(["Ali\n", "Vali\n", "Guli\n"])
#7
# with open("text.txt","r") as file:
#     a = file.read().split()
#     print(len(a))
#8
# with open("text.txt","r") as file:
#     a=file.read().replace(" ", "").strip()
#     print(len(a))
#9
# with open("text.txt","r") as file:
#     c = 0
#     for i in file:
#         c += int(i.strip())
#     print(c)
#10
# with open("text.txt", "r") as file:
#     a = file.read().split()

# b = [int(i) for i in a]
# print(max(b))
#11
# with open("text.txt","r") as file:
#     a = file.read()
# with open("copy.txt","w") as f:
#     f.write(a)
#12
# with open("text.txt", "r") as file:
#     cnt = 1
#     for i in file:
#         print(f"{cnt}: {i.strip()}")
#         cnt+=1
#13
# with open("text.txt","r") as file:
#     a = file.read().split()
# cnt = 0
# for i in a:
#     if i == "python":
#         cnt += 1
# print(cnt)
#14
# with open("text.txt", "r") as file:
#     l = file.readlines()
# lon = max(l, key=len)
# print(lon.strip())
#
#15
# with open("text.txt", "r") as file:
#     l = file.read().upper()
# with open("copy.txt","w") as file1:
#     file1.write(l)
#16
# with open("text.txt", "r") as file:
#     line = file.readlines()

# all = [i for i in line if i.strip() !=""]
# with open("copy.txt", "w") as file:
#     file.writelines(all)
#17
# with open("text.txt", "r") as file:
#     l = file.readlines()
# with open("copy.txt", "r") as file1:
#     al=file1.readlines()
# with open("tex.txt", "w") as fil:
#     fil.writelines(l)
#     fil.writelines(al)
#18


#19
# with open("text.txt", "r") as file:
#     text = file.read()
# dic = {}
# for i in text.split():
#     dic[i] = dic.get(i, 0) + 1
# with open("copy.txt", "w") as file:
#     for i,t in dic.items():
#         file.write(f"{i}: {t}\n")
#20
