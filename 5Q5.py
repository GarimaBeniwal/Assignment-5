rows=int(input("enter the no of rows"))
a=ord("A")

for i in range(rows):
    for j in range(i+1):
        if(a>ord("Z")):
            a=ord("A")
        print(chr(a),end=" ")
        a=a+1
    print()    


     

    