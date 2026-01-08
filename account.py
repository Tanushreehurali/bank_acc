def account_details(acc_no,acc_name,acc_type,bal):
    result = (
        f"acc_number: {acc_no}\n"
        f"acc_name: {acc_name}\n"
        f"acc_type: {acc_type}\n"
        f"balance: {bal}"
    )
    return result


if __name__ == "__main__":
    acc_no= "24ECF123"
    acc_name = "tanu"
    acc_type = "savings"
    bal = 32000

    print(account_details(acc_no,acc_name,acc_type,bal))
