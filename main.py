# Program to count the number of words in a text file

# open and read the file content as a string, and save it to variable file content
inputFile = open("input.txt", "r").read()
inputFile = inputFile.replace("\n", " ").replace("\t", " ")

# split the file content string by white spaces to get an array of words, save it to variable words
wordsList = inputFile.split()
# declare a dictionary wordDict
wordDictionary = dict()
# for each word in words array, check the keys of the dictionary. if found, increment the value of the particular key.
# if not found, create a key for this word and keep it's value as 1
for currentWord in wordsList:
    if currentWord in wordDictionary:
        wordDictionary[currentWord] += 1
    else:
        wordDictionary[currentWord] = 1
# print wordDictionary to see the results
print(wordDictionary)

# Name : Wafaa El Bouchikhi
# Student No. : WE117460
# Date : 07-12-2021