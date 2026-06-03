class Father:
    def bike(self):
        print("Father's Bike")

class Mother:
    def jewellery(self):
        print("Mother's Jewellery")

class Child(Father, Mother):
    pass

c = Child()

c.bike()
c.jewellery()