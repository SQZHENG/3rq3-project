# Requirement 3.3.1
"""The following code stimulates the process of retrieving information from a database when a user logs in."""


def retrieve_customer_info():
    from ypb_website.customer import Customer
    from ypb_website.banking_accounts import ChequeingAccount, CreditAccount, SavingsAccount
    chequeing = ChequeingAccount(220202, 0, ["""list of transactions"""])
    credit = CreditAccount(330330, 0, 0, ["""list of transactions"""])
    savings = SavingsAccount(450054, 0, ["""list of transactions"""])

    customer = Customer('zhengs46', '#@F$!s', 'Siqi', 'Zheng', '1280 Main St W, Hamilton, ON L8S 4L8',
                        [chequeing, credit, savings])
    return customer


# Requirements 3.5.1.1, 3.5.1.2
def test_create_new_transaction_from_chequeing_to_credit():
    customer = retrieve_customer_info()
    chequeing = customer.get_chequeing_account()
    chequeing_new_transaction = chequeing.new_transaction('Chequeing', 'Credit', '27/11/2020',
                                                          200) if chequeing is not None else None

    assert chequeing_new_transaction is not None, 'a new transaction for the Chequeing account should be created'
    assert chequeing_new_transaction is not None and chequeing_new_transaction.transaction_type == 'W', 'the new chequeing transaction should have a Transaction Type of Withdrawal.'
    assert chequeing_new_transaction is not None and chequeing_new_transaction.is_pending == False, 'the new chequeing transaction should not be pending.'

    credit = customer.get_credit_account()
    credit_new_transaction = credit.new_transaction('Chequeing', 'Credit', '27/11/2020',
                                                    200) if credit is not None else None

    assert credit_new_transaction is not None, 'a new transaction for the Credit account should be created'
    assert credit_new_transaction is not None and credit_new_transaction.transaction_type == 'D', 'the new credit transaction should have a Transaction Type of Deposit.'
    assert credit_new_transaction is not None and credit_new_transaction.is_pending == False, 'the new credit transaction should not be pending.'


# Requirements 3.5.1.1, 3.5.1.2
def test_create_new_transaction_from_chequeing_to_savings():
    customer = retrieve_customer_info()
    chequeing = customer.get_chequeing_account()
    chequeing_new_transaction = chequeing.new_transaction('Chequeing', 'Savings', '27/11/2020',
                                                          300) if chequeing is not None else None

    assert chequeing_new_transaction is not None, 'a new transaction for the Chequeing account should be created'
    assert chequeing_new_transaction is not None and chequeing_new_transaction.transaction_type == 'W', 'the new chequeing transaction should have a Transaction Type of Withdrawal.'
    assert chequeing_new_transaction is not None and chequeing_new_transaction.is_pending == False, 'the new chequeing transaction should not be pending.'

    savings = customer.get_savings_account()
    savings_new_transaction = savings.new_transaction('Chequeing', 'Savings', '27/11/2020',
                                                      300) if savings is not None else None

    assert savings_new_transaction is not None, 'a new transaction for the Credit account should be created'
    assert savings_new_transaction is not None and savings_new_transaction.transaction_type == 'D', 'the new savings transaction should have a Transaction Type of Deposit.'
    assert savings_new_transaction is not None and savings_new_transaction.is_pending == False, 'the new savings transaction should not be pending.'


# Requirements 3.5.1.1, 3.5.1.2
def test_create_new_transaction_from_credit_to_chequeing():
    customer = retrieve_customer_info()
    credit = customer.get_credit_account()
    credit_new_transaction = credit.new_transaction('Credit', 'Savings', '27/11/2020',
                                                    700) if credit is not None else None

    assert credit_new_transaction is not None, 'a new transaction for the Credit account should be created'
    assert credit_new_transaction is not None and credit_new_transaction.transaction_type == 'W', 'the new credit transaction should have a Transaction Type of Withdrawal.'
    assert credit_new_transaction is not None and credit_new_transaction.is_pending == True, 'the new credit transaction should be pending.'

    chequeing = customer.get_chequeing_account()
    chequeing_new_transaction = chequeing.new_transaction('Savings', 'Chequeing', '27/11/2020',
                                                          500) if chequeing is not None else None

    assert chequeing_new_transaction is not None, 'a new transaction for the Chequeing account should be created'
    assert chequeing_new_transaction is not None and chequeing_new_transaction.transaction_type == 'D', 'the new chequeing transaction should have a Transaction Type of Deposit.'
    assert chequeing_new_transaction is not None and chequeing_new_transaction.is_pending == False, 'the new chequeing transaction should not be pending.'


