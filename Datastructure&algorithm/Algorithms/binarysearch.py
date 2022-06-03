
def linear_search(numbers_list,finding_number):
	for index, elements in enumerate(numbers_list):
		if elements == finding_number:
			return index
	else:
		return None

		
def binary_search(numbers_list,finding_number):
	left_index = 0
	right_index = len(numbers_list)-1
	mid_index = 0
	while left_index <= right_index:
		mid_index = (left_index + right_index) //2
		mid_number = numbers_list[mid_index]

		if mid_number == finding_number:
			return mid_number
		if mid_number < finding_number:
			left_index = mid_index +1
		else:
			right_index = mid_index - 1
	return -1

def binary_search_recursive(numbers_list,finding_number,left_index,right_index):
	if right_index < left_index:
		return -1

	mid_index = (left_index+right_index)//2
	mid_number = numbers_list[mid_index]
	if mid_number < finding_number:
		left_index = mid_index +1
		return binary_search_recursive(numbers_list,finding_number,left_index,right_index)
	else:
		right_index = mid_index - 1
		return binary_search_recursive(numbers_list,finding_number,left_index,right_index)
def main():
	#numbers_list = [12,15,17,19,21,24,45,67]
	finding_number = 1
	numbers_list = [x for x in range(2,10000001)]

	index = linear_search(numbers_list,finding_number)
	index1 = binary_search(numbers_list,finding_number)
	print(index1)
main()