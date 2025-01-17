from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=1000)

    def __str__(self):
        return "Name: " + self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(null=False, max_length=30)

    SUV = 'suv'
    SEDAN = 'sedan'
    WAGON = 'wagon'
    TYPE_CHOICES = [(SUV, 'SUV'),(SEDAN, 'Sedan'), (WAGON, 'Wagon')]
    type = models.CharField(null=False, max_length=20, choices=TYPE_CHOICES)
    year = models.DateField(null=True)

    def __str__(self):
        return "Name: " + self.name + "," + \
                "Type: " + self.type + "," + \
                "Year: " + self.year.strftime('%Y')

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address # Dealer address
        self.city = city # Dealer city
        self.full_name = full_name # Dealer Full Name
        self.id = id # Dealer id
        self.lat = lat # Location lat
        self.long = long # Location long
        self.short_name = short_name # Dealer short name 
        self.st = st # Dealer state
        self.zip = zip # Dealer zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership # Dealer id
        self.name = name 
        self.purchase = purchase 
        self.review = review 
        self.purchase_date = purchase_date 
        self.car_make = car_make 
        self.car_model = car_model 
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id
        
    def __str__(self):
        return "Review: " + self.review +\
                "Sentiment: " + self.sentiment