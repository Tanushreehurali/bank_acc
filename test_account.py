from account import account_details
def account_details_output():
    return account_details("24ECF123","tanu","saving",32000)
expected=(
    "account_no=24ECF123\n"
    "account holdername=tanu\n"
    "account_type=saving\n"
    "balance=32000\n"

)
assert return==expected
