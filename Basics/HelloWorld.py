sentence = "A long time ago in a galaxy far far away"
words = sentence.split()

wordsLengths = [len(word) for word in words if word != "far"]
print(wordsLengths)