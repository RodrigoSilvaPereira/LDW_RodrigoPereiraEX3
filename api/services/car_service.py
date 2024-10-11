from api import mongo
from ..models import car_model
from bson import ObjectId

class CarService:
    @staticmethod
    def add_car(car):
        result = mongo.db.cars.insert_one({
            'model': car.model,
            'specifications': car.specifications,
            'year': car.year,
        })
        return mongo.db.cars.find_one({'_id': ObjectId(result.inserted_id)})

    @staticmethod
    def get_cars():
        return list(mongo.db.cars.find())

    # Função para coletar registro único - listar um único carro
    @staticmethod
    def get_car_by_id(id):
        return mongo.db.cars.find_one({'_id': ObjectId(id)})

    def update_car(self, id):
        # Atualiza o carro e retorna o documento atualizado
        updated_car = mongo.db.cars.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': {
                'model': self.model,
                'specifications': self.specifications,
                'year': self.year,
            }},
            return_document=True  # Garante que o documento retornado seja atualizado
        )
        return updated_car

    @staticmethod
    def delete_car(id):
        mongo.db.cars.delete_one({'_id': ObjectId(id)})
