def gcf(x,y):
    while y!= 0:

        (x,y)=y, x%y
    x= int(input ("input a number"))
    y= int(input("input another number"))
    result=gcf(x,y)
    print(result)


