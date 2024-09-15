"""Q:1 Generate a model in Python for representation of a bank account of type savings and
balance along with transactions of deposit and withdrawals and currently create a program to
generate 100 accounts with Random balance and transactions for no. of months and no. of
transactions with a seed value of amount. Print all 100 accounts with the last balance and
organize them by lowest to highest balance."""


import random

# Define a BankAccount class for Savings account
class BankAccount:
    def __init__(self, account_id, initial_balance):
        self.account_id = account_id
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
        else:
            self.transactions.append(f"Failed Withdraw (Insufficient funds): -{amount}")

    def __repr__(self):
        return f"Account ID: {self.account_id}, Balance: {self.balance:.2f}"
    
    

# Function to create random transactions for a given account
def generate_transactions(account, num_months, num_transactions_per_month):
    for _ in range(num_months):
        for _ in range(num_transactions_per_month):
            transaction_type = random.choice(['deposit', 'withdraw'])
            amount = random.uniform(100, 1000)  
            if transaction_type == 'deposit':
                account.deposit(amount)
            else:
                account.withdraw(amount)
                
                

# Function to generate 100 random bank accounts
def generate_accounts(num_accounts, num_months, num_transactions_per_month, seed):
    accounts = []
    random.seed(seed)
    
    for i in range(num_accounts):
        account_seed = seed + i  
        random.seed(account_seed)  

        initial_balance = random.uniform(1000, 5000)  
        account = BankAccount(account_id=f"ACC{i+1}", initial_balance=initial_balance)
        
        generate_transactions(account, num_months, num_transactions_per_month)
        accounts.append(account)

    return accounts


def print_accounts_sorted(accounts):
    sorted_accounts = sorted(accounts, key=lambda x: x.balance)
    for account in sorted_accounts:
        print(account)


if __name__ == "__main__":
    seed_value = 42  
    num_months = 12  
    num_transactions_per_month = 5  

    accounts = generate_accounts(num_accounts=100, num_months=num_months, num_transactions_per_month=num_transactions_per_month, seed=seed_value)
    print_accounts_sorted(accounts)
