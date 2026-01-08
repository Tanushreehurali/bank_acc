rom account import account_details

def test_account_details():
    result = account_details(
        "24ecf1234",
        "tanu",
        "savings",
        32000
    )

    expected = (
        "Account Number: 24ecf1234\n"
        "Account Holder Name: tanu\n"
        "Account Type: savings\n"
        "Balance: 32000\n"
    )

    assert result == expected
    
