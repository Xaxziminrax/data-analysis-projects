# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

fuel_level = 69
number_of_asstronauts = 5
shuttle_altitude = 10

fuel_level = int(input('Please enter the fuel level: '))



# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 

while (fuel_level < 5000 or fuel_level > 30000):
    fuel_level = int(input("Unsafe fuel level chosen. Please input a fuel level between 5000 and 30000: "))

print("Excellent choice, fuel level specified as: " + str(fuel_level))



# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
number_of_asstronauts = int(input("How many Astronauts are there on board? "))

while (number_of_asstronauts < 1 or number_of_asstronauts > 7):
    number_of_asstronauts = int(input("Number of Astronauts cannot be less than 1 or more than 7: "))

print("Affirmative, there are " + str(number_of_asstronauts) + " Astronauts on board.")
  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.

while (fuel_level > 100*number_of_asstronauts):
    fuel_level -= number_of_asstronauts * 100
    shuttle_altitude += 50
    print("Shuttle altitude is now: " + str(shuttle_altitude) + ", " + str(fuel_level) + "kg of fuel remain")

print("Shuttle can go no higher. Final altitude reached is: " + str(shuttle_altitude))
# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

print("The shuttle gained an altitude of ", shuttle_altitude, "km and has ", fuel_level, "kg of fuel left.")

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”

if shuttle_altitude > 2000:
  print("Orbit achieved!")
else:
  print("Failed to reach orbit. F's in the chat")