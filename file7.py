f=open("file1.txt","r")
data=f.read()
print(data)
f.close()

#  "r" means read

f=open("file1.txt","r")

line1= f.readline()
line2= f.readline()
print(line1)
print(line2)
f.close()

# for writing
f=open("file1.txt", "w")
f.write("COEP FOR SURE")

f.close()


f=open("file1.txt", "a")
f.write("I am a coder")

f.close()
f=open("file1.txt","r")
data=f.read()
print(data)
f.close()

#  "r" means read

f=open("file1.txt","r")

line1= f.readline()
line2= f.readline()
print(line1)
print(line2)
f.close()

# for writing
f=open("file1.txt", "w")
f.write("COEP FOR SURE")

f.close()


f=open("file1.txt", "a")
f.write("I am a coder")

f.close()

#for overwriting
f=open("file2.txt","r+")
f.write("abc")# initial statement is "This is my cat"
print(f.read())
f.close()


f=open("file1.txt", "w+") #"w+" will remove all from file1 and only write "COEP FOR SURE"
f.write("COEP FOR SURE")

f.close()



f=open("file3.txt","r")
data=f.read()
newdata=data.replace("cool","preety") # "I am so cool" was initial statement.

print(newdata)



f=open("file3.txt","w")
f.write(newdata)

f.close()


f=open("file4.txt","w")
f.write("why so hot?")





