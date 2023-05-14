file = open("System Security Project.txt", "r")
count = 0
for line in file:
    words = line.split(" ")
    count += len(words)
file.close()    
print(count)