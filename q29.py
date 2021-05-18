class myClass:
  def __init__(self,name,age):
    self.age=age
    self.name=name
  def myFunc(self):
   print(self.name,self.age)
    
p1=myClass("jay",36)
p1.myFunc()