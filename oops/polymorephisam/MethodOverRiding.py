class Bank:
    
    def withdraw(self):
        print("bank class withdraw method called...")



class SBI(Bank):
    
    def withdraw(self):
        print("SBI class withdraw method called...")   
        super().withdraw()     


s = SBI()
s.withdraw()        