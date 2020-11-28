class Transaction:
    def __init__(self, transaction_num, detail, date, amount, transaction_type, is_pending):
        self.transaction_num = transaction_num
        self.detail = detail
        self.date = date
        self.amount = amount
        self.transaction_type = transaction_type # 'W' for Withdrawal or 'D' for Deposit
        self.is_pending = is_pending # True or False. Always False for a Chequeing or Savings account

    def approve_transaction(self): self.is_pending = False
