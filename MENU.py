def add():
    a=int(input("Enter a Number "))
    b=int(input("Enter a Number "))
    c=a+b
    print("a= ",a)
    print("b= ",b)
    print("c= ",c)
    print("======================")
    

def subs():
    a=int(input("Enter a Number "))
    b=int(input("Enter a Number "))
    c=a-b
    print("a= ",a)
    print("b= ",b)
    print("c= ",c)
    print("======================")


def divi():
    a=int(input("Enter a Number "))
    b=int(input("Enter a Number "))
    c=a/b
    print("a= ",a)
    print("b= ",b)
    print("c= ",c)
    print("======================")


def mul():
    a=int(input("Enter a Number "))
    b=int(input("Enter a Number "))
    c=a*b
    print("a= ",a)
    print("b= ",b)
    print("c= ",c)
    print("======================")

#================================================================                 

def submenu1():
    while True:
          print("\n\n\ncalculator ")
          print("======================")
          print(" 1 addition ")
          print(" 2 substraction ")
          print(" 3 division")
          print(" 4  multiplication  ")
          print("0- Back  ")
          print("======================")
          ch=int(input("Enter u r choice "))
          if ch==1:
                    add()
          if ch==2:
                    subs()
          if ch==3:
                    divi()
          if ch==4:
                    mul()
          if ch==0:
                    return
#================================================================                 

def submenu2():
    while True:
          print("\n\n\naLL sERIES r ")
          print("======================")
          print(" 1.1 2 3 4 5 6 .... N ")
          print(" 2- N. ..... 1")
          print(" 3  SERIES OF ODD ")
          print(" 4  series of even no  ")
          print("0- Back  ")
          print("======================")
          ch=int(input("Enter u r choice "))
          if ch==1:
                    add()
          if ch==2:
                    subs()
          if ch==3:
                    divi()
          if ch==4:
                    mul()
          if ch==0:
                    return

#================================================================                 
def submenu3():
    while True:
          print("\n\n\naLL area  ")
          print("======================")
          print(" 1.area of rect")
          print(" 2- trianglr")
          print(" 3  circle ")
          print(" 4  square  ")
          print("0- Back  ")
          print("======================")
          ch=int(input("Enter u r choice "))
          if ch==1:
                    add()
          if ch==2:
                    subs()
          if ch==3:
                    divi()
          if ch==4:
                    mul()
          if ch==0:
                    return

#================================================================                 
def mainmenu():
          print("======================")
          print("M A I  N    M E N U ")
          print("======================")
          print("1. calculator ")
          print("2. series question ")
          print("3. Area of ... ")
          print("4. general concept  ")
          print("0  Quit  ")
          print("======================")

          ch=int(input("Enter u r choice "))
          if ch==1:
                    submenu1()
          if ch==2:
                    add()
          if ch==3:
                      submenu1()()
          if ch==4:
                      submenu1()()
          if ch==0:
                    exit()
                    
          input()


while True:
        mainmenu()






















          
      





