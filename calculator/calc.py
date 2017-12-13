while True:
 print ("type 'break' to end the program")	
 print ("type 'add' ; 'sub' ;'mult' ;and 'div';  'expo'; 'Double'; and 'break' to access different functions")	
 print ("type input here:")
 user_input = input(": ")

 def doub(x):
     return x * 2

 def add(x,y):
     return x +y

 def sub(x,y):
     return x-y

 def mult (x,y):
     return x*y

 def div (x,y):
     return x//y

 def expo (x,y):
     return x**y

 if user_input == "break":
     break
 elif user_input == "add":
     x = float(input("enter the decided variable for x: "))
     y = float(input("enter the decided variable for y: "))
     sum = add(x,y)
     print(sum)

 elif user_input == "sub":
     x = float(input("enter the decided variable for x: "))
     y = float(input("enter the decided variable for y: "))
     sum = sub(x,y)
     print(sum)
    
 elif user_input == 'mult':
     x = float(input("enter the decided variable for x: "))
     y = float(input("enter the decided variable for y: "))
     sum = mult(x,y)
     print(sum)
    
 elif user_input == 'div':
     x = float(input("enter the decided variable for x: "))
     y = float(input("enter the decided variable for y: "))
     sum = div(x,y)
     print(sum)
    
 elif user_input == "expo":
     x = float(input("enter the decided variable for x: "))
     y = float(input("enter the decided variable for y: "))
     sum = expo(x,y)
     print(sum)
    
 elif user_input == "double":
     x = float(input("enter the decided variable for x: "))
     doubled = doub(x)
     print(doubled)

 elif user_input == "THE ANSWER":
     print(42)
    
