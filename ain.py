def OddOccuring(arr):
    r = 0
    for e in arr:
        r = r^e
        return r

arr = []
n = int(input("Enter array size: "))
while(n):
    num = int(input("Enter a number: "))
    arr.append(num)
    n-=1
print("OddOccuring number is",OddOccuring(arr))