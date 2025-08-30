class Mobile:
    
    def __init__(self):
        print("mobile class default const called...")
        self.price= 1000
        self.x = 100

    def call(self):
        print("call method called from mobile")

class TAB:
    
    def __init__(self):
        print("tab class default const called...")        
        self.price=1200
        self.y=200

    
    def scroll(self):
        print("scroll method called..")

class Device(Mobile,TAB):
    
    def __init__(self):
        print("device class const called...")        
        super().__init__()#parent class const...
    def detail(self):
        print("price = ",self.price)         #
        print("x = ",self.x)#
        print("y = ",self.y)#


d =Device() #device class default  const...        
# d.call()
# d.scroll()
d.detail()