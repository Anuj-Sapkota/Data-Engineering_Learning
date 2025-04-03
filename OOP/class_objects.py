class Animal:
    def __init__(self, name, classification):
        self.name = name
        self.classification = classification
    def info(self):
        return f"The animal is {self.name} with class {self.classification}."

dog = Animal("dog", "Animalia")
print(dog.info())
