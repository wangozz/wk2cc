# Restaurant Review System

This project implements a simple restaurant review system using Python classes. It includes classes for `Customer`, `Review`, and `Restaurant`, each with specific functionalities as described in the code challenge.

## Files

- `customer.py`: Contains the `Customer` class with methods for managing customer information and reviews.
- `review.py`: Contains the `Review` class responsible for managing reviews.
- `restaurant.py`: Contains the `Restaurant` class with methods for managing restaurant information and reviews.
- `main.py`: Provides a testing script to demonstrate the functionality of the implemented classes.

## How to Use

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal or command prompt.
4. Run the `main.py` file with the command `python main.py`.
5. The script will execute and demonstrate various functionalities of the classes.

## Class Details

### Customer

- `__init__(self, given_name, family_name)`: Initializes a new customer with given and family names.
- `get_given_name(self)`: Returns the given name of the customer.
- `get_family_name(self)`: Returns the family name of the customer.
- `full_name(self)`: Returns the full name of the customer.
- `all()`: Returns a list of all created customers.
- `restaurants(self)`: Returns a list of unique restaurants reviewed by the customer.
- `add_review(self, restaurant, rating)`: Adds a new review associated with the customer.

### Review

- `__init__(self, customer, restaurant, rating)`: Initializes a new review with a customer, restaurant, and rating.
- `get_rating(self)`: Returns the rating of the review.
- `all()`: Returns a list of all created reviews.
- `customer(self)`: Returns the associated customer object.
- `restaurant(self)`: Returns the associated restaurant object.

### Restaurant

- `__init__(self, name)`: Initializes a new restaurant with a name.
- `get_name(self)`: Returns the name of the restaurant.
- `all()`: Returns a list of all created restaurants.
- `average_star_rating(self)`: Calculates and returns the average star rating of the restaurant based on reviews.
- `reviews(self)`: Returns a list of reviews for the restaurant.
- `customers(self)`: Returns a list of unique customers who reviewed the restaurant.

## Testing

You can add further test cases to `main.py` to evaluate the functionalities of the classes.

## Contributors

- [Wango](https://github.com/wangozz) 


