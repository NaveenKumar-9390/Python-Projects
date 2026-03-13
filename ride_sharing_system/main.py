class Driver:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.available = True


class RideSharingSystem:
    def __init__(self):
        self.drivers = []

    def add_driver(self):
        name = input("Driver name: ")
        location = int(input("Driver location: "))
        driver = Driver(name, location)
        self.drivers.append(driver)
        print("Driver added")

    def request_ride(self):
        rider = input("Rider name: ")
        pickup = int(input("Pickup location: "))
        nearest_driver = None
        min_distance = float('inf')

        for driver in self.drivers:
            if driver.available:
                distance = abs(driver.location - pickup)
                if distance < min_distance:
                    min_distance = distance
                    nearest_driver = driver

        if nearest_driver:
            nearest_driver.available = False
            print("Ride assigned!")
            print("Driver:", nearest_driver.name)
        else:
            print("No drivers available")

    def complete_ride(self):
        name = input("Driver name: ")
        for driver in self.drivers:
            if driver.name == name:
                driver.available = True
                print("Ride completed")
                return
        print("Driver not found")

    def list_drivers(self):
        for d in self.drivers:
            status = "Available" if d.available else "Busy"
            print(d.name, "| Location:", d.location, "|", status)


def main():
    system = RideSharingSystem()
    while True:
        print("\n1 Add Driver")
        print("2 Request Ride")
        print("3 Complete Ride")
        print("4 List Drivers")
        print("5 Exit")
        choice = input("Choice: ")

        if choice == "1":
            system.add_driver()
        elif choice == "2":
            system.request_ride()
        elif choice == "3":
            system.complete_ride()
        elif choice == "4":
            system.list_drivers()
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
