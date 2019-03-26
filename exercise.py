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

    def __str__(self):
        return "{}".format(self.name)


class Trip:

    def __init__(self):
        self.destinations = []

    def addLocation(self, location):
        self.destinations.append(location)

    def printTrip(self):
        i = 0
        print("Began trip.")
        for i in range(len(self.destinations) - 1):
            print("Travelled from {} to {}.".format(self.destinations[i], self.destinations[i + 1]))
        i =+ 1
        print("Ended trip.")


toronto = Location("Toronto")
ottawa = Location("Ottawa")
montreal = Location("Montreal")
quebec = Location("Quebec City")
halifax = Location("Halifax")
stjohns = Location("St. John's")
trip1 = Trip()
trip1.addLocation(toronto)
trip1.addLocation(ottawa)
trip1.addLocation(montreal)
trip1.addLocation(quebec)
trip1.addLocation(halifax)
trip1.addLocation(stjohns)
trip1.printTrip()
