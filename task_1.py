from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> "Car":
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> "Motorcycle":
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


def main() -> None:
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Ducati", "Monster")
    vehicle2.start_engine()


if __name__ == "__main__":
    main()
