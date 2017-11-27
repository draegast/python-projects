print ("type 'break' to end the program")	
print ("type 'add' ; 'sub' ;'mult' ;and 'div'; and 'expo'")	
print ("type input here:")
user_input = input(": ")
if user_input == "add":
    y = float(input("enter the decided variable for y: "))
    x = float(input("enter the decided variable for x: "))
    sum = (x + y)
    print(sum)
elif user_input == "sub":
    y = float(input("enter the decided variable for y: "))
    x = float(input("enter the decided variable for x: "))
    sum = (x-y)
    print(sum)
elif user_input == 'mult':
    y = float(input("enter the decided variable for y: "))
    x = float(input("enter the decided variable for x: "))
    sum = (x*y)
    print(sum)
elif user_input == 'div':
    y = float(input("enter the decided variable for y: "))
    x = float(input("enter the decided variable for x: "))
    sum = (x//y)
    print(sum)
elif user_input == "expo":
    y = float(input("enter the decided variable for y: "))
    x = float(input("enter the decided variable for x: "))
    sum = x**y
    print(sum)

  
