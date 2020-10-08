from prac08.taxi import Taxi

prius = Taxi(100, "Prius 1")
prius.drive(40)
print(f"{prius} Current fare: ${prius.get_fare():.2f}")
prius.start_fare()
prius.drive(100)
print(f"{prius} Current fare: ${prius.get_fare():.2f}")

