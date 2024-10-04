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
	t.Run("saying hello to people", func(t *testing.T) {
		got := Hello("Guille", "")
		want := "Hello, Guille"
		assertCorrectMessage(t, got, want) // Refactor using a function

	})

	t.Run("say 'Hello, World' when an empty string is supplied", func(t *testing.T) {
		got := Hello("", "")
		want := "Hello, World"
		assertCorrectMessage(t, got, want)
	})

	t.Run("in Spanish", func(t *testing.T) {
		got := Hello("Jusep", "Spanish")
		want := "Hola, Jusep"
		assertCorrectMessage(t, got, want)
	})

	t.Run("in French", func(t *testing.T) {
		got := Hello("Piere", "French")
		want := "Bonjour, Piere"
		assertCorrectMessage(t, got, want)
	})
}

/*
testing.B is for benchmarking tests (measure performance of code)
testing.TB allows func to be used both in tests and benchmarks
t.Helper is used to tell the test suit this method is a helper
*/
func assertCorrectMessage(t testing.TB, got, want string) {
	t.Helper()
	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}
