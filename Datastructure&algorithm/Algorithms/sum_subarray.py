import time

def find_max_crossing_subarray(ar,low,mid,high):
  sum = 0
  left_sum = -10000
  for i in range(mid,low-1,-1):
    sum += ar[i]
    if sum > left_sum:
      left_sum = sum
  right_sum = -10000
  sum = 0
  for j in range(mid+1,high+1):
    sum += ar[j]
    if sum >  right_sum:
      right_sum = sum
  return left_sum+right_sum

def find_max_subarray(ar,low,high):
  if low == high:
    return ar[low]
  mid = (low+high)//2
  left = find_max_subarray(ar,low,mid)
  right = find_max_subarray(ar,mid+1,high)
  cross = find_max_crossing_subarray(ar,low,mid,high)
  if left >= right >= cross:
    return left
  elif right >= left >= cross:
    return right
  else:
    return cross

def max_subarray_kadane(ar):
  max_so_far = -1000000
  max = 0
  for i in range(len(ar)):
    max += ar[i]
    if max > max_so_far:
      max_so_far = max
    if max < 0:
      max = 0
  return max_so_far

if __name__ == "__main__":
  ar = [-2,-3,-4,-5,-7]
  st = time.time()
  # max = find_max_subarray(ar,0,len(ar)-1)
  max = max_subarray_kadane(ar)
  et = time.time()
  print(max)
  print (et-st)
  st = time.time()
  max = find_max_subarray(ar,0,len(ar)-1)
  # max = max_subarray_kadane(ar)
  et = time.time()
  print(max)
  print (et-st)