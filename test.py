# An iterative implementation of Binary Search
def binarySearch( theValues, target ):
 # Start with the entire sequence of elements
    low = 0
    high = len( theValues ) - 1
 # Repeatedly subdivide the sequence in half
 # until the target is found
    while low <= high:
 # Find the midpoint of the sequence
        mid = (high + low) // 2
 # Does the midpoint contain the target?
 # If yes, return midpoint (i.e. index of the list)
        if theValues[mid] == target:
            return mid
            
 # Or is the target before the midpoint?
        elif target < theValues[mid]:
             high = mid - 1
 # Or is the target after the midpoint?
        else:
            low = mid + 1
 # If the sequence cannot be subdivided further,
 # target is not in the list of values
        print(mid)
    return -1

binarySearch([1,2,3,4,5,6,7,8], 5)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def good(n):
    if n <= 1:
        
        return (n,0)
    else:
        
        (a, b) = good(n-1)
        print(b)
        return (a+b, a)
    
print(good(8))

listx= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list=[]
for i in listx:
    if i%2 == 0:
        list.append(i)
for i in listx:
    if i%2 != 0:
        list.append(i)
print(list)