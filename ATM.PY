ch=input("please enter your card\n 1)yes 2) no\n")
if ch=='1':
    a=input('please select language\n 1) english\n 2) hindi\n')
    if a=='1'or a=='2':
        b=int(input('enter any number between 10 and 99:-')) 
        if b>=10 and b<=99:
            c=int(input('please enter your pin:-'))
            if len(str(c))==4:
                d=8000
                e=input("please choose \n 1)cash widhdrawel\n 2) balance inquary\n 3) deposite \n")
                if e=='1':
                    f=input("1) current\n 2)saving\n")
                    if f=='2'or f=='1':
                        g=int(input('enter amount:-'))
                        print('your transaction is being proceed')
                        print('available balance is',d-g)
                    else:
                        print('enter 1 and 2 only')
                elif e=='3':
                    t=int(input('enter amount to deposite\n'))
                    print('the main balance is',d+t) 
                else:
                    print(d) 
            else:
                print('please enter 4 digit no')   
        else:
            print('enter two digit no only')
    else:
        print("enter 1 or 2 only")
else:
    print('please insert your card')     