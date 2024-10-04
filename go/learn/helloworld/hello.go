package main // Required when building an executable

import "fmt" // Packages containing the Println function

/*
Constants are initialized with "="
Variables are initialized with ":="
*/
const spanish = "Spanish"
const french = "French"
const englishHelloPrefix = "Hello, "
const spanishHelloPrefix = "Hola, "
const frenchHelloPrefix = "Bonjour, "

func Hello(name string, language string) string {
	if name == "" {
		name = "World"
	}

	return greetingPrefix(language) + name
}

// language is the argument and prefix the return value
func greetingPrefix(language string) (prefix string) {
	switch language {
	case spanish:
		prefix = spanishHelloPrefix
	case french:
		prefix = frenchHelloPrefix
	default:
		prefix = englishHelloPrefix
	}
	return // No need to specify prefix here
}

func main() {
	fmt.Println(Hello("Guille", "French"))
}
