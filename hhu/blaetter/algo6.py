def Msort(A, l, r):
    b = True
    while (b):
        b = False
        ll = l
        while (ll < r):
            mm = ll+1
            while ((mm <= r) and (A[mm-1] <= A[mm])):
                mm+=1
            rr = mm+1
            while ((rr <= r ) and (A[rr-1] <= A[rr])):
                rr+=1
            rr-=1
            if (mm <= r):
                Merge (A, ll, mm, rr)
                b = True
            ll = rr+1
def Merge (A, l, m, r):
    print(A)
    B = {}
    i = l
    j = m
    for k in range(l, r+1):
        if (i >= m or (j <= r and A[i] > A[j])):
            B[k] = A[j]
            j += 1
        else:
            B[k] = A[i]
            i += 1
    for k in range(l, r+1):
        A[k] = B[k]
    print(A)
    print()


array = [5065, 7628, 6977, 5585, 4854, 113, 5224, 3642, 7008, 4609, 9892, 6739, 4253, 1817, 3790, 286]

def list_to_buckets(array, base, iteration):
    buckets = [[] for x in range(base)]
    for number in array:
        # Isolate the base-digit from the number
        digit = (number // (base ** iteration)) % base
        # Drop the number into the correct bucket
        buckets[digit].append(number)
    return buckets

def buckets_to_list(buckets):
    numbers = []
    for bucket in buckets:
        # append the numbers in a bucket
        # sequentially to the returned array
        for number in bucket:
            numbers.append(number)
    return numbers

maxval = max(array)

it = 1
# Iterate, sorting the array by each base-digit
while 10 ** it <= maxval:
    print(list_to_buckets(array, 10, it))
    array = buckets_to_list(list_to_buckets(array, 10, it))
    print(array)
    it += 1