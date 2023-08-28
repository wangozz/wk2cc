class Customer:
    all_customers = []  # A list to keep track of all customer instances

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)  # Add the customer instance to the list

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers  # Return the list of all customer instances


class Restaurant:
    all_restaurants = []  # A list to keep track of all restaurant instances

    def __init__(self, name):
        self.name = name
        Restaurant.all_restaurants.append(self)  # Add the restaurant instance to the list

    def name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.all_restaurants  # Return the list of all restaurant instances


class Review:
    all_reviews = []  # A list to keep track of all review instances

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)  # Add the review instance to the list

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews  # Return the list of all review instances

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant


# Additional Methods

# Review class
def Review_customer(self):
    return self.customer

def Review_restaurant(self):
    return self.restaurant

# Restaurant class
def Restaurant_reviews(self):
    return [review for review in Review.all() if review.restaurant == self]

def Restaurant_customers(self):
    return [review.customer for review in Review.all() if review.restaurant == self]

# Customer class
def Customer_restaurants(self):
    return [review.restaurant for review in Review.all() if review.customer == self]

def Customer_add_review(self, restaurant, rating):
    Review(self, restaurant, rating)

def Customer_num_reviews(self):
    return len([review for review in Review.all() if review.customer == self])

@classmethod
def Customer_find_by_name(cls, name):
    for customer in cls.all():
        if customer.full_name() == name:
            return customer

@classmethod
def Customer_find_all_by_given_name(cls, name):
    return [customer for customer in cls.all() if customer.given_name == name]

# Restaurant class
def Restaurant_average_star_rating(self):
    reviews = [review.rating for review in Review.all() if review.restaurant == self]
    if reviews:
        return sum(reviews) / len(reviews)
    else:
        return 0
