class TRAI:
    
    def call(self):
        print("call from TRAI CALLED>.")
        

class JIO(TRAI):
    
    def call1(self):
        print("jio calling...")

class Airtel(TRAI):
    
    def call2(self):
        print("airtel calling..")        

a = Airtel()
a.call()        