a=int(input("Choose the operation the operation \n Press 1 for area \n press 2 for perimeter "))

if(a==1):
    l=int(input("Length of rectangle "))
    b=int(input("width of rectangle "))

    print("the area of rectangle is ",l*b)
    
elif (a==2):
    l=int(input("Length of rectangle "))
    b=int(input("width of rectangle "))

    print("the perimeter of rectangle is " , 2*( l+b ))
else:
    print("invalid request")