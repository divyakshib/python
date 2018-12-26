class person:
    def __init__(self,name,gender,number):
        self.name=name
        self.gender=gender
        self.number = number

    def __phonenumber(self):
        print(self.number)
    def introduction(self):
        print(self.gender)
        print(self.name)
        self.__phonenumber()
class student(person):
    def __init__(self,n,g,num,roll):
        person.__init__(self,n,g,num)
        self.roll_number=roll
    def display(self):
        self.introduction()
        print(self.roll_number)
m=person("Divyakshi","Female",98786554)
m.introduction()
s=student("Rose","Male",98392497,12)
s.display()
