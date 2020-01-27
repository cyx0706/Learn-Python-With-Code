#这道题也可以用split()创建列表【更好一点】，我直接用字符串处理的
m = input()
m1 = input()
m2 = input()
m3 = input()
m4 = input()
x = int(m[1])
y = int(m[3])

if 'UP' in m1:
    y = y - int(m1[3])
if 'DOWN' in m1:
    y = y + int(m1[5])
if 'RIGHT' in m1:
    x = x + int(m1[6])
if 'LEFT' in m1:
    x = x -int(m1[5])

if 'UP' in m2:
    y = y - int(m2[3])
if 'DOWN' in m2:
    y = y + int(m2[5])
if 'RIGHT' in m2:
    x = x + int(m2[6])
if 'LEFT' in m2:
    x = x -int(m2[5])

if 'UP' in m3:
    y = y - int(m3[3])
if 'DOWN' in m3:
    y = y + int(m3[5])
if 'RIGHT' in m3:
    x = x + int(m3[6])
if 'LEFT' in m3:
    x = x -int(m3[5])

if 'UP' in m4:
    y = y - int(m4[3])
if 'DOWN' in m4:
    y = y + int(m4[5])
if 'RIGHT' in m4:
    x = x + int(m4[6])
if 'LEFT' in m4:
    x = x -int(m4[5])

print("(" + str(x) + "," + str(y) + ")")
