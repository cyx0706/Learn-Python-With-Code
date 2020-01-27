number=input()
dict1={'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖',}
i=len(number)
#亿 仟 佰 拾  万  仟 佰 拾  元


if i==1:
    print(dict1[number]+"元")

if i==2:
    if number[-1]=='0':
        print(dict1[ number[-2] ]+'拾元')
    else:
        print(dict1[ number[-2] ]+"拾"+dict1[ number[-1] ]+"元")

if i==3:
    if number[-1]=='0':
        if number[-2]=="0":
            print(dict1[ number[-3] ]+"佰元")
        else :
            print(dict1[ number[-3] ]+"佰"+dict1[ number[-2] ]+"拾元")
    else :
        if number[-2]=="0":
            print(dict1[ number[-3] ]+"佰零"+dict1[ number[-1] ]+"元")
        else :
            print(dict1[ number[-3] ]+"佰"+dict1[ number[-2] ]+"拾"+dict1[ number[-1] ]+"元")

if i==4:
    if number[-1]=='0':
    
        if number[-2]=="0":
        
            if number[-3]=="0":
                print(dict1[ number[-4] ]+"仟元")
            else :
                print(dict1[ number[-4] ]+"仟"+dict1[ number[-3] ]+"佰元")
            
        else :
            
            if number[-3]=="0":
                print(dict1[ number[-4] ]+"仟零"+dict1[ number[-2] ]+"拾元")
            else :
                print(dict1[ number[-4] ]+"仟"+dict1[ number[-3] ]+"佰"+dict1[ number[-2] ]+"拾元")
    
    else :
        if number[-2]=="0":
               
            if number[-3]=="0":
                print(dict1[ number[-4] ]+"仟零"+dict1[ number[-1] ]+'元')
            else :
                print(dict1[ number[-4] ]+"仟零"+dict1[ number[-3] ]+"佰"+dict1[ number[-1] ]+'元')
            
        else :
            
            if number[-3]=="0":
                print(dict1[ number[-4] ]+"仟零"+dict1[ number[-2] ]+"拾"+dict1[ number[-1] ]+'元')
            else :
                print(dict1[ number[-4] ]+"仟"+dict1[ number[-3] ]+"佰"+dict1[ number[-2] ]+"拾"+dict1[ number[-1] ]+'元')        

b=i
x=0
   
