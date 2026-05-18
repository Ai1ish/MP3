import datetime

class BankAccount:
    def __init__(self, name, initial_deposit=0):
        self.name = name
        self.balance = initial_deposit
        self.transaction_history = []
        self._record_transaction(f"Account created with initial balance: ${initial_deposit:.2f}")

    def _record_transaction(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(f"[{timestamp}] {message}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._record_transaction(f"Deposited ${amount:.2f}")
            print(f"Success! Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self._record_transaction(f"Withdrew ${amount:.2f}")
                print(f"Success! Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
                return True
            else:
                print("Insufficient funds!")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def transfer(self, target_account, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                target_account.balance += amount
                self._record_transaction(f"Transferred ${amount:.2f} to {target_account.name}")
                target_account._record_transaction(f"Received ${amount:.2f} from {self.name}")
                print(f"Success! Transferred ${amount:.2f} to {target_account.name}.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Transfer amount must be positive.")

    def get_history(self):
        return self.transaction_history


class SavingsAccount(BankAccount):
    def __init__(self, name, initial_deposit=0, interest_rate=0.03, min_balance=100):
        super().__init__(name, initial_deposit)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def withdraw(self, amount):
        # Enforce minimum balance
        if self.balance - amount < self.min_balance:
            fee = 10.0
            print(f"Warning: This withdrawal drops your balance below the minimum (${self.min_balance}). A ${fee} fee will be applied.")
            if self.balance >= (amount + fee):
                self.balance -= (amount + fee)
                self._record_transaction(f"Withdrew ${amount:.2f} (Minimum balance fee ${fee:.2f} applied)")
                print(f"Success! Withdrew ${amount:.2f} (Fee: ${fee:.2f}). New balance: ${self.balance:.2f}")
                return True
            else:
                print("Insufficient funds to cover the withdrawal and the fee.")
                return False
        else:
            return super().withdraw(amount)
            
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._record_transaction(f"Interest added: ${interest:.2f} at rate {self.interest_rate*100}%")
        print(f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, name, initial_deposit=0, overdraft_limit=50):
        super().__init__(name, initial_deposit)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
                self._record_transaction(f"Withdrew ${amount:.2f}")
                if self.balance < 0:
                    print(f"Success! Withdrew ${amount:.2f}. Account is overdrawn by ${-self.balance:.2f}")
                else:
                    print(f"Success! Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
                return True
            else:
                print("Insufficient funds, overdraft limit exceeded.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False


def print_header(text):
    print(f"\n{text.center(57)}")
    print("_,-'\"`-._,-'\"`-._,-'\"`-._,-'\"`-._,-'\"`-._,-'\"`-._,-'\"`-._")

def get_account_from_user(users):
    if not users:
        print("No accounts exist yet. Please create one first.")
        return None
    
    print("\nSelect an account:")
    for idx, acc in enumerate(users):
        print(f"{idx + 1}. {acc.name} ({type(acc).__name__})")
        
    try:
        choice = int(input("Enter account number: ")) - 1
        print()
        if 0 <= choice < len(users):
            return users[choice]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def main():
    title = "Maya Bank"
    users = []

    while True:
        print("\n╔────────────────────────────────────────╗")
        print("│          Welcome to Maya Bank          │")
        print("│                                        │")
        print("│  1. Add Account                        │")
        print("│  2. Deposit / Withdraw                 │")
        print("│  3. Check Balance                      │")
        print("│  4. Add Savings Interest               │")
        print("│  5. Send / Transfer Funds              │")
        print("│  6. View Transaction History           │")
        print("│  7. Exit                               │")
        print("╚────────────────────────────────────────╝")
        
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print_header("ADD ACCOUNT")
            name = input("Name of the user: ")
            print("Account Type:")
            print("1. Savings Account (Requires $100 min balance to avoid fees, earns interest)")
            print("2. Checking Account (Has $50 overdraft limit)")
            
            acc_type = input("Choose type (1-2): ")
            
            try:
                initial = float(input("Enter initial deposit amount: $"))
                if initial < 0:
                    print("Initial deposit cannot be negative.")
                    continue
                    
                if acc_type == "1":
                    new_account = SavingsAccount(name, initial)
                    users.append(new_account)
                    print(f"Savings Account created successfully for {name}!")
                elif acc_type == "2":
                    new_account = CheckingAccount(name, initial)
                    users.append(new_account)
                    print(f"Checking Account created successfully for {name}!")
                else:
                    print("Invalid account type selected.")
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            print_header("DEPOSIT / WITHDRAW")
            acc = get_account_from_user(users)
            if acc:
                print("1. Deposit")
                print("2. Withdraw")
                action = input("Choose action (1-2): ")
                
                if action in ["1", "2"]:
                    try:
                        amount = float(input("Enter amount: $"))
                        if action == "1":
                            acc.deposit(amount)
                        elif action == "2":
                            acc.withdraw(amount)
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")
                else:
                    print("Invalid action selected.")

        elif choice == "3":
            print_header("CHECK BALANCE")
            acc = get_account_from_user(users)
            if acc:
                print(f"\nAccount Name: {acc.name}")
                print(f"Account Type: {type(acc).__name__}")
                print(f"Current Balance: ${acc.balance:.2f}")

        elif choice == "4":
            print_header("ADD SAVINGS INTEREST")
            acc = get_account_from_user(users)
            if acc:
                if isinstance(acc, SavingsAccount):
                    acc.add_interest()
                else:
                    print(f"Error: {acc.name} has a {type(acc).__name__}. Only Savings Accounts earn interest.")

        elif choice == "5":
            print_header("SEND / TRANSFER FUNDS")
            if len(users) < 2:
                print("You need at least 2 accounts to make a transfer.")
                continue
                
            print("Select the account to transfer FROM:")
            from_acc = get_account_from_user(users)
            if from_acc:
                print("\nSelect the account to transfer TO:")
                to_acc = get_account_from_user(users)
                
                if to_acc:
                    if from_acc == to_acc:
                        print("Cannot transfer to the same account.")
                        continue
                        
                    try:
                        amount = float(input("Enter amount to transfer: $"))
                        from_acc.transfer(to_acc, amount)
                    except ValueError:
                        print("Invalid amount.")

        elif choice == "6":
            print_header("VIEW TRANSACTION HISTORY")
            acc = get_account_from_user(users)
            if acc:
                print(f"\nTransaction History for {acc.name}:")
                history = acc.get_history()
                if not history:
                    print("No transactions yet.")
                else:
                    for entry in history:
                        print(entry)

        elif choice == "7":
            print("\nAre you sure you want to exit?")
            print("1. Yes")
            print("2. No")
            exit_choice = input("Enter your choice (1-2): ")
            
            if exit_choice == "1":
                print("Thank you for using Maya Bank. Goodbye!")
                break
            elif exit_choice == "2":
                print("Returning to main menu...")
            else:
                print("Invalid choice, returning to main menu.")

        else:
            print("\nInvalid Choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
