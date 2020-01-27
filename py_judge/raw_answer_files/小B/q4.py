x = input()
alpha = []
num = []
all = []
for i in x:
    if i.isalpha():
        i = i.lower()
        alpha.append(i)
    if i.isdigit():
        num.append(i)
alpha.sort()
num.sort()
all = alpha + num
Y = "".join(all)
print(Y)
