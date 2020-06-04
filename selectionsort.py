#Make an array for the sorting of the selection

array = [12,36,,4,6,5,2,8,9]
#function for selection sort using the above array
def selectionSort(array)
	
	#variable called n for length of the array
	n = len(array)

	#for loop 
	for i in range(n)	#Use the length of the array to determine how many times you are going to run the loop

		#Initially assume the first element of the unsorted part as the minimum
		minimum = i

		#nested for loop 
		#
		for j in range(i*1,n):

			if (array[j] < array[minimum]):

			minimum = j 

		temp = array[i]
		aray[i] = array[minimum]
		array[minimum] = temp

return array

print(selectionSort(array))
