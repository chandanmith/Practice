class animal:
    def speak(self):
        print("animal_speaking")
class cat(animal):
    def miaw(self):
        print("cat crying")
c=cat()
c.speak()
c.miaw()
