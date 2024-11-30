


def user_acc():
    name = input("\nEnter your name: ")
    print(f"\nGood day, Ma'am/Sir {name}! Welcome to Rvn Bank.")
    initial_deposit = float(input("\nEnter the initial deposit amount: "))
    return {"name": name, "balance": initial_deposit}

def current_balance(account):
    print(f"\nMa'am/Sir {account["name"]}, your current balance is: ₱{account["balance"]}")

def deposit(account):
    amount = float(input("\nEnter the amount to deposit: "))
    if amount > 0:
        account["balance"] += amount
        print(f"\nSuccessfully deposited ₱{amount}")
    else:
        print("\nDeposit amount must be greater than 0.")
    current_balance(account)

def filo_denom(amount):
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    result = {}
    
    for denom in denominations:
        if amount >= denom:
            fDiv = amount // denom
            result[denom] = fDiv
            amount -= fDiv * denom
    return result

def denomi_bd(bk_denomi):
    print("\nDenomination Breakdown:")
    for denom, count in bk_denomi.items():
        print(f"{count} pc/s of ₱{denom} ")

def withdraw(account):
    amount = float(input("\nEnter the amount to withdraw: "))
    if 0 < amount <= account["balance"]:
        account["balance"] -= amount
        print(f"\nSuccessfully withdrew ₱{amount}")
        
        breakdown = filo_denom(int(amount))
        denomi_bd(breakdown)
    else:
        print("Invalid withdrawal amount.")
    current_balance(account)

def main():
    account = user_acc()
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == "1":
            deposit(account)
        elif choice == "2":
            withdraw(account)
        elif choice == "3":
            current_balance(account)
        elif choice == "4":
            print("\nThank you for using the Rvn banking system.")
            break
        else:
            print("Invalid choice. Please select from options 1-4.")

if __name__ == "__main__":
    main()
