food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.

food = food.split(',')
equipment = equipment.split(',')
pets = pets.split(',')
sleep_aids = sleep_aids.split(',')

food.sort()
equipment.sort()
pets.sort()
sleep_aids.sort()

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = [food, equipment, pets, sleep_aids]
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

userCargoSelect = int(input("Please choose a location from the cargo hold. Select from bays 0, 1, 2, or 3: "))

# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.

if (userCargoSelect >= 0 and userCargoSelect <= 3):
    print(f"You have chosen cargo hold [{userCargoSelect}]. The contents of the cargo hold are: {cargo_hold[userCargoSelect]}")
else:
    print("Invalid selection. No soup for you!")

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, 
# then print “Cabinet ____ DOES/DOES NOT contain ____.”

userCargoSelect = int(input("Please choose a location from the cargo hold. Select from bays 0, 1, 2, or 3: "))
userCargoItem = input("What item were you looking for? ")

cargoHoldString = ['food', 'equipment', 'pets', 'sleep_aids']

if userCargoItem in cargo_hold[userCargoSelect]:
    print(f"Cargo hold {cargoHoldString[userCargoSelect]} DOES contain {userCargoItem}")
else:
    print(f"Cargo hold {cargoHoldString[userCargoSelect]} DOES NOT contain {userCargoItem}")