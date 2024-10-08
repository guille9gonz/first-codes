package pointers

import (
	"testing"
)

func TestWallet(t *testing.T) {

	t.Run("deposit", func(t *testing.T) {
		wallet := Wallet{}
		wallet.Deposit(Bitcoin(10))

		got := wallet.Balance()
		//fmt.Printf("Address of balance in test is %p\n", &wallet.balance)
		want := Bitcoin(10) // Result has to be a Bitcoin type, not valid just 10 (int)

		if got != want {
			t.Errorf("got %s, but wanted %s", got, want)
		}
	})

	t.Run("withdraw", func(t *testing.T) {
		wallet = Wallet{balance: Bitcoin(20)}
		wallet.Withdraw(Bitcoin(10))

		got := wallet.Balance()
		want := Bitcoin(10)

		if got != want {
			t.Errorf("got %s, but wanted %s", got, want)
		}

	})

}
