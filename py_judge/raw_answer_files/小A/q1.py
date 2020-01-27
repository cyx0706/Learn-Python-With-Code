n = input("Please enter a number:")
n = n.replace("0","零")
n = n.replace("1","壹")
n = n.replace("2","贰")
n = n.replace("3","叁")
n = n.replace("4","肆")
n = n.replace("5","伍")
n = n.replace("6","陆")
n = n.replace("7","柒")
n = n.replace("8","捌")
n = n.replace("9","玖")

if len(n)==9:
    n1 = n[0]+"亿"+n[1]+"仟"+n[2]+"佰"+n[3]+"拾"+n[4]+"万"+n[5]+"仟"+n[6]+"佰"+n[7]+"拾"+n[8]+"元"

if len(n)==8:
    n1 = n[0]+"仟"+n[1]+"佰"+n[2]+"拾"+n[3]+"万"+n[4]+"仟"+n[5]+"佰"+n[6]+"拾"+n[7]+"元"

if len(n)==7:
    n1 = n[0]+"佰"+n[1]+"拾"+n[2]+"万"+n[3]+"仟"+n[4]+"佰"+n[5]+"拾"+n[6]+"元"

if len(n)==6:
    n1 = n[0]+"拾"+n[1]+"万"+n[2]+"仟"+n[3]+"佰"+n[4]+"拾"+n[5]+"元"

if len(n)==5:
    n1 = n[0]+"万"+n[1]+"仟"+n[2]+"佰"+n[3]+"拾"+n[4]+"元"

if len(n)==4:
    n1 = n[0]+"仟"+n[1]+"佰"+n[2]+"拾"+n[3]+"元"

if len(n)==3:
    n1 = n[0]+"佰"+n[1]+"拾"+n[2]+"元"

if len(n)==2:
    n1 = n[0]+"拾"+n[1]+"元"

if len(n)==1:
    n1 = n[0]+"元"


n1 = n1.replace("零仟","零")
n1 = n1.replace("零佰","零")
n1 = n1.replace("零拾","零")
n1 = n1.replace("零零零","零")
n1 = n1.replace("零零","零")
n1 = n1.replace("仟零万","仟万")
n1 = n1.replace("佰零万","佰万")
n1 = n1.replace("拾零万","拾万")
n1 = n1.replace("零元","元")
n1 = n1.replace("零万","零")
n1 = n1.replace("零零","零")



print(n1)


