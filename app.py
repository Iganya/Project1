class Bank:
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no

    # reprint the user name and aoount details on the console.
    def __str__(self):
        return f"The account name is {self.name} and the account no is {self.acc_no}"

    def opening_balance(self, balance):
        self.balance = balance
        print(f"Your balance is: {balance}")

    # function for depositing money to the users account
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"You have deposited: {amount}")
        print(f"The current balance is : {self.balance}")

     #for withdrawing money from the account.
    def withdrawal(self, with_amount):
        if with_amount <= self.balance:
            self.balance -= with_amount
            print(f"Withdrawal Accepted! \nYour balance is now {self.balance}")
        else:
            print("withdrawal Denied. Insufficient fund.")


while True:
    bank = Bank(input("kindly input your name: "),
                int(input("Kindly input your account number: ")))
    print(bank)
    bank.opening_balance(int(input("What is your opening balance: ")))
    bank.deposit(int(input("deposit amount: ")))
    bank.withdrawal(int(input("Amount to withdraw: ")))

    break