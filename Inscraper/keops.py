def welcomekeops():
    print("|",end="")
    print(32*" ",end="")
    print("*",end="")
    print(32*" ",end="")
    print("|")
    print("|",end="")
    print(31*" ",end="")
    print("*",end="")
    print(" ",end="")
    print("*",end="")
    print(31*" ",end="")
    print("|")
    a=1
    b=30
    while a<5:
        print("|",end="")
        print(b*" ",end="")
        print("*",end="")
        print(((a*2)+1)*" ",end="")
        print("*",end="")
        print(b*" ",end="")
        print("|")
        a+=1
        b-=1
        if a==5:
            print("|",end="")
            print(b*" ",end="")
            print("* * * * * * *",end="")
            print(b*" ",end="")
            print("|")
    print("|", end="")
    print(" "*30,end="")
    print("Keops",end="")
    print(" "*30,end="")
    print("|")
