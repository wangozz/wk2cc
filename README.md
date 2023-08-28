# wk2cc
# Customer, Restaurant, and Review Management System

This Python program provides a simple management system for tracking customers, restaurants, and reviews. It allows you to create instances of customers, restaurants, and reviews, and perform various operations related to them.

## Table of Contents

- [Classes](#classes)
  - [Customer](#customer)
  - [Restaurant](#restaurant)
  - [Review](#review)
- [Additional Methods](#additional-methods)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Classes

### Customer

The `Customer` class represents a customer with a given name and family name. It keeps track of all customer instances and allows you to retrieve their information.

- `given_name`: The given name of the customer.
- `family_name`: The family name of the customer.
- `full_name()`: Returns the full name of the customer.
- `all()`: Returns a list of all customer instances.

### Restaurant

The `Restaurant` class represents a restaurant with a name. It maintains a list of all restaurant instances and provides methods to access their information.

- `name`: The name of the restaurant.
- `all()`: Returns a list of all restaurant instances.

### Review

The `Review` class represents a review submitted by a customer for a restaurant. It stores information about the customer, restaurant, and rating of the review. The class also keeps track of all review instances.

- `customer`: The customer who submitted the review.
- `restaurant`: The restaurant being reviewed.
- `rating`: The rating given in the review.
- `all()`: Returns a list of all review instances.

## Additional Methods

Additional methods are provided to extend the functionality of the existing classes.

### Review class

- `Review_customer(self)`: Returns the customer who submitted the review.
- `Review_restaurant(self)`: Returns the restaurant being reviewed.

### Restaurant class

- `Restaurant_reviews(self)`: Returns a list of reviews for the restaurant.
- `Restaurant_customers(self)`: Returns a list of customers who reviewed the restaurant.
- `Restaurant_average_star_rating(self)`: Calculates and returns the average star rating for the restaurant.

### Customer class

- `Customer_restaurants(self)`: Returns a list of restaurants reviewed by the customer.
- `Customer_add_review(self, restaurant, rating)`: Adds a review by the customer for a specific restaurant.
- `Customer_num_reviews(self)`: Returns the number of reviews submitted by the customer.
- `Customer_find_by_name(cls, name)`: Finds a customer by their full name.
- `Customer_find_all_by_given_name(cls, name)`: Finds all customers with a given name.

## Usage

To use this code, create instances of customers, restaurants, and reviews using the provided classes. You can then utilize the various methods to retrieve information, perform operations, and manage reviews.

Example usage:

```python
# Creating instances
alice = Customer("Alice", "Johnson")
pizza_place = Restaurant("Pizza Place")
review1 = Review(alice, pizza_place, 4)

# Using methods
restaurant_reviews = pizza_place.Restaurant_reviews()
alice_reviews = alice.Customer_num_reviews()

# Additional methods
average_rating = pizza_place.Restaurant_average_star_rating()

print(f"{pizza_place.name} average rating: {average_rating}")
