# 5) G A M E

import random
secret= random.randint(1,10) # Both 1 ,10 are included or you may use random.randrange(1,11)
guess=int(input("write a no."))
if(secret==guess):
   print("you won")
else:
   print("you lose")

# 6) reverse a string
str= "victory and"
print(str[::-1])

# To remove duplicate from lists
info=[2,3,6,2,4]
print(set(info))

#to arrange in ascending

info.sort()
print(info)


