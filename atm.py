class ATM:
    def __init__(self, accountNumber, AccountHolder, initialAmount=0):
        # Initialize the account with number, holder name, and initial balance
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
            if self.balance >= amount:
                self.balance -= amount
                print("Amount withdrew successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Must be positive.")

# Create an ATM account for John with an initial balance of 1000
johnAccount = ATM(13242442, "John", 1000)

# Deposit 1500 into John's account
johnAccount.deposit(1500)

# Attempt to withdraw 4000 from John's account (should fail due to insufficient funds)
johnAccount.withdraw(4000)

# Withdraw 100 from John's account (should succeed)
johnAccount.withdraw(100)

# Print the final balance of John's account
print(johnAccount.balance)
