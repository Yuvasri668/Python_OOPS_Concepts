class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False

mobile1 = Mobile("Samsung", "Galaxy S21", 70000)
mobile2 = Mobile("Samsung", "Galaxy S21", 65000)
mobile3 = Mobile("Apple", "iPhone 14", 80000)

print(mobile1 == mobile2)  
print(mobile1 == mobile3) 
