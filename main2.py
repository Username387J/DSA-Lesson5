#insertion sorting

a=[34,5,1,26,68]
print("Array before sorting: {}".format(a))

def insertionSort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i-1
        while j>=0 and temp<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp

insertionSort(a)

print("Array after sorting: {}".format(a))