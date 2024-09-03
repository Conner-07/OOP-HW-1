import csv

class Car:
    """
    A class to represent a car in the inventory.
    
    Attributes:
        make (str): Manufacturer of the car.
        model (str): Model of the car.
        year (int): Manufacturing year.
        mileage (int): Mileage of the car.
        engine (str): Type of engine.
        transmission (str): Transmission type.
        drivetrain (str): Drivetrain type.
        mpg (int): Miles per gallon.
        ext_color (str): Exterior color of the car.
        int_color (str): Interior color of the car.
        accident (str): Accident history.
        price (int): Price of the car.
    """

    def __init__(self, make, model, year, mileage, engine, transmission, drivetrain, mpg, ext_color, int_color, accident, price):
        self.make = make
        self.model = model
        self.year = year 
        self.mileage = mileage
        self.engine = engine
        self.transmission = transmission
        self.drivetrain = drivetrain 
        self.mpg = mpg
        self.ext_color = ext_color
        self.int_color = int_color
        self.accident = accident
        self.price = price

    def paint(self, color):
        """Change the exterior color of the car."""
        self.ext_color = color
    
    def repair(self, part, replacement):
        """Replace a part of the car."""
        if part == 'engine':
            self.engine = replacement
        elif part == 'transmission':
            self.transmission = replacement
        elif part == 'drivetrain':
            self.drivetrain = replacement
        else:
            print("Invalid part specified.")
    
    def reupholster(self, color):
        """Change the interior color of the car."""
        self.int_color = color
    
    def drive(self, miles):
        """Increase the mileage of the car."""
        self.mileage += miles
    
    def modify_price(self, new_price):
        """Change the price of the car."""
        if new_price < 1:
            discount = self.price * new_price
            new_price = self.price - discount
            print(f"New discounted price: {new_price}")
            confirm = input("Is this the correct desired amount? (yes/no): ")
            if confirm.lower() == 'yes':
                self.price = new_price
            else:
                print("Price modification canceled.")
        else:
            self.price = new_price

    @classmethod
    def from_csv(cls, file_path):
        car_objects = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = cls(
                    make=row['make'],
                    model=row['model'],
                    year=int(row['year']),
                    mileage=int(row['mileage']),
                    engine=row['engine'],
                    transmission=row['transmission'],
                    drivetrain=row['drivetrain'],
                    mpg=int(row['mpg']),
                    ext_color=row['exterior_color'],
                    int_color=row['interior_color'],
                    accident=row['accident'],
                    price=int(row['price'])
                )
                car_objects.append(obj)
        return car_objects

class Seller:
    """
    A class to represent a seller.
    
    Attributes:
        name (str): Name of the seller.
        rating (float): Rating of the seller.
        inventory (list): List of cars in the seller's inventory.
    """

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.inventory = []

    def buy(self, car):
        """Add a car to the seller's inventory."""
        if car not in self.inventory:
            self.inventory.append(car)
            print(f"Car {car.make} {car.model} added to inventory.")
        else:
            print("Car is already in the inventory.")

    def sell(self, car):
        """Remove a car from the seller's inventory."""
        if car in self.inventory:
            self.inventory.remove(car)
            print(f"Car {car.make} {car.model} sold from inventory.")
        else:
            print("Car not found in inventory.")



file_path = 'Macintosh HD/Users/connerstarkey/Downloads/cars.csv' 
car_objects = Car.from_csv(file_path)

for car in car_objects:
    print(f'Make: {car.make}, Model: {car.model}, Year: {car.year}, Mileage: {car.mileage}')
    print(f'Engine: {car.engine}, Transmission: {car.transmission}, Drivetrain: {car.drivetrain}')
    print(f'MPG: {car.mpg}, Exterior Color: {car.ext_color}, Interior Color: {car.int_color}')
    print(f'Accident History: {car.accident}, Price: {car.price}')
    print('---')

seller = Seller("John's Used Cars", 4.5)
seller.buy(car_objects[0])
seller.sell(car_objects[0])
