from model.airport import AirportSchema
from model.city import CitySchema
from model.flight import FlightSchema
from model.seat import SeatSchema
from model.crew import CrewSchema

guarulhos = {
    "name": "Guarulhos",
    "state": "São Paulo",
    "country": "Brazil",
}

los_angeles = {
    "name": "Los Angeles",
    "state": "California",
    "country": "United States",
}

guarulhos = CitySchema().load(guarulhos)
los_angeles = CitySchema().load(los_angeles)

print(f"=== Serialized City Info ===\n{ guarulhos }\n{ los_angeles }")

guarulhos_airport = {
    # Deserializes the city object to a dictionary
    "city": CitySchema().dump(guarulhos),
    "max_departures": 10,
    "name": "Guarulhos International Airport"
}

guarulhos_airport = AirportSchema().load(guarulhos_airport)

los_angeles_airport = {
    "city": CitySchema().dump(los_angeles),
    "max_departures": 10,
    "name": "Los Angeles International Airport"
}

los_angeles_airport = AirportSchema().load(los_angeles_airport)

print(f"\n=== Serialized Airport Info ===\n{ guarulhos_airport }\n{ los_angeles_airport }")

seats = [
    {
        'id': 'A11'
    },
    {
        'id': 'A12'
    },
    {
        'id': 'A13'
    },
    {
        'id': 'A14'
    }
]

seats = SeatSchema(many=True).load(seats)

crew = [
    {
        'name': 'John Doe',
        'occupation': 'Pilot'
    },
    {
        'name': 'Jane Doe',
        'occupation': 'Co-Pilot'
    },
    {
        'name': 'John Smith',
        'occupation': 'Flight Attendant'
    },
    {
        'name': 'Jane Smith',
        'occupation': 'Flight Attendant'
    }
]

crew = CrewSchema(many=True).load(crew)

flight_a01 = {
    'type': 'International',
    'departure': AirportSchema().dump(guarulhos_airport),
    'destination': AirportSchema().dump(los_angeles_airport),
    'departure_time': '10:00:00',
    'departure_date': '2021-01-01',
    'seats': SeatSchema(many=True).dump(seats),
    'crew': CrewSchema(many=True).dump(crew)
}

flight_a01 = FlightSchema().load(flight_a01)

print(f"\n=== Serialized Flight Info ===\n{ flight_a01 }")

free_seats = flight_a01.freeSeats()

print(f"\n=== Free Seats ===")
for seat in free_seats:
    print(seat.id)

crew_members = flight_a01.showCrew()

print(f"\n=== Crew Members ===")
for crew_member in crew_members:
    print(crew_member)
