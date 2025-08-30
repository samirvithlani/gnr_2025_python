class Shape:
    
    def area(self):
        print("area function called with no param")
    
    def area(self,r):
        print("area function called with r param..",r)    
    
    def area(self,h,w):
        print("area function called with heigh and width..")    
        


s = Shape()
#s.area() 
#s.area(100)       
#s.area(10,20)