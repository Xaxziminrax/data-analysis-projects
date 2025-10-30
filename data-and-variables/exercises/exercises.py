# 1. Declare and assign the variables here:

shuttleName = "Determination"
shuttleSpeedMPH = 17500
marsDistanceKM = 225000000
moonDistanceKM = 384400
milesPerKilometer = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.

print(type(shuttleName))
print(type(shuttleSpeedMPH))
print(type(marsDistanceKM))
print(type(moonDistanceKM))
print(type(milesPerKilometer))

# Code your solution to exercises 3 and 4 here:

milesToMars = marsDistanceKM * shuttleSpeedMPH
hrsToMars = milesToMars / shuttleSpeedMPH
daysToMars = hrsToMars / 24

print(shuttleName + " will take " + str(daysToMars) + " days to reach Mars.")


# Code your solution to exercise 5 here

milesToMoon = moonDistanceKM * shuttleSpeedMPH
hrsToMoon = milesToMoon / shuttleSpeedMPH
daysToMoon = hrsToMoon / 24
print(shuttleName + " will take " + str(daysToMoon) + " days to reach da MOON.")