proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
protoProtoList = [proto_list1, proto_list2, proto_list3, proto_list4]
#print(protoProtoList)
listCount = 0
for comma in protoProtoList:
    listCount += 1
    if ',' in comma:
        print("The characters are separated by commas in proto_list" + str(listCount))

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

arrayString1 = proto_list1.split(',')
#print(arrayString)

arrayString1.reverse()
#print(arrayString1)

nuArrayString1 = ",".join(arrayString1)
print(nuArrayString1)

arrayString4 = proto_list4.split(',')
#print(arrayString)

arrayString4.reverse()
#print(arrayString1)

nuArrayString4 = ",".join(arrayString4)
print(nuArrayString4)


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.

arraystring2 = proto_list2.split(';')
arraystring2.sort()
nuArrayString2 = ",".join(arraystring2)
print(nuArrayString2)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

arraystring3 = proto_list3.split(' ')
arraystring3.sort()
arraystring3.reverse()
nuArrayString3 = " ".join(arraystring3)
print(nuArrayString3)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
arrayString4 = proto_list4.split(',')
arrayString4.reverse()
nuArrayString4 = ",".join(arrayString4)

print(nuArrayString4.replace(" ",""))