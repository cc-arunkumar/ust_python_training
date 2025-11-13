class Test:
    def add(self,a=0,b=0,c=0):
        print("sum2=",a+b+c)
    def add(self,a=0,b=0):
        print("sum1=",a+b)

t=Test()
t.add(6,8)
# when we declare with a same name the leatest method is called......
# so we gte an error here..
t.add(1,2,3)

    