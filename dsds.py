from simple_colors import *

class DATA:
    def __init__(self,n):
        self.n=n

    def authorization(self,password,code):
        self.username=input("Enter your name:")    
        password=input("Enter your password:")
        code=input("Enter your code:")
        if password=="" and code==0000:
            return 1
        else:
            return 0

    def input(self):
        self._name=[]
        self._age=[]
        self._mobno=[]
        self._email=[]
        self._address=[]
        for i in range(0,self.n):
            name=input("Enter the candidates name:")
            age=int(input("Enter the candidates age:"))
            address=input("Enter the address:")
            mob_no=input("Enter the mobile number:")
            email=input("Enter E-mail:")
            self._name.append(name)
            self._age.append(age)
            self._address.append(address)
            self._mobno.append(mob_no)
            self._email.append(email)

    def searching(self,name):
        for i in range(0,self.n):
            if self._name==name:
                return i

    def serachedPrinting(self,i):
        print(f'''Name - {self._name[i]} 
                 Age - {self._age[i]} 
                 Mobile number - {self._mobno[i]} 
                 Email - {self._email[i]} 
                 Address - {self._address[i]}''')            
    def filewriting(self):
        #user .json to dump data
        with open('data.txt','a') as f:
            f.writelines(self.username + ":")
            for i in range(0,self.n):
                f.writelines(self._name)
                f.writelines(self._age)
                f.writelines(self._address)
                f.writelines(self._mobno)
                f.writelines(self._email)


x='''Welcome to the server,this is my first project
             Points to be noted:
             -You need to have username,password,
             -pin(6 digits) to make new entries
         '''
print( black('*') * 320+ '\n' +red(f'{x.center(900)}','bold') + '\n'  +black('*') * 320)
choice=input('''Operations Available:-
-Become a member.(1)
-Adding DATA.(2)
-Editing DATA.(3)
-Accessing DATA.(4)
-Leave the PROGRAM.(5)
-EXIT! (6)
Enter your choice as numbers:''')
while(choice !=6 or choice.upper() !="EXIT"):
    if choice==1:
        name=input("Enter your name:")
        username=input("Enter your username:")
        password=input("Enter your password:")
        #write this things to file and .json 
    elif choice==2:
        numOfInput=int(input("Enter the number of participants data you will add:"))
        d= DATA()
        d.input()
        d.filewriting()

    elif choice==3:
        #open file and edit the data
        pass

    elif choice==4:
        __name=input("enter the account name you want to search:")
        d=DATA(10) 
        _i=d.searching(__name) 
        d.serachedPrinting(_i)

    elif choice==5:
        __name=input("enter the account name you want to deleted:")
        d=DATA(10) 
        _i=d.searching(__name) 
        d.serachedPrinting(_i)
        fc=input("confirm(yes\no):")
        if fc.upper()=="YES":
            del d._name
            del d._age
            del d._mobno
            del d._address
            del d._email
        print("ACCOUNT DELETED!!")
           