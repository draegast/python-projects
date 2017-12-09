print ("type 'break' to end the program")	
print ("type 'add' ; 'sub' ;'mult' ;and 'div'; and 'expo'")	
print ("type input here:")
user_input = input(": ")

def doub(x):
    return x*2

def add(x,y)
    return x +y
if user_input == "add":
    x = float(input("enter the decided variable for x: "))
    y = float(input("enter the decided variable for y: "))
    sum = add(x,y)
    print(sum)

 elif user_input == "sub":
    x = float(input("enter the decided variable for x: "))
    y = float(input("enter the decided variable for y: "))
    sum = (x-y)
    print(sum)
    
elif user_input == 'mult':
    x = float(input("enter the decided variable for x: "))
    y = float(input("enter the decided variable for y: "))
    sum = (x*y)
    print(sum)
    
elif user_input == 'div':
    x = float(input("enter the decided variable for x: "))
    y = float(input("enter the decided variable for y: "))
    sum = (x//y)
    print(sum)
    
elif user_input == "expo":
    x = float(input("enter the decided variable for x: "))
    y = float(input("enter the decided variable for y: "))
    sum = x**y
    print(sum)
    
elif user_input == "THE ANSWER":
    print(42)
    
elif user_input == "double":
    x = float(input("enter the decided variable for x: "))
    doubled = doub(x)
    print(doubled)
    
  
