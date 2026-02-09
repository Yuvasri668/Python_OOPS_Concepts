class Student:
    college_name="ABC College"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    @classmethod
    def change_college(cls,new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        if marks>=35:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        print("name:",self.name)
        print("Roll no:",self.roll_no)
        print("College:", Student.college_name)

s1 = Student("Sri", 101)
s2 = Student("Yuva", 102)

s1.display()
s2.display()

Student.change_college("Mysuru Royal Institute of Technology")

s1.display()
s2.display()

print("Sri Result:", Student.is_pass(78))
print("Yuva Result:", Student.is_pass(80))

