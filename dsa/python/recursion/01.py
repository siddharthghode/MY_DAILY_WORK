def print_to_n(n):
 if(n==1):
  print(1)
 else:
  print(n)
  n=n-1
  
  print_to_n(n)

n=5
print_to_n(n)
