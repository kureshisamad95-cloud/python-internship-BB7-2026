class Car:
    def _init_(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"My car is {self.brand} {self.model}, manufactured in {self.year}.")


car1 = Car("Toyota", "Fortuner", 2024)
car2 = Car("BMW", "X5", 2023)
car3 = Car("Honda", "City", 2022)

car1.display_info()
car2.display_info()
car3.display_info()