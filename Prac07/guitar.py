
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        self.age = 2016 - self.year
        print("The {} is {} years old.".format(self.name, self.age))

    def is_vintage(self):
        self.get_age()
        if self.age >= 50:
            print("{} is vintage".format(self.name))
