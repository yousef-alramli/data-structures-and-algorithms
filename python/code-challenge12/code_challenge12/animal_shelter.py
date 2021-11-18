
class Animal:
    def __init__(self,value):
        self.next = None
        self.value = value

class Dog(Animal):
    def __init__(self, value):
        Animal.__init__(self, value)

class Cat(Animal):
    def __init__(self, value):
        Animal.__init__(self, value)

class AnimalShelter:
    def __init__(self):
        self.rear = None
        self.front = None

    
    def enqueue(self,animal):        
        if self.rear == None:
            self.rear = animal
            self.front = animal
        else:
            self.rear.next = animal
            self.rear = animal
        
    
    def dequeue(self, pref=None):

        if self.rear == None:
            raise Exception("Sorry, this queue is empty")
        if pref == "Dog":
            while not isinstance(self.front, Dog):
                if self.front == None:
                    return "None"
                self.front = self.front.next
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        if pref == "Cat":
            while not isinstance(self.front, Cat):
                if self.front == None:
                    return "None"
                self.front = self.front.next
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            return "None"    


if __name__ == "__main__":
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("losy"))
    animal_shelter.enqueue(Cat("candy"))
    animal_shelter.enqueue(Dog("soso"))
    animal_shelter.enqueue(Cat("black"))
    print(animal_shelter.dequeue("Dog"))
    print(animal_shelter.dequeue("Cat"))
    print(animal_shelter.dequeue("Cat"))
