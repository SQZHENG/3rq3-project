"""This function stimulates the process of retrieving information from a database when a user logs in."""


def retrieve_customer_info():
    from ypb_website.customer import Customer
    customer = Customer('zhengs46', '#@F$!s', 'Siqi', 'Zheng', '1280 Main St W, Hamilton, ON L8S 4L8',
                        ["""list of banking accounts"""])
    return customer


# Requirement 3.3.1
def test_display_chequeing_account():
    customer = retrieve_customer_info()
    chequeing_account = customer.get_chequeing_account()
    assert chequeing_account is not None and chequeing_account.acc_type == 'Chequeing', 'account type should be Chequeing.'


# Requirement 3.3.1
def test_display_credit_account():
    customer = retrieve_customer_info()
    credit_account = customer.get_credit_account()
    assert credit_account is not None and credit_account.acc_type == 'Credit', 'account type should be Credit.'


# Requirement 3.3.1
def test_display_savings_account():
    customer = retrieve_customer_info()
    savings_account = customer.get_savings_account()
    assert savings_account is not None and savings_account.acc_type == 'Savings', 'account type should be Savings.'


# Requirement 3.3.2
def test_move_from_chequeing_to_credit():
    customer = retrieve_customer_info()
    assert customer.move_money('Chequeing', 'Credit', '27/11/2020',
                               200) == True, 'should successfully move the money from Chequeing to Credit.'


# Requirement 3.3.2
def test_move_from_chequeing_to_savings():
    customer = retrieve_customer_info()
    assert customer.move_money('Chequeing', 'Savings', '27/11/2020',
                               400) == True, 'should successfully move the money from Chequeing to Savings.'


# Requirement 3.3.2
def test_move_from_credit_to_chequeing():
    customer = retrieve_customer_info()
    assert customer.move_money('Credit', 'Chequeing', '27/11/2020',
                               500) == True, 'should successfully move the money from Credit to Chequeing.'


# Requirement 3.3.2
def test_move_from_credit_to_savings():
    customer = retrieve_customer_info()
    assert customer.move_money('Credit', 'Savings', '27/11/2020',
                               200) == True, 'should successfully move the money from Credit to Savings.'


# Requirement 3.3.2
def test_move_from_savings_to_chequeing():
    customer = retrieve_customer_info()
    assert customer.move_money('Savings', 'Chequeing', '27/11/2020',
                               200) == True, 'should successfully move the money from Savings to Chequeing.'


# Requirement 3.3.2
def test_move_from_savings_to_credit():
    customer = retrieve_customer_info()
    assert customer.move_money('Savings', 'Credit', '27/11/2020',
                               200) == True, 'should successfully move the money from Savings to Credit.'
