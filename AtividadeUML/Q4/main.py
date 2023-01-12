from crew_role import Crew_Role

r1 = Crew_Role.commander
r2 = Crew_Role.co_pilot
r3 = Crew_Role.flight_attendant
r4 = Crew_Role.flight_mecanic

from crew import Crew

commander_latam = Crew("Leonardo", "46578412322", "leo@latam.com", "1145658712", r1)
co_pilot_latam = Crew("Marcos", "16584513456", "marcos@latam.com", "1135486874", r2)
attendant_latam = Crew("Estefani", "231564868461", "estefani@latam.com", "1135441241", r3)
mecanic_latam = Crew("Breno", "2351564815", "breno@latam.com", "11345416515", r4)

from city import City

guarulhos = City("Guarulhos", "SP", "Brasil")
rio = City("Rio de Janeiro", "RJ", "Brasil")

from airport import Airport

gru_airport = Airport("GRU Airport", guarulhos, 10)
gal_airport = Airport("Galeão Airport", rio, 5)

from type_flight import Type_Flight

tf1 = Type_Flight.international
tf2 = Type_Flight.national

from flight import Flight

flight_latam = Flight('LAZ-1541', 32, tf2, gru_airport, gal_airport, 2023, 1, 13, 13, 30)
flight_latam.add_crew(commander_latam)
flight_latam.add_crew(co_pilot_latam)   
flight_latam.add_crew(attendant_latam)
flight_latam.add_crew(mecanic_latam)

print("--------Flight--------\n\n", flight_latam)

from passenger import Passenger

passenger_latam = Passenger("Mauro", "43123451534", "mauro@email.com", "1113546184", 42.9)

from operators import Operators

operator_latam = Operators("Márcia", "3242545453", "marcia@latam.com","4234325543","3")

booking_one = operator_latam.new_booking(passenger_latam, flight_latam)
print("\n\n--------Booking--------\n\n", booking_one)
