from model.airport import AirportSchema
from model.city import CitySchema
from model.flight import FlightSchema

from db import city_list, airport_list, flight_list

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


"""City related routes and methods"""

# List all created cities
@app.route('/city', methods=['GET'])
def get_cities():
    return make_response(jsonify(
        cities=CitySchema(many=True).dump(city_list)
    ), 200)

# Create a new city object
@app.route('/city/add', methods=['POST'])
def add_city():
    city = {
        "name": request.json["name"],
        "state": request.json["state"],
        "country": request.json["country"]
    }

    schema = CitySchema().load(city)

    city_list.append(schema)

    return make_response(jsonify(
        message="City added successfully!",
        city=CitySchema().dump(schema)
    ), 200)

"""Airport related routes and methods"""

# List all created airports
@app.route('/airport', methods=['GET'])
def get_airports():
    return make_response(jsonify(
        airports=AirportSchema(many=True).dump(airport_list)
    ), 200)

# Create a new airport object
@app.route('/airport/add', methods=['POST'])
def add_airport():
    """ 
    Get a city object from city list that matches the city name sent in the request
        If there isn't any city with this name, return a 404 error 
    """
    try:
        city = [city for city in city_list if city["name"] == request.json["city"]][0]
    except IndexError:
        return make_response(jsonify(
            message="Sorry! There isn't any city with this name!",
            city=request.json["city"]
        ), 404)

    airport = {
        "city": city, # City object from city list
        "max_departures": request.json["max_departures"],
        "name": request.json["name"]
    }

    schema = AirportSchema().load(airport)

    airport_list.append(schema)

    return make_response(jsonify(
        message="Airport added successfully!",
        airport=AirportSchema().dump(schema)
    ), 200)
                                     
"""Flight related routes and methods"""

# List all created flights
@app.route('/flight', methods=['GET'])
def get_flights():
    return make_response(jsonify(
        flights=FlightSchema(many=True).dump(flight_list)
    ), 200)

# List all created flights by city destination
@app.route('/flight/destination/<destination>', methods=['GET'])
def get_flight_by_destination(destination: str):
    """
    Verify if there is any flight scheduled to this destination
        If there isn't any flight scheduled to this destination, return a 404 error
    """
    try:
        flight = [flight for flight in flight_list if flight["destination"]["city"]["name"] == str(destination)][0]
    except IndexError:
        return make_response(jsonify(
            message="Sorry! There isn't any flight scheduled to this destination!",
            destination=destination
        ), 404)
    
    return make_response(jsonify(
        flight=FlightSchema().dump(flight)
    ), 200)

# List all created flights by city departure
@app.route('/flight/departure/<departure>', methods=['GET'])
def get_flight_by_departure(departure: str):
    """
    Verify if there is any flight scheduled from this departure
        If there isn't any flight scheduled from this departure, return a 404 error    
    """
    try:
        flight = [flight for flight in flight_list if flight["departure"]["city"]["name"] == str(departure)][0]

    except IndexError:
        return make_response(jsonify(
            message="Sorry! There isn't any flight scheduled from this departure!",
            destination=departure
        ), 404)


    return make_response(jsonify(
        flight=FlightSchema().dump(flight)
    ), 200)

# List all created flights by National | International
@app.route('/flight/type/<flight_type>', methods=['GET'])
def get_flight_by_type(flight_type: str):
    flight_type = flight_type.capitalize()

    """
    Verify if there is any flight of this type
        If there isn't any flight of this type, return a 404 error
    """
    try:
        flight = [flight for flight in flight_list if flight["type"] == str(flight_type)]

    except IndexError:
        return make_response(jsonify(
            message="Sorry! There isn't any flight of this type!",
            destination=flight_type
        ), 404)

    return make_response(jsonify(
        flight=FlightSchema(many=True).dump(flight)
    ), 200)

# Create a new flight object
@app.route('/flight/add', methods=['POST'])
def add_flight():
    """
    Verify if both departure and destination exist on airport list
        If there isn't any airport with this name, return a 404 error    
    """
    try:
        departure = [airport for airport in airport_list if airport["name"] == request.json["departure"]["name"]][0]
        destination = [airport for airport in airport_list if airport["name"] == request.json["destination"]["name"]][0]

    except IndexError:
        return make_response(jsonify(
            message="Sorry! There isn't any airport with this name!",
            departure=request.json["departure"],
            destination=request.json["destination"]
        ), 404)
    
    """
    Verify if departure and destination are different
        If they are the same, return a 400 error    
    """
    if departure == destination:
        return make_response(jsonify(
            message="Sorry! Departure and destination can't be the same!",
            departure=request.json["departure"],
            destination=request.json["destination"]
        ), 400)
    
    """
    Verify if the flight has at least 5 seats
        If it has less than 5 seats, return a 400 error    
    """
    if len(request.json['seats']) < 5:
        return make_response(jsonify(
            message="Sorry! A flight must have at least 10 seats!",
            seats=request.json["seats"]
        ), 400)

    flight = {
        "departure": departure,
        "destination": destination,
        "type": request.json["type"],
        "seats": request.json["seats"],
        "crew": request.json["crew"],
        "departure_date": request.json["departure_date"],
        "departure_time": request.json["departure_time"],
    }

    schema = FlightSchema().load(flight)

    flight_list.append(schema)

    return make_response(jsonify(
        message="Flight added successfully!",
        flight=FlightSchema().dump(schema)
    ), 200)

app.run(debug=True)