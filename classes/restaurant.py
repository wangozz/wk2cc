class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def average_star_rating(self):
        total_rating = sum([review.rating for review in self.reviews])
        return total_rating / len(self.reviews) if self.reviews else 0

    def reviews(self):
        return self.reviews

    def customers(self):
        reviewers = [review.customer for review in self.reviews]
        return list(set(reviewers))