if 4<i<=9:
    number1=[]
    number2=number[-4]+number[-3]+number[-2]+number[-1]
    if i==9:
        a=dict1[number[0]]+'亿'
        number=number[-8]+number[-7]+number[-6]+number[-5]+number[-4]+number[-3]+number[-2]+number[-1]
        i=i-1
    n=-i

    while i>4:
        number1.append( number[n] )
        x=x+1
        n=n+1
        i=i-1
        
    number1=''.join(number1)
 
    if x==1:#i=1
        num=(dict1[number1]+"万")#
    
    if x==2:#i=2
        if number1[-1]=='0':
            num=(dict1[ number1[-2] ]+'拾万')
        else:
            num=(dict1[ number1[-2] ]+"拾"+dict1[ number1[-1] ]+"万")
    
    if x==3:#i=3
        if number1[-1]=='0':
            if number1[-2]=="0":
                num=(dict1[ number1[-3] ]+"佰万")
            else :
                num=(dict1[ number1[-3] ]+"佰"+dict1[ number1[-2] ]+"拾万")
        else :
            if number1[-2]=="0":
                num=(dict1[ number1[-3] ]+"佰零"+dict1[ number1[-1] ]+"万")
            else :
                num=(dict1[ number1[-3] ]+"佰"+dict1[ number1[-2] ]+"拾"+dict1[ number1[-1] ]+"万")
    
    if x==4:#i=4
        if number1[-1]=='0':
        
            if number1[-2]=="0":
            
                if number1[-3]=="0":
                    num=(dict1[ number1[-4] ]+"仟万")
                    
                else :
                    num=(dict1[ number1[-4] ]+"仟"+dict1[ number1[-3] ]+"佰万")
                
            else :
                
                if number1[-3]=="0":
                    num=(dict1[ number1[-4] ]+"仟零"+dict1[ number1[-2] ]+"拾万")
                else :
                    num=(dict1[ number1[-4] ]+"仟"+dict1[ number1[-3] ]+"佰"+dict1[ number1[-2] ]+"拾万")
        
        else :
            if number1[-2]=="0":
                   
                if number1[-3]=="0":
                    num=(dict1[ number1[-4] ]+"仟零"+dict1[ number1[-1] ]+'万')
                else :
                    num=(dict1[ number1[-4] ]+"仟零"+dict1[ number1[-3] ]+"佰"+dict1[ number1[-1] ]+'万')
                
            else :
                
                if number1[-3]=="0":
                    num=(dict1[ number1[-4] ]+"仟零"+dict1[ number1[-2] ]+"拾"+dict1[ number1[-1] ]+'万')
                else :
                    num=(dict1[ number1[-4] ]+"仟"+dict1[ number1[-3] ]+"佰"+dict1[ number1[-2] ]+"拾"+dict1[ number1[-1] ]+'万')        

    if number2[-1]=='0':#因此时首位可能为0，故有不同
        
            if number2[-2]=="0":
            
                if number2[-3]=="0":
                
                    if number2[-4]=='0':
                        ber='元'
                    else :
                        ber=(dict1[ number2[-4] ]+"仟元")
                        
                else :
                
                    if number2[-4]=='0':
                        ber=('零'+dict1[ number2[-3] ]+"佰元")
                    else :
                        ber=(dict1[ number2[-4] ]+"仟"+dict1[ number2[-3] ]+"佰元")
            else :
                
                if number2[-3]=="0":
                    if number2[-4]=='0':
                        ber=("零"+dict1[ number2[-2] ]+"拾元")
                    else:
                        ber=(dict1[ number2[-4] ]+"仟零"+dict1[ number2[-2] ]+"拾元")
                else :
                    if number2[-4]=='0':
                        ber=(dict1[ number2[-4] ]+dict1[ number2[-3] ]+"佰"+dict1[ number2[-2] ]+"拾元")
                    else:
                        ber=(dict1[ number2[-4] ]+"仟"+dict1[ number2[-3] ]+"佰"+dict1[ number2[-2] ]+"拾元")
        
    else :
            if number2[-2]=="0":
                
                if number2[-3]=="0":
                    if number2[-4]=='0':#
                        ber=('零'+dict1[ number2[-1] ]+'元')
                    else:
                        ber=(dict1[ number2[-4] ]+"仟零"+dict1[ number2[-1] ]+'元')
                        
                else :
                    if number2[-4]=='0':
                        ber=("零"+dict1[ number2[-3] ]+"佰"+dict1[ number2[-1] ]+'元')
                    else:
                        ber=(dict1[ number2[-4] ]+"仟零"+dict1[ number2[-3] ]+"佰"+dict1[ number2[-1] ]+'元')
                
            else :
                
                if number2[-3]=="0":
                    if number2[-4]=='0':
                        ber=("零"+dict1[ number2[-2] ]+"拾"+dict1[ number2[-1] ]+'元')
                    else:
                        ber=(dict1[ number2[-4] ]+"仟零"+dict1[ number2[-2] ]+"拾"+dict1[ number2[-1] ]+'元')
                else :
                    if number2[-4]=='0':
                        ber=(dict1[ number2[-4] ]+dict1[ number2[-3] ]+"佰"+dict1[ number2[-2] ]+"拾"+dict1[ number2[-1] ]+'元')
                    else:
                        ber=(dict1[ number2[-4] ]+"仟"+dict1[ number2[-3] ]+"佰"+dict1[ number2[-2] ]+"拾"+dict1[ number2[-1] ]+'元')  


    if b!=9 :
        print(num+ber)
    if b==9:
        print(a+num+ber)



