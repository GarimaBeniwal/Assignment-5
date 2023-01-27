lower_value=int(input("enter the lower limit"))
upper_value=int(input("enter the upper limit"))
for no in range(lower_value,upper_value+1):
    if no>1:
        for i in range(2,no):
            if(no%i==0):
                break
        else:
            print(no)    