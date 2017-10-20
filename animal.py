class Animal:
    def __init__(self, kind, place):
        self.kind = kind
        self.place = place

    def get_kind(self):
    	return self.kind
    
class Dog(Animal):
    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed

    def speak(self):
    	return "woof!!"

class Cat(Animal):
    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed
    def speak(self):
    	return "meow!!"
    	
Mickey = Dog('Mickey', 'Male', 'Bulldog')
Flora = Dog('Flora','Female','Pug')
Tina = Cat('Tina','Female','Persian')
Tina.speak()
Mickey.speak()