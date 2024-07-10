class ATM:
    def __init__(self, accountNumber, AccountHolder, initialAmount=0):
        self.accountNumber = accountNumber
        self.accountHolder = AccountHolder
        self.balance = initialAmount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited amount successfully.")
        else:
            print("Must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance > amount:
                self.balance -= amount
                print("Amount withdrew successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Must be positive.")

johnAccount = ATM(13242442, "John", 1000)

johnAccount.deposit(1500)

johnAccount.withdraw(4000)

johnAccount.withdraw(100)

print(johnAccount.balance)