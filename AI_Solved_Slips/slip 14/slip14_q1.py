# input string
inputString = "This is KKW college, nashik"
print("Input String =",inputString)
# splitting the input string into a list of words
wordsList = inputString.split(" ")
# traversing through each word in the words list till the length of the words list
for w in range(len(wordsList)):
   # converting all the words into lowercase using the lower() function
   wordsList[w]=wordsList[w].lower()
# traversing through each word from the end in the words list
# Applying bubble sort to sort the words
for n in range(len(wordsList)-1, 0, -1):
   for i in range(n):
      if wordsList[i] > wordsList[i + 1]:
         # swapping data if the element is less than the next element in the array
         wordsList[i], wordsList[i + 1] = wordsList[i + 1], wordsList[i]
# printing the list of sorted Words in alphabetic Order
print("Sorted Words Alphabetically =",wordsList)
