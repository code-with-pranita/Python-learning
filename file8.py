#....init...functions

class student:
    name="Pranita"

s1=student()
print(s1.name)

#parametirized constructors
class student:

 def __init__(self,name,marks):
    self.name=name
    self.marks=marks



s1=student("Pranita", 99)
# print(s1.name,s1.marks)