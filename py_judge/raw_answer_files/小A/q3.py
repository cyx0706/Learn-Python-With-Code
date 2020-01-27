x = input()
y = []
num = 0
for i in x:
    if i.isupper():
        y.append(i)
        num = num + 1
        
y = set(y)

if num == 0:
    print("Not Found")

if num > 0:
    y = "".join(y)
    print(y)
    
        
