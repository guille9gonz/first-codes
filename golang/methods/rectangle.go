package methods

import "math"

/*
 A struct is a collection of fields to store data
 Both parameters use capitalization to indicate they are exported (accessible from other packages)
*/
type Rectangle struct {
	Width  float64
	Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

type Circle struct {
	Radius float64
}

func (c Circle) Area() float64 {
	return math.Pi * c.Radius * c.Radius
}

type Triangle struct {
	Base   float64
	Height float64
}

func (t Triangle) Area() float64 {
	return (t.Base * t.Height) / 2
}

/*
Any type that has this method is considered to implement 'Shape' interface
Rectangle and Circle classes can use Area() as a method because
Area() can receive either a Rectangle, Circle or Triangle object
*/
type Shape interface {
	Area() float64
}

func Perimeter(rectangle Rectangle) float64 {
	return 2 * (rectangle.Width + rectangle.Height)
}

// This is not ncessary, as Area() is defined before for Rectangle and Circle types
func Area(rectangle Rectangle) float64 {
	return rectangle.Width * rectangle.Height
}
