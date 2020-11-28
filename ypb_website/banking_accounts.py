class BankingAccount:
    def __init__(self, acc_num, balance, transactions, acc_type):
        self.acc_num = acc_num
        self.balance = balance
        self.acc_type = acc_type
        self.transactions = transactions

    def new_transaction(self, from_acc_type, to_acc_type, value, date): return None


class ChequeingAccount(BankingAccount):
    def __init__(self, acc_num, balance, transactions, acc_type='Chequeing'):
        BankingAccount.__init__(self, acc_num, balance, transactions, acc_type)

    def deposit(self, value): self.balance += value

    def withdraw(self, value): self.balance -= value

    def check_withdrawal_value(self, value): return None


class CreditAccount(BankingAccount):
    def __init__(self, acc_num, balance, pending_balance, transactions, acc_type='Credit'):
        BankingAccount.__init__(self, acc_num, balance, transactions, acc_type)
        self.pending_balance = pending_balance

    def deposit(self, value): self.balance -= value

    def withdraw(self, value): self.balance += value

    def check_withdrawal_value(self, value): return None

    def approved_pending_balance(self, pending_value): return None


class SavingsAccount (BankingAccount):
    def __init__(self, acc_num, balance, transactions, acc_type='Savings'):
        BankingAccount.__init__(self, acc_num, balance, transactions, acc_type)

    def deposit(self, value): self.balance += value

    def withdraw(self, value): self.balance -= value

    def check_withdrawal_value(self, value): return None