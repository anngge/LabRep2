class Person:
    name = "Angeliza"
    age = 20

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return {'name': sellf.name, 'age': self.age}

    def __str__(self):
        return 'personName(name=' + self.name + 'age=' + str(self.age) + ')'

