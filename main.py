#bubble sorting
myList=[1,21,94,38,69]
print("The Original List is {}".format(myList))

for i in range(0,len(myList)):
    for j in range(i,len(myList)):
        if myList[i] > myList[j]:
            myList[i],myList[j]=myList[j],myList[i]

print("The sorted list contains: {}".format(myList))