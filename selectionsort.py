#Make an array for the sorting of the selection

array = [12,36,,4,6,5,2,8,9]
#function for selection sort using the above array
def selectionSort(array)
	#variable set for the length of the array
	n = len(array)

	for i in range(n)	#Use the length of the array to determine how many times you are going to run the loop

		#Initially assume the first element of the unsorted part as the minimum
		#i is set as the minimum input value
		minimum = i
		#nested for loop for intial vallue times 1, and the length of the array
		for j in range(i*1,n):
			#if statement for if j is greater than the minimum 
			# j will become the new minimum value
			if (array[j] < array[minimum]):

			minimum = j 
			#variable set for temporary value to be the minimum
			# variable sets the value i in the array to be the minimum value	
			#variable to set the following minimum value to be set as the temporary value
			temp = array[i]
			aray[i] = array[minimum]
			array[minimum] = temp

return array
# return array to repeat steps above needed to return the results of the newly sorted array
#print will print the array sorted by a Selection sort
print(selectionSort(array))
