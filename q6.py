class Teacher:
    def teach(self):
        print("Teaching")

class Researcher:
    def research(self):
        print("Researching")

class Professor(Teacher, Researcher):
    pass

p = Professor()

p.teach()
p.research()