class Customer:
    def __init__(self, username, password, first_name, last_name, mailing_address, banking_accts):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.mailing_address = mailing_address
        self.banking_accts = banking_accts

    def get_chequeing_account(self): return None

    def get_credit_account(self): return None

    def get_savings_account(self): return None

    def move_money(self, from_acc_num, to_acc_num, date, value):
        # deposit(value) and withdraw(value) should be called for relevant banking accounts
        return None