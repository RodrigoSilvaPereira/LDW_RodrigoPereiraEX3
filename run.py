from api import app, mongo
from api.models.car_model import Car
from api.services.car_service import CarService

if __name__ == '__main__':
    with app.app_context():
        if 'cars' not in mongo.db.list_collection_names():
            car = Car(
                model='',
                specifications={},
                year=0
            )
            CarService.add_car(car)
    app.run(port=5000, debug=True)
