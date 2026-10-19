
class AIStudent:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Course: ", self.course)


student = AIStudent("Ahmad", 22, "AI")

student.introduce()
print("----------")

