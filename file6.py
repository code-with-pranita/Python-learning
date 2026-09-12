#function

def calc_avg(a,b,c):
  avg=(a+b+c)/3
  print(avg)
  return avg


  
calc_avg(3,4,5)

def calc_pro(a=1,b=8):
  pro=(a*b)
  print(pro)
  return pro
calc_pro()



str="Pranav"

def calc_len(str):
  print(len(str))
  return len

calc_len(str)


num=[1,3,5]

def cal_list(num):
  print(list(num))
  return list

cal_list(num)
  
#To calculate factorial
def calc_fact(n):
  fact=1
  for i in range(1,n+1):
    fact*=i
  print(fact)
  return fact
    
calc_fact(4)

# convert to usd
usd_val=int(input("Enter a USD no:"))
def converter(usd_val):
  inr_val=usd_val*92
  print(usd_val,"USD=",inr_val,"INR")

  converter(usd_val)
  # RECURSION
# It is nothing but a loop. we mainly use loop instead of it.
def show(n):
  if(n == 0):
      return
  print(n)
  show(n-1)
  
show(3)