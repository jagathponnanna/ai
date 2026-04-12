# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.
# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

def total_hours(speed,piles):
    hours=0
    for b in piles:
        if speed>b:
            hours=hours+1
        else:
            temp=b
            while(temp>0):
                hours=hours+1
                temp=temp-speed
    return hours
def eat_speed(h,piles):
    speeds=[x for x in range(1,max(piles))]
    print(speeds)
    m=0
    n=max(piles)
    result = n
    while(m<=n):
        mid=(m+n)//2
        tspeed=total_hours(speeds[mid],piles)
        if tspeed <= h:
            result= speeds[mid]
            n=mid-1
        elif tspeed> h:
            m=mid+1
    return result

print(eat_speed(8,[3,6,7,11]))
