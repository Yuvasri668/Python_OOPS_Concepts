class emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{self.name} ({self.salary})"

    def __len__(self):
        return 6   

    def __add__(self, other):
        return emp(
            self.name + " + " + other.name,
            self.salary + other.salary
        )

e1 = emp("Abhi", 50000)
e2 = emp("Balu", 10000)
e3 = emp("Chandu", 20000)

print(e1 + e2 + e3)
