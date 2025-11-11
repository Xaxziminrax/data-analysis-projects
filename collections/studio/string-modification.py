my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

originString = my_string
modString = my_string[3:]
threeString = my_string[0:3]
my_string = modString
#print(modString)
#print(threeString)
my_string = my_string + threeString
#print(my_string)

# Use a template literal to print the original and modified string in a descriptive phrase.

#print(f"The original string is {originString}, the modified string is {my_string}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

my_string = originString
charCount = int(input("Enter number of characters to modify here: "))
#print(charCount)
nuModString = my_string[charCount:]
nuThreeString = my_string[0:charCount]
my_string = nuModString
my_string = my_string + nuThreeString
print(my_string)

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

my_string = originString
charCount = int(input("Enter number of characters to modify here: "))
if charCount > 0 and charCount <= 7:
    nuModString = my_string[charCount:]
    nuThreeString = my_string[0:charCount]
    my_string = nuModString
    my_string = my_string + nuThreeString
    print(my_string)
else:
    charCount = 3
    nuModString = my_string[charCount:]
    nuThreeString = my_string[0:charCount]
    my_string = nuModString
    my_string = my_string + nuThreeString
    print(f"Incorrect choice, bozo. Default of {charCount} chosen instead")
    print(my_string)
