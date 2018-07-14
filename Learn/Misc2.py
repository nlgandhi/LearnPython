

def TestLambda():
    sqr = lambda i:i*i
    for i in range(1,10):        
       print(sqr(i)) 

def multiply2(x):
  return (x * 2)

def TestMap():    
    map_outputs = map(lambda x: x*2, [1, 2, 3, 4])
    

TestMap()
#TestLambda()

