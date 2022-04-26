from Driver import Driver
from account import Account
from car import Car
from UberX import UberX

if __name__ == "__main__":
    print("Hola Mundo")
    account = Account("Andres Herrera","70585583")
    car = Car("AMS234",account)
    print(vars(car))

    account2 = Account("Marta Herrera","70585583")
    car2 = Car("QWE567",account2)
    print(vars(car2))

    uber = UberX("asdassLicense", account2,"BRANDSSS", "MODELXXX")
    print(vars(uber))

    driver = Driver("nieve", "60484922", 2, "A3")
    print(vars(driver))