def InsertionSort():
    a=[19,8,4,0,91,26,1,100,35]
    print("Elements before sorting",a)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            k=i
            yash=j
            while(k>=0 and a[k]>a[yash] ):
                temp=a[k]
                a[k]=a[yash]
                a[yash]=temp
                k-=1
                yash-=1
    return a






print("sorted elements are",InsertionSort())