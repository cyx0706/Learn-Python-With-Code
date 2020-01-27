a=input()
change1=input()
change2=input()
change3=input()
change4=input()
t=(change1,change2,change3,change4)
x=int(a[1])
y=int(a[3])
#测试输出未删去

for changes in t:
    if "UP"in changes:
        d1=int(changes[3:])
        x=x-d1
    if "DOWN"in changes:
        d2=int(changes[5:])
        x=x+d2
    if "LEFT"in changes:
        d3=int(changes[5:])
        y=y-d3
    if "RIGHT"in changes:
        d4=int(changes[6:])
        y=y+d4
      
print('({},{})'.format(x,y))






