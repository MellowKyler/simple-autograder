import os


testInput = input("Test Version: ")
attemptInput = input("Attempt Number: ")
keyFile = open(testInput + "-answer-key.txt")
ansFile = open(testInput + "-" + attemptInput + ".txt")
tempFile = testInput + "-" + attemptInput + "-graded.txt"


key = list()
ans = list()
rev = list()


for k in keyFile:
	key.append(k.rstrip())
for a in ansFile:
	ans.append(a.rstrip())

	
for j in ans:
	for i in key:
		if i == j:
			rev.append(j + "\n")
			break
		else:
			rev.append("~ " + j + "\n")
			break

			
writeFile = open(tempFile, "w")
for b in rev:
	writeFile.write(b)
writeFile.close()


readFile = open(tempFile, "r")
count = 0
searching = readFile.read()
count = searching.count("~")
readFile.close()


outputFile = open(tempFile, "a")
correct = len(key) - count
percent = round((correct / len(key) * 100), 2)
strPercent = str(percent)
outputFile.write("\nScore: " + str(correct) + "/" + str(len(key)) + " (" + strPercent + "%)")
print("Score: " + str(correct) + "/" + str(len(key)) + " (" + strPercent + "%)")


smolPercent = strPercent[:-3]
oldName = testInput + "-" + attemptInput + "-graded.txt"
newName = testInput + "-" + attemptInput + "-(" + smolPercent + "%).txt"
os.rename(oldName, newName)

































