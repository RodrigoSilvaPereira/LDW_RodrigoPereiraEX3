from api import mongo

class Car:
    def __init__(self, model, specifications, year):
        self.model = model
        self.specifications = specifications
        self.year = year

    def to_dict(self):
        return {
            'model': self.model,
            'specifications': self.specifications,
            'year': self.year,
        }
