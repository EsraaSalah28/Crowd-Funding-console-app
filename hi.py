name = "ahmed"
def outerFn():
   name = "ali"
   def innerFn():
     print(name)
   innerFn()
outerFn()
print(name)