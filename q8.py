class Employee:
    def work(self):
        print("Employee Working")

class Developer(Employee):
    pass

class Tester(Employee):
    pass

d = Developer()
t = Tester()

d.work()
t.work()