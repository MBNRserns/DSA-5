#Bubble Sort in decending order
numbs=[1,7,4,3,10,5]
print("Before swapping :", numbs)
for i in range(0, len(numbs)):
    for j in range(i, len(numbs)):
        if numbs[i]<numbs[j]:
            numbs[i],numbs[j]=numbs[j],numbs[i]

print("After swapping :", numbs)