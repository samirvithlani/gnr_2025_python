class Mobile:
    
    def __init__(self):
        print("mobile class default const called...")

    def call(self):
        print("call method called from mobile")

class TAB:
    
    def __init__(self):
        print("tab class default const called...")        

    
    def scroll(self):
        print("scroll method called..")

class Device(Mobile,TAB):
    
    def __init__(self):
        print("device class const called...")        
        super().__init__()#parent class const...
        self.call()
        self.scroll()


d =Device() #device class default  const...        
# d.call()
# d.scroll()