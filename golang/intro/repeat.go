package main

func Repeat(character string, repeatCount int) string {
	var repeated string // Explicit declaration, initializes to "" (empty string), := is only used inside functions
	for i := 0; i < repeatCount; i++ {
		repeated += character
	}
	return repeated
}
