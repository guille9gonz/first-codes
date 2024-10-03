package main

/*
Package for testing, contains *testing.T
needs a file with name "xxx_test.go"
*/
import "testing"

/*
Must start with "Test"
Only takes one argument (t * testing.T)
"t" is an instance of *testing.T
*/
func TestHello(t *testing.T) {
	got := Hello("Guille")
	want := "Hello, Guille"

	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}
