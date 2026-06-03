class Vehicle:

    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):

    def drive(self):
        print("Car is being driven")

car1 = Car()

car1.start()
car1.drive()
car1.stop()