first_divisor = 24
second_divisor = 36
counting = True
i = 1 
while counting : 
  if i % first_divisor ==0 and i % secon_divisor == 0 :
    print("The LCM of ",first_divisor, 'and' ,second_divisor,'is',i,'.')
    break
  i += 1 
