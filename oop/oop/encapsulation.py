class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance


# Example usage
if __name__ == "__main__":
    account = BankAccount(1000)
    account.deposit(500)
    print("Current Balance:", account.get_balance())
