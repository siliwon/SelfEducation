class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = str(brand + ' ' + model)

laptop1 = Laptop('hp', 'werw', 15)
laptop2 = Laptop('intel', 'aaaa', 16)

print(laptop1.laptop_name)
print(laptop2.laptop_name)