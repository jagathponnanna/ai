numbers=[23,56,48,941,481,616,156,8,684,16,661,416,48484,16514,161,4,151,16,4,151,161,48,68,1684,88]

numbers.sort()
print(numbers)

def binary_search(numbers, key):
    n=len(numbers)
    m=0
    while(m<=n):
        mid=(m+n)//2
        if numbers[mid]==key:
            return mid
        elif key>numbers[mid]:
            m=mid+1
        elif key<numbers[mid]:
            n=mid-1
    return -1

if __name__=="__main__":
    print(binary_search(numbers,16))