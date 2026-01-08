from account import account_details
def account_details_output():
    return account_details("24ECF123","tanu","saving",32000)
expected=(
    " acc_no= 24ECF123\n"
    "acc_name = tanu\n"
    "acc_type = savings\n"
    "bal = 32000\n"

)
assert return==expected
