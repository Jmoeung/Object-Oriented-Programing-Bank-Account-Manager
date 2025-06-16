#!/usr/bin/env python3
import os
import sys
class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        self.filename=f'{owner}_balance.txt'
        self.load_balance() #<-- main function that loads balance if file exists
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited ${amount:,.2f}, New Balance: ${self.balance:,.2f}')
        else:
            print ('Deposit amount must be positive')
    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient balance')
        elif amount <= 0:
            print('Withdrawal amount must be positive')
        else:
            self.balance -= amount
            print(f'Withdrawn ${amount:,.2f}, New Balance: ${self.balance:,.2f}')
    def get_balance(self):
        return self.balance
    def save_balance(self):
        with open(self.filename,'w') as file:
            file.write(str(self.balance))
    def load_balance(self):
        if os.path.isfile(self.filename):
            with open(self.filename,'r') as file:
                self.balance = float(file.read())
    def __str__(self):
        return f'Owner: {self.owner}, Balance: ${self.balance:,.2f}'

# --- User Interface Loop ---
owner = input('Enter owner: ')
account=Account(owner)
print(f'Welcome {owner} to Bank Account')
while True:
    print('\nOptions: deposit, withdraw, balance,exit')
    choice = input('Enter option: ')

    if choice == 'deposit':
        try:
            amount = int(input('Enter amount to deposit: $'))
            account.deposit(amount)
        except ValueError:
            print('Invalid input')
    elif choice == 'withdraw':
        try:
            amount = int(input('Enter amount to withdraw: $'))
            account.withdraw(amount)
        except ValueError:
            print('Invalid input')
    elif choice == 'balance':
        print(f'Balance is: ${account.get_balance():,.2f}')
    elif choice == 'exit':
        account.save_balance()
        print('Balance saved. Goodbye!')
        sys.exit(0)


