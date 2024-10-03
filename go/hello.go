package main // Required when building an executable

import "fmt" // Packages containing the Println function

func Hello(name string) string {
	return "Hello, " + name
}

func main() {
	fmt.Println(Hello("Guille"))
}
