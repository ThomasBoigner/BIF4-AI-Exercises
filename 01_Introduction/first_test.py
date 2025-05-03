# 1
a = list((39, 40, 45, 13, 7, 28, 22, 35, 24, 26, 62, 21, 31, 32))
b = list((3, 40, 28, 10, 46, 20, 31, 29))

print(len(set(a + b)))

# 2
dic1 = {1:10, 2:20}
dic2 = {1:20, 3:40}
dic3 = {2:50, 6:60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)