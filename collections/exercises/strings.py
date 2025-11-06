# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.

textLen = int(len(text))
textStartSlice = text[0:12]
#print(len(textSlice))
print(textStartSlice)

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!

endTextSlice = text[(textLen-12):(textLen)]
#print(len(endTextSlice))
print(endTextSlice)

# 3. Print a slice of the middle 12 characters from 'text'.

textMidStart = int(textLen/3)
textMidEnd = int(textLen/3*2)
textMiddle = text[textMidStart:textMidEnd]
#print(len(textMiddle))
print(textMiddle)

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
loopCount = 0
for index in range(len(word)):
    wordIndex = int(len(word))
    loopCount += 1
    print(word[int(wordIndex-loopCount)])

    # NOTE: I am aware this is an inefficient way to do it, but got the idea and wanted to see if I could make it possible, and I did that

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
loopCount = 0
accumulator = ''
for index in range(len(word)):
    wordIndex = int(len(word))
    loopCount += 1
    accumulator = accumulator + word[int(wordIndex-loopCount)]
    # print(word[int(wordIndex-loopCount)])

print(accumulator)
# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
loopCount = 0
accumulator = ''
rotalumucca = ''
for index in range(len(word)):
    wordIndex = int(len(word))
    loopCount += 1
    accumulator = accumulator + word[int(wordIndex-loopCount)]
    rotalumucca = rotalumucca + word[index]
    # print(word[int(wordIndex-loopCount)])

print(rotalumucca, '|', accumulator)