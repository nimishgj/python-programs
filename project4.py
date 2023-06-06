ch=int(input("1.addition  2.subtraction   3.multiply   4.division  \n Enter your choice:"))

if ch>4:
    print("Invalid choice..!")
else:
    a,b=map(int,input("Enter two numbers:").split(" "))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        div()
    
def add(a,b):
    print(f"Addition result:{a+b}")
    
def sub(a,b):
    print(f"subtraction result:{a-b}")  
    
def mul(a,b):
    print(f"multiplication result:{a*b}")      
    
def div(a,b):
    print(f"divison result:{a/b}")          
    
    
    
    