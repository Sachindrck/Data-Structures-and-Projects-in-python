#class computer
class Computer:

  #self callable method
  def __init__(self,cpu,ram):
    self.cpu=cpu
    self.ram=ram

  #method
  def config(self):
    print("config is :",self.cpu,self.ram)
  
#object
com1=Computer('i5',16)
com2=Computer('i7',8)


com1.config()
com2.config()
