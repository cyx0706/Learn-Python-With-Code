#没有删除重复部分
a=input()
i=len(a)
n=0
z=0
l1=[]

while n<i:
    b=ord(a[n])
    n=n+1
    if 64<b<97 :
        l1.append(a[n-1])
        z=z+1

if z==0:
    c="Not Found" 
    print(c)      

else :
    l2 = []
    for m in l1:
      if not m in l2:
        l2.append(m) 
    i=len(l2)
    n=0
    while n<i:
        print(l2[ n ],end='')
        n=n+1