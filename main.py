from classes.customer import Customer
from classes.review import Review
from classes.restaurant import Restaurant

customer1 = Customer("Sam", "Abel")
customer2 = Customer("Kim", "Omondi")

restaurant1 = Restaurant("Java")
restaurant2 = Restaurant("Chicken Inn")

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

for review in Review.all():
    print(f"{review.customer.full_name()} reviewed {review.restaurant.name()} with a rating of {review.rating}")

for restaurant in Restaurant.all():
    print(f"The average rating for {restaurant.name} is {restaurant.average_star_rating()}")

for restaurant in Restaurant.all():
    print(f"Customers who reviewed {restaurant.name}: {[customer.full_name() for customer in restaurant.customers()]}")

for customer in Customer.all():
    print(f"{customer.full_name()} reviewed {[restaurant.name for restaurant in customer.restaurants()]}")

found_customer = Customer.find_by_name("Sam Abel")
print(f"Found customer: {found_customer.full_name()}")

found_customers = Customer.find_all_by_given_name("Kim")
print(f"All customers with given name 'Kim': {[customer.full_name() for customer in found_customers]}")

for customer in Customer.all():
    print(f"{customer.full_name()} authored {customer.num_reviews()} reviews.")
