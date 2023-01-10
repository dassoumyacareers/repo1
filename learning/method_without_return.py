def drive():
  while True:
    user_input=input("enter drive instruction :  ")
    if user_input=="a":
      print("the car is speeding")
      drive()
    elif user_input=="b":
      print("the car is put to rest")
    elif user_input=="c":
      print("the car is experiencing traffic")
    else:
      print("there is no matching input")
      break


def specification():
  print("car details")
  brand=input("enter the brand name : ")
  model=input("enter the model name : ")
  colour=input("enter the car colour : ")
  print("the brand is {0} has model {1} in colour {2}".format(brand,model,colour))



print(specification())

print("lets test drive")

drive()
