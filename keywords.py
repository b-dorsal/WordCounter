# Open a text file and print the top n used words in the file.
__author__ = "Brian Dorsey"
__email__ = "bdor528@gmail.com"
# To-do: this is to be used as a module for a bigger project. 
# No user input is required yet.

# Open the file and read the text into a string.
file = open("/Users/admin/Desktop/text.txt", "r")
rawtext = file.read() 


# Omitted words that are often used in large quantities in text.
illegalwords = ["the", "an", "a", "in", "on", 
				"and", "then", "than", "at", 
				"to", "of", "is", "that", 
				"can", "were", "how", "was", 
				"this", "or", "their", "with", 
				"also", "be", "by", "all", 
				"very", "any", "are", 
				"because", "some", "but", 
				"them", "may", "it"]


# Load the words from the text and increment their quantities.
words = {}
s = ""
for w in rawtext:
	if w == ' ':
		s = s.lstrip()
		s = s.lower()
		if s not in words:
			words[s] = 1
		else:
			words[s] = words[s] + 1
		s = ""
	else:
		s += w


# Get the top n used words.
count = 20	#top n words
biggestlist = []
for n in range(count):
	
	biggest = 0
	most = ""
	for s in words:
		# print s + ", " + str(words[s])
		if words[s] > biggest and s not in illegalwords and s not in biggestlist:
			biggest = words[s]
			most = s
	biggestlist.append(most)


#print the top n used words.
for w in biggestlist:
	print w


