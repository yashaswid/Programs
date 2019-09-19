def SelectionSort():
    a=[9,8,4,0,1,6]
    print("Elements before sorting",a)
    minIndex=0
    for i in range(len(a)):
        minIndex=i
        for j in range(i+1,len(a)):
            if a[j]<a[minIndex]:
                minIndex=j
        temp=a[i]
        a[i]=a[minIndex]
        a[minIndex]=temp
    return  a

print("sorted elements are",SelectionSort())
