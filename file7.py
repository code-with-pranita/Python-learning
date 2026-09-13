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


