import json
from flask import Flask, jsonify, request

app = Flask(__name__)


def load_cars():
    try:
        with open('cars.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_cars(cars):
    with open('cars.json', 'w') as f:
        json.dump(cars, f, indent=4)


@app.route('/cars', methods=['GET'])
def get_cars():
    cars = load_cars()
    return jsonify(cars)


@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    cars = load_cars()
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    return jsonify(car)


@app.route('/cars', methods=['POST'])
def create_car():
    new_car = request.get_json()
    cars = load_cars()

    new_car_id = max([car['id'] for car in cars], default=0) + 1
    new_car['id'] = new_car_id
    
    cars.append(new_car)
    save_cars(cars)
    return jsonify(new_car), 201


@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    updated_data = request.get_json()
    cars = load_cars()
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    car.update(updated_data)
    save_cars(cars)
    return jsonify(car)


@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    cars = load_cars()
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    cars.remove(car)
    save_cars(cars)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)


import requests
import json
import os


URL = "http://127.0.0.1:5000/cars"


def create_empty_json_file():
    if not os.path.exists('cars.json'):
        with open('cars.json', 'w') as f:
            json.dump([], f) 


def create_car(data):
    response = requests.post(URL, json=data)
    print("Create Car Response:", response.status_code, response.json())


def get_all_cars():
    response = requests.get(URL)
    print("Get All Cars Response:", response.status_code, response.json())


def get_car_by_id(car_id):
    response = requests.get(f"{URL}/{car_id}")
    print(f"Get Car with ID {car_id} Response:", response.status_code, response.json())


def update_car(car_id, updated_data):
    response = requests.put(f"{URL}/{car_id}", json=updated_data)
    print(f"Update Car with ID {car_id} Response:", response.status_code, response.json())


def delete_car(car_id):
    response = requests.delete(f"{URL}/{car_id}")
    print(f"Delete Car with ID {car_id} Response:", response.status_code)



def test_api():

    create_empty_json_file()

    cars_data = [
        {"make": "Toyota", "model": "Corolla", "year": 2020, "price": 20000},
        {"make": "Honda", "model": "Civic", "year": 2022, "price": 25000},
        {"make": "Ford", "model": "Focus", "year": 2021, "price": 22000},
    ]
    
    for car_data in cars_data:
        create_car(car_data)

    get_all_cars()

    get_car_by_id(1)

    updated_car_data = {"make": "Toyota", "model": "Corolla", "year": 2021, "price": 21000}
    update_car(1, updated_car_data)

    get_car_by_id(1)

    delete_car(2)

    get_car_by_id(2)


if __name__ == "__main__":
    test_api()

