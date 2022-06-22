print ("Hello world")

if 2 > 5:
    print ("2 is bigger than 5")
else:
# 2 less than or equal to 5
    print ("2 is not bigger than 5")

"""
this is a multiline comment

"""
x = 5
y = "Hello world"
print (x)
print (y)
x = "none of your business"
print (x)

x=str(3)
print(type(x))
x=int(3)
print(type(x))
x=float(3)
print(type(x))

x="John"
y='John'
if x == y:
    print ("x is equal to y")
else:
    print ("x and y are not equal")

x = "John"
X = "Yoko"
if x == X:
    print ("x and X are equal")
else:
    print ("x and X are not equal")

x,y,z="Nick","Stijn","Jan"
print(x)
print(y)
print(z)

x=y=z="Danny"
print(x)
print(y)
print(z)

collegas=["Nick","Stijn","Jan"]
x,y,z=collegas
print(x)
print(y)
print(z)
x="ik"
y="ben"
z="geweldig"
print(x,y,z)
print(x+y+z)
x=5
y=10
print(x+y)
x=5
y="koen"
print(x,y)

x="global"
def myfunction():
    print("here x is " + x)
myfunction()
x="global"
def myfunction():
    x="local"
    print("here x is " +x)
myfunction()
print ("here x is " + x)

def myfunction():
    global x
    x="fantastic"
myfunction()
print("python is " + x)
x="global"
def myfunction():
    global x 
    x="super"
myfunction()
print ("x is " +x)