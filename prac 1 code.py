import random


y0 = 50
x0 = 50
print("x0",x0)
print("y0",y0)
x1=50
y1=50
print("x1",x1)
print("y1",y1)

#change  x0 by a small amount
random_number= random.random()
print("random_number",random_number) 
if random_number < 0.5:
    x0=x0+1
    print("added 1 to x0")
else: 
    x0=x0-1
    print("subtracted 1 from x0") 

# move y0
random_number= random.random()
print("random_number",random_number) 
if random_number < 0.5:
    y0=y0+1
    print("added 1 to y0")
else: 
    y0=y0-1
    print("subtracted 1 from y0")
    
# move x1
random_number= random.random()
print("random_number",random_number) 
if random_number < 0.5:
    x1=x1+1
    print("added 1 to x1")
else: 
    x1=x1-1
    print("subtracted 1 from x1") 

# move y1
random_number= random.random()
print("random_number",random_number) 
if random_number < 0.5:
    y1=y1+1
    print("added 1 to y1")
else: 
    y1=y1-1
    print("subtracted 1 from y1")    
    
print(y0, x0)
print(y1, x1)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print("distance", answer)