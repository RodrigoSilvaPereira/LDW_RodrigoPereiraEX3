from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import car_schema
from ..models import car_model
from ..services import car_service
from ..services.car_service import CarService


class CarList(Resource):
    def get(self):
        cars = CarService.get_cars()
        car_schema_inst = car_schema.CarSchema(many=True)
        return make_response(car_schema_inst.jsonify(cars), 200)
    
    def post(self):
        car_schema_inst = car_schema.CarSchema()
        json_data = request.get_json()

        # Valida os dados recebidos
        validate = car_schema_inst.validate(json_data)
        if validate:  # Se houver erros de validação
            return make_response(jsonify(validate), 400)

        new_car = car_model.Car(
            model=json_data['model'],
            specifications=json_data['specifications'],
            year=json_data['year']
        )

        # Adiciona o carro ao banco de dados
        result = CarService.add_car(new_car)
        res = car_schema_inst.jsonify(result)
        return make_response(res, 201)


class CarDetails(Resource):
    def get(self, id):
        car = CarService.get_car_by_id(id)
        if car is None:
            return make_response(jsonify({"message": "Car not found"}), 404)
        car_schema_inst = car_schema.CarSchema()
        return make_response(car_schema_inst.jsonify(car), 200)  # OK

    def put(self, id):
        car_bd = CarService.get_car_by_id(id)
        if car_bd is None:
            return make_response(jsonify("Car not found!"), 404)
        car_schema_inst = car_schema.CarSchema()
        validate = car_schema_inst.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_car = car_model.Car(**json_data)
            updated_car = CarService.update_car(new_car, id)
            return make_response(car_schema_inst.jsonify(updated_car), 200)

    def delete(self, id):
        car_bd = CarService.get_car_by_id(id)
        if car_bd is None:
            return make_response(jsonify("Car not found"), 404)
        CarService.delete_car(id)
        return make_response(jsonify("Car deleted successfully!"), 200)


api.add_resource(CarList, '/cars')
api.add_resource(CarDetails, '/car/<id>')
