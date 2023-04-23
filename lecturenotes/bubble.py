def bubbleSort(aList):
    n = len(aList)
    for scan in range(1,n):
        i = 0
        while i < n - scan:
            print(f"i = {i}", end = "\t");
            
            if aList[i+1] < aList[i]:
                aList[i],aList[i+1] = aList[i+1],aList[i]
            i += 1
            
            print(aList) # added instrumentation to print list at each iteration
        print('---') # added separator to distinguish outer loop iterations
        
l = [87,3,56,9,2,10,38]

bubbleSort(l)
print(l)

