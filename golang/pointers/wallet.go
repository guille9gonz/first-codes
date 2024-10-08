package pointers

import "fmt"

type Bitcoin int // Create a new data type from a existing one

type Stringer interface {
	String() string // String() is used to print passed values to any format that accepts strings
}

func (b Bitcoin) String() string {
	return fmt.Sprintf("%d BTC", b) // Sprint() is used to store the string/sentence in a variable
}

type Wallet struct {
	balance Bitcoin
}

// Add a pointer '*' to match main with test (means "a pointer to a wallet")
func (w *Wallet) Deposit(amount Bitcoin) {
	//fmt.Printf("Address of balance in Deposit is %p \n", &w.balance) Look where the balance is stored in memory
	w.balance += amount
}

func (w *Wallet) Balance() Bitcoin {
	return w.balance
}
