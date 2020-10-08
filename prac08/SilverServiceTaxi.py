from prac08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, fuel, name, fanciness):
        super().__init__(fuel, name)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        self.current_fare_distance = 0

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagfall
