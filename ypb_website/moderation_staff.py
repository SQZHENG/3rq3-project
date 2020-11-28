class ModerationStaff():
    def __init__(self, staff_id, first_name, last_name, department, customers, transactions):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.customers = customers
        self.transactions = transactions

    def approve_transaction(self, username, transaction_num):
        # approve_transaction() should be called for the related transaction
        # approved_pending_balance(pending_value) should be called for the related Credit account
        return None


