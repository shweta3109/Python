class myClass:
  def __init__(self,marks,percentage):
    self.marks=marks
    self.percentage=percentage
  def myFunc(self):
   print(self.marks,self.percentage)
    
p1=myClass(45,90)
p1.myFunc()
class performance(myClass):
    pass
w=performance(23,89)
w.myFunc()