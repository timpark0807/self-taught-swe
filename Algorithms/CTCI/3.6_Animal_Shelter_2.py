import unittest

class AnimalShelter:
    
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, animal, name):
        if animal == 'dog':
            self.dogs.append((name, self.order))
            self.order += 1
            
        elif animal == 'cat':
            self.cats.append((name, self.order))
            self.order += 1

    def dequeueAny(self):
        if self.dogs != [] and self.dogs[0][1] < self.cats[0][1]:
            adopt = self.dogs.pop(0)[0]
        elif self.cats != [] and self.cats[0][1] < self.dogs[0][1]:
            adopt = self.cats.pop(0)[0]
        return adopt

    def dequeueDog(self):
        if self.dogs != []:
            adopt = self.dogs.pop(0)[0]
            return adopt

    def dequeueCat(self):
        if self.cats != []:
            adopt = self.cats.pop(0)[0]
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


    
