class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('vat mango')

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

# Override
    def eat(self):
        print('vegetables')

    def exercise(self):
        print('gym e poisa diya')

# + sign operator overload
    def __add__(self, other):
        return self.age + other.age
    
    # * sign overload
    def __mul__(self, other):
        return self.weight * other.weight
    
    # len overload
    def __len__(self):
        return self.height
    
    def __gt__(self, other):
        return self.age > other.age

sakib = Cricketer('sakib', 38, 68, 91, 'BD')
Mushi = Cricketer('sakib', 36, 67, 94, 'BD')

# sakib.eat()
# sakib.exercise()

# plus sign overload
print(45+63)
print('sakib' + 'Rakib')
print([12, 98] + [5, 6,7,1,2])
print(sakib + Mushi)
print(sakib * Mushi)
print(len(sakib))
print(sakib > Mushi)