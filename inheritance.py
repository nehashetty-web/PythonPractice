'''Create:
Parent class: Vehicle → method start()
Child class: Car → method drive()
Call both methods using object of Car'''
class vehicle:
    def start(self):
        print("vehicle starts")
class car(vehicle):
    def drive(self):
        print("drives car")
c=car()
c.start()

c.drive()
class person:
    def work(self):
        print("person works")
class engineer(person):
    def work(self):
        print("engineer codes")
e=engineer()
e.work()

#If you want to call parent method also, use:
class engineer(person):
    def work(self):
        super().work()
        print("engineer codes")

        