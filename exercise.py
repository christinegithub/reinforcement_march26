# Create a Location class with a name.
#
# Create a Trip class with a list of Location instances (called stops or destinations or something similar).
# Define a method that lets you add locations to the trip's list of destinations.
#
# Make several instances of Locations and add them to an instance of Trip.
#
# Define a method in the Trip class that iterates through the list of locations and prints something
# similar to the following:

class Location:

    def __init__(self, name):
        self.name = name

    # def printStations():
    #     print("printing stations")

# class Trip:
#
#     def __init__(self, destinations = []):
#         self.destinations = destinations
#
#     def addLocations(self):
#         self.destinations.push(Location(name))
#         return self.destinations


class Trip:

    def __init__(self, destinations = []):
        self.destinations = destinations

    def printTrip(destinations):
        i = 1
        # destinations = []
        destinations = ["Toronto", "Ottawa", "Montreal", "Quebec City", "Halifax", "St. John's"]
        print("Began trip.")
        for i in range(len(destinations) - 1):
            print("Travelled from {} to {}.".format(destinations[i], destinations[i + 1]))
            i =+ 1
        print("Ended trip.")


destinations = Trip(["Toronto", "Ottawa", "Montreal", "Quebec City", "Halifax", "St. John's"])
Trip.printTrip(destinations)
