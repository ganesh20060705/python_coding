class Vehicle:
    def show_brand(self):
        print("Brand: Toyota")

class Car(Vehicle):
    def show_model(self):
        print("Model: Fortuner")

c = Car()

c.show_brand()
c.show_model()