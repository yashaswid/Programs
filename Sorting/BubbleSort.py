class Sorting():
    def bubbleSort(self,a):
        print(a)
        for i in range(0,len(a)-2):
            for j in range(i+1,len(a)-1):
                if a[j]<a[i]:
                    temp=a[i]
                    a[i]=a[j]
                    a[j]=temp
        return (a)


d=Sorting()
a = [1, 9, 5, 3, 0]
print("Before Sorting")
print(a)
print("After Sorting")
print(d.bubbleSort(a))






