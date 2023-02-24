import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v,k):
    if v <= k:
      # if v <=k Chris will only write v lines of code
      return v
    sum = v # initialize sum as v
    p = 1 # p is the largest integer such that v // k ** p > 0
    while v//k**p >0:
       # calculate the sum of the series until v // k ** p becomes 0
        sum += v//k**p
        p += 1
    return sum



# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  # Iterate through the range of values from 1 to n+1.
  for v in range(1,n+1):
    if sum_series(v, k) >= n:
       # Chris will only be able to write at least n lines of code before falling asleep if sum_series >= n
      return v



# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search(n,k):
    lo = 1 # initialize the minimum lines of code to 1
    hi = n # initialize the maximum lines of code to n
    while lo < hi:
        mid = (lo + hi)//2 # Calculates the middle value
        if sum_series(mid, k) >= n:
          # the minimum allowable value of v is less than or equal to mid, so search in lower half
            hi = mid
        else:
            lo = mid + 1
            # the minimum allowable value of v is greater than mid, so search in the upper half
    return lo # return the minimum allowable value of v



def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
