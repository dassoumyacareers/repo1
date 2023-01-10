def check_method(*args):
  """
  this is method which accepts arguments 
  """
  iter_for_n_times = args[3]     # args[3] mapping the index position 3 in the print statement ie. iteration_range
  x = args[4]                    # args[4] mapping the index position 4 in the print statement ie. check_var
  
  for num in range(iter_for_n_times):
    print(num)

    if num == x:
      print("match")
  return 10.0

iteration_range = int(input("range: "))
check_var = int(input("x: "))
print(type(check_method("hello0", 324, 45, iteration_range, check_var)))
# print("hello")

# iter_count_range = 10
# check_method(10, 7)

# check_method(iteration_range=6, check_var=4)
