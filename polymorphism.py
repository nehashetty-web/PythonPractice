class animal:
    def speak(self):
        print("animal makes sound")
class dog(animal):
    def speak(self):
        print("dog barks")
class cat(animal):
    def speak(self):
        print("cat meows")
c=cat()
d=dog()
a=animal()
a.speak()
d.speak()
c.speak()
#using loop
animals=[dog(),cat(),animal()]
for a in animals:
    a.speak()