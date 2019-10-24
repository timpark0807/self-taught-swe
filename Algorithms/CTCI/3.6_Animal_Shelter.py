import unittest

class AnimalShelter:
    
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.overall = []

    def enqueue(self, animal, name):
        self.overall.append(name)
        if animal == 'dog':
            self.dogs.append(name)
        elif animal == 'cat':
            self.cats.append(name)

    def dequeueAny(self):
        adopt = self.overall.pop(0)
        if self.dogs != [] and adopt == self.dogs[0]:
            self.dogs.pop(0)
        elif self.cats != [] and adopt == self.cats[0]:
            self.cats.pop(0)
        return adopt

    def dequeueDog(self):
        if self.dogs != []:
            adopt = self.dogs.pop(0)
            for index, name in enumerate(self.overall):
                if name == adopt:
                    self.overall.pop(index)
            return adopt

    def dequeueCat(self):
        if self.cats != []:
            adopt = self.cats.pop(0)
            for index in range(len(self.overall)):
                if self.overall[index] == adopt:
                    self.overall.pop(index)
                    break
            return adopt


class TestSolution(unittest.TestCase):
    def test_valid(self):
            a = AnimalShelter()
            output = []
            a.enqueue('dog', 'rex')
            a.enqueue('dog', 'spot')
            a.enqueue('cat', 'will')
            a.enqueue('cat', 'garfield')
            a.enqueue('dog', 'bud')
            output.append(a.dequeueAny())
            output.append(a.dequeueCat())
            output.append(a.dequeueAny())

            self.assertEqual(output, ['rex', 'will', 'spot'])

            
if __name__ == '__main__':
    unittest.main()


    