# Requirements 3.5.1.1, 3.5.1.2
def test_create_new_transaction_from_credit_to_savings():
    customer = retrieve_customer_info()
    credit = customer.get_credit_account()
    credit_new_transaction = credit.new_transaction('Credit', 'Savings', '27/11/2020',
                                                    700) if credit is not None else None

    assert credit_new_transaction is not None, 'a new transaction for the Credit account should be created'
    assert credit_new_transaction is not None and credit_new_transaction.transaction_type == 'W', 'the new credit transaction should have a Transaction Type of Withdrawal.'
    assert credit_new_transaction is not None and credit_new_transaction.is_pending == True, 'the new credit transaction should be pending.'

    savings = customer.get_savings_account()
    savings_new_transaction = savings.new_transaction('Credit', 'Savings', '27/11/2020',
                                                      700) if savings is not None else None

    assert savings_new_transaction is not None, 'a new transaction for the Savings account should be created'
    assert savings_new_transaction is not None and savings_new_transaction.transaction_type == 'D', 'the new savings transaction should have a Transaction Type of Deposit.'
    assert savings_new_transaction is not None and savings_new_transaction.is_pending == False, 'the new savings transaction should not be pending.'


# Requirements 3.5.1.1, 3.5.1.2
def test_create_new_transaction_from_savings_to_chequeing():
    customer = retrieve_customer_info()
    savings = customer.get_savings_account()
    savings_new_transaction = savings.new_transaction('Savings', 'Chequeing', '27/11/2020',
                                                      500) if savings is not None else None

    assert savings_new_transaction is not None, 'a new transaction for the Savings account should be created'
    assert savings_new_transaction is not None and savings_new_transaction.transaction_type == 'W', 'the new savings transaction should have a Transaction Type of Withdrawal.'
    assert savings_new_transaction is not None and savings_new_transaction.is_pending == False, 'the new savings transaction should not be pending.'

    chequeing = customer.get_chequeing_account()
    chequeing_new_transaction = chequeing.new_transaction('Savings', 'Chequeing', '27/11/2020',
                                                          500) if chequeing is not None else None

    assert chequeing_new_transaction is not None, 'a new transaction for the Chequeing account should be created'
    assert chequeing_new_transaction is not None and chequeing_new_transaction.transaction_type == 'D', 'the new savings transaction should have a Transaction Type of Deposit.'
    assert chequeing_new_transaction is not None and chequeing_new_transaction.is_pending == False, 'the new savings transaction should not be pending.'


# Requirements 3.5.1.1, 3.5.1.2
def test_create_new_transaction_from_savings_to_credit():
    customer = retrieve_customer_info()
    savings = customer.get_savings_account()
    savings_new_transaction = savings.new_transaction('Savings', 'Credit', '27/11/2020',
                                                      250) if savings is not None else None

    assert savings_new_transaction is not None, 'a new transaction for the Savings account should be created'
    assert savings_new_transaction is not None and savings_new_transaction.transaction_type == 'W', 'the new savings transaction should have a Transaction Type of Withdrawal.'
    assert savings_new_transaction is not None and savings_new_transaction.is_pending == False, 'the new savings transaction should not be pending.'

    credit = customer.get_credit_account()
    credit_new_transaction = credit.new_transaction('Savings', 'Credit', '27/11/2020',
                                                    250) if credit is not None else None

    assert credit_new_transaction is not None, 'a new transaction for the Credit account should be created'
    assert credit_new_transaction is not None and credit_new_transaction.transaction_type == 'D', 'the new credit transaction should have a Transaction Type of Deposit.'
    assert credit_new_transaction is not None and credit_new_transaction.is_pending == False, 'the new credit transaction should not be pending.'


# Requirements 3.1, 3.4.3, 3.4.5
def test_check_withdrawal_from_chequeing():
    values = [-200, 200, 100000]
    customer = retrieve_customer_info()
    chequeing = customer.get_chequeing_account()
    for i in values:
        assert chequeing is not None and chequeing.check_withdrawal_value(
            i) == False, f'${i} should not be allowed to be withdrew from the Chequeing account'


# Requirements 3.1, 3.4.3, 3.4.5
def test_check_withdrawal_from_credit():
    values = [-200, 200, 100000]
    customer = retrieve_customer_info()
    credit = customer.get_credit_account()
    for i in values:
        comment = 'should' if 10000 >= i > 0 else 'should not'
        assert credit is not None and credit.check_withdrawal_value(
            200) == True, f'${i} {comment} be allowed to be withdrew from the Credit account'


# Requirements 3.1, 3.4.3, 3.4.5
def test_check_withdrawal_from_savings():
    values = [-200, 200, 100000]
    customer = retrieve_customer_info()
    savings = customer.get_savings_account()
    for i in values:
        assert savings is not None and savings.check_withdrawal_value(
            i) == False, f'{i} should not be allowed to be withdrew from the Savings account'
