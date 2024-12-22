class BankAccount:
    
    def __init__(self, account_number, balance):
        self.__account_number = account_number  
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdraw amount.")

    def display_account_info(self):
        print(f"Account Number: {self.get_account_number()}, Current Balance: {self.get_balance()}")

    def __display_balance(self):
        print(f"Current Balance: {self.__balance}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        self.__display_balance() 
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Error: Balance cannot be negative.")

account = BankAccount("11", 100.0)

account.deposit(500.0)

account.withdraw(200.0)

account.set_balance(10000.0)

account.display_account_info()