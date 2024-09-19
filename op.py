class maths():
    def add(self):
        self.a=int(input("Enter first no:"))
        self.b=int(input("Enter second no:"))
        self.c=self.a+self.b
        print("Addition is :",self.c)
def sub(self):
        self.a=int(input("Enter first no:"))
        self.b=int(input("Enter second no:"))
        self.c=self.a-self.b
        print("substraction is :",self.c)

def mult(self):
        self.a=int(input("Enter first no:"))
        self.b=int(input("Enter second no:"))
        self.c=self.a*self.b
        print("Addition is :",self.c)

def div(self):
        self.a=int(input("Enter first no:"))
        self.b=int(input("Enter second no:"))
        self.c=self.a/self.b
        print("division is :",self.c)
        
        obj=maths()
        while True:
              print("\n 1.addition")
              print("2.substraction")
              print("3.Multiplication")
              print("4.division")
              print("5.exit")

              ch=int(input("Enter choice to perform, any operation"))
              if ch==1:
                    obj.add()
              elif ch==2:
                    obj.sub()
              elif ch==3:
                    obj.mult()
              elif ch==4:
                    obj.div()
              elif ch==5:
                    print("\n program stop")
                    break
              else:
                    print("Wrong  choice!!")