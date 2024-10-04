package main

func Sum(numbers []int) int {
	sum := 0
	for _, number := range numbers {
		sum += number
	}
	return sum
}

/*
The "..." allows the function to accept a variable number of arguments
Iterates and passes each array to the Sum function and stores the result in a new array
*/
func SumAll(numbersToSum ...[]int) []int {
	var sums []int
	for _, numbers := range numbersToSum {
		sums = append(sums, Sum(numbers))
	}
	/*
		Another option is:
		lengthOfNumbers := len(numbersToSum)
		sums := make([]int, lengthOfNumbers) 'make' is used to create slices

		for i, numbers := range numbersToSum {
			sums[i] = Sum(numbers)
		}
	*/
	return sums
}

func SumAllTails(numbersToSum ...[]int) []int {
	var sums []int
	for _, numbers := range numbersToSum {
		if len(numbers) == 0 {
			sums = append(sums, 0)
		} else {
			tail := numbers[1:]
			sums = append(sums, Sum(tail))
		}
	}
	return sums
}
