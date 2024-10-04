package main

import "testing"

func TestSum(t *testing.T) {
	numbers := [5]int{1, 2, 3, 4, 5} // Arrays can be initialized [N] or [...] (no specifying size)

	got := Sum(numbers)
	want := 15

	if got != want {
		t.Errorf("got %d but wanted %d after giving %v", got, want, numbers)
	}
}
