 # 3) sum of all no. from 1 to 100
sum=0
for el in range(1,101):
 sum+=el
print("sum=",sum)

 # 4) clculate freq of each words in string

str=input("write")


for el in str:
      print(el,str.count(el))

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

#Year is leap or not
year=int(input("type year"))
if(year%400==0)or(year%4==0)and(year%100!=0):
   print("leap year")
else:
   print("nonleap year")

#to find second largest no. in list
list=[3,5,8,6]
list.sort()
print(list[-2])