import matplotlib.pyplot as plt                           # importing the matplotlib function
f = open("D:\PyCharm Edu 2018.2\pg49327.txt","r")         #function to open and read the file and the name of the function must include the location of the file


dictionary = {}                                           #This is variable for the dictionary

textbook = f.read()                                       #I decided to name my text file as variable, "Textbook" and here I ask the python to read it.
textbook = textbook.split()                               #Here I ask the python to make the textbook as an object and to split all the words.

for words in textbook:                                    #For the words in the textfile, I want to the make all the words lowercase by using the method ".lower()"
    words = words.lower()
    if words not in dictionary:                           #If the word is not yet in the dictionary so the new word will be inserted into the dictionary and that means the value of the word is 1
        dictionary[words] = 1
    if words in dictionary:                               #If the word is already in the dictionary so inserted into the dictionary and the value of that certain word in the dictionary will
        dictionary[words]+= 1                               #will be added by 1
for word, count in dictionary.items():                    #This inputs together the key and value in the dictionary by using the method .Items()
    print(word, "=", count)                                #print the word, count


top_10 = sorted(dictionary.items(), key=lambda textbook: textbook[1])                   #variable top_10 that sort the items in the dictionary with lambda fuction

count = []                                                                              #array for count
word = []                                                                               #array for word


for c in range (0,10):                                                                  #for looping with the condition of c in range (0,10)
    ct = (top_10[-1-c])[-1]
    count.append(ct)

for w in range (0, 10):                                                                 #for looping with the condition of w in range (0,10)
    wd = (top_10[-1-w])[0]
    word.append(wd)

print(word, "=", count)                                                                 #print the word = count



plt.title("10 most common words", fontsize = 24)                                        # Title in the graph
plt.xlabel("words", fontsize = 12)                                                      # Words category in the graph
plt.ylabel("count", fontsize = 12)                                                      # Count category in the graph

plt.plot(word, count, "o")                                                              # plotting the points in the graph
plt.show()                                                                              # showing it in the graph

f.close()                                                                               # closing the file





'''
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()
'''

