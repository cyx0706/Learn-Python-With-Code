x = input()
x = x.split()
year = x[0]
year = int(year)
month = x[1]
month = int(month)
day = x[2]
day = int(day)
num = x[3]
num = int(num)
R = [0,31,29,31,30,31,30,31,31,30,31,30,31]
P = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#判断num和该月剩余天数的关系
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    if num <= R[month] - day:
        day = day +num
        num = 0
    else:
        num = num + day - R[month]
        month = month + 1
        if month ==13:
            year = year + 1
            month = 1
else:
    if num <= P[month] - day:
        day = day +num
        num = 0
    else:
        num = num + day - P[month]
        month = month + 1
        if month == 13:
            year = year + 1
            month = 1
#如果num大于该月剩余天数，判断num和该年剩余天数的关系
if num != 0:
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        while month <= 12:
            if num > R[month]:
                num = num - R[month]
                month = month + 1
            else:
                day = num
                num = 0
                break
    else:
        while month <= 12:
            if num > P[month]:
                num = num - P[month]
                month = month + 1
            else:
                day = num
                num = 0
                break
if num != 0:
    year = year + 1
#如果num大于该年剩余天数，就让num进行一个while循环，直到num=0,循环结束    
while num != 0:
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        for i in range(1,13):
            if num > R[i]:
                num = num - R[i]
            else:
                day = num
                num = 0
                month = i
                break
    else:
        for i in range(1,13):
            if num > P[i]:
                num = num - P[i]
            else:
                day = num
                num = 0
                month = i
                break
    if num != 0:
        year = year + 1
        

print(str(year) + " " + str(month) + " " + str(day))
            
            
            










