print("choose options from the menu below : ")
while True:
    user_input=int(input("enter options : "))
    if user_input==1:
        print("learn python")
    elif user_input==2:
        print("learn java")
    elif user_input==3:
        print("learn swimming ")
    elif user_input==4:
        print("have dinner ")
    elif user_input==5:
        print("go to bed ") 
    elif user_input==0:
        break
    else:
        print("invalid option")
        
