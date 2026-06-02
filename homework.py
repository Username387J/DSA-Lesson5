list=[1,100,34,91,50,28,287,30]
print("List before: {}".format(list))

for i in range(0,len(list)):
    for l in range(i,len(list)):
        if list[i] < list[l]:
            list[i],list[l]=list[l],list[i]

print("List after: {}".format(list))