print ("type 'break' to end the program")	
print ("type 'add' ; 'sub' ;'mult' ;and 'div'; and 'expo'")	
print ("type input here:")
user_input = input(": ")
if user_input == "add":
    x = float(input("enter the decided variable for x: "))
    y = float(input("enter the decided variable for y: "))
    sum = (x + y)
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

  
