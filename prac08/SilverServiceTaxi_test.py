from prac08.SilverServiceTaxi import SilverServiceTaxi


hummer = SilverServiceTaxi(100, "Hummer", 2)
hummer.drive(18)
print(f"Fare = {hummer.get_fare():.2f}")
print(hummer)