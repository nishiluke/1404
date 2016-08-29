"""
the quick brown fox jumped over the lazy dog
"""

inputText = str(input("Text: "))
inputDict = {}
for word in inputText.split():
    if word not in inputDict:
        inputDict[word] = 1
    else:
        inputDict[word] += 1

for item in inputDict:
    print("{:{}} : {}".format(item, len(max(inputDict, key=len)), inputDict[item]))

