def insertion_sort():
	ar = [3,41,2,42,34,32,1,50,21]
	for i in range(1,len(ar)):
		key = ar[i]
		j = i -1
		while j >= 0 and ar[j]>key:
			ar[j+1] = ar[j]
			j = j -1
		ar[j+1] = key
	return ar
def swap(a,b,ar):
	if a != b:
		tmp = ar[a]	
		ar[a] = ar[b]
		ar[b] = tmp
def partition(elements,start,end):
	pivot_index = start
	pivot = elements[pivot_index]

	while start < end:
		while start < len(elements) and elements[start] <= pivot:
			start += 1
		while elements[end] > pivot:
			end -= 1

		if start < end:
			swap(start,end, elements)

	swap(pivot_index,end,elements)

	return end
def quick_sort(elements,start,end):
	if start < end:
		pi = partition(elements,start,end)
		quick_sort(elements,start,pi-1) # left partition
		quick_sort(elements,pi+1,end)  #right partition

def merge_sort(ar):
	if len(ar) <= 1:
		return 
	mid = len(ar)//2
	left = ar[:mid]
	right = ar[mid:]
	merge_sort(left)
	merge_sort(right)
	merge_two_sorted_arrays(left,right,ar)


def merge_two_sorted_arrays(a,b,ar):
	i = j = k =0
	len_a = len(a)
	len_b = len(b)
	while i < len_a and j < len_b:
		if a[i] <= b[j]:
			ar[k] = a[i]
			i += 1
		else:
			ar[k] = b[j]
			j += 1
		k+=1

	while i < len_a:
		ar[k] = a[i]
		i+=1
		k+=1
	while j < len_b:
		ar[k] = b[j]
		j+=1
		k+=1

	

def main():
	print(insertion_sort())
	elements = [21,12,9,7,20,12,2,5,28]
	quick_sort(elements,0,len(elements)-1)
	merge_sort(elements)
	print(elements)
main()