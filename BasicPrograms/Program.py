class First:

    def __init__(self):
        self.id = 1
        self.name = "madhan"
        self.company = "legato"
        self.lap = self.Second()

    def show(self):
        print(self.id, self.name, self.company)
        self.lap.show()

    class Second:

        def __init__(self):
            self.id = 1
            self.name = "nani"
            self.company = "microsoft"
            self.brand = "BMW"

        def show(self):
            print(self.id, self.name, self.company, self.brand)


f1 = First()

f1.show()
