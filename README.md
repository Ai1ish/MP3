# MP3 – Banking System Refactoring

## Object-Oriented Programming Structure

### `BankAccount` (Base Class)

Handles shared account functionality such as:

- Account number
- Account holder name
- Balance
- Transaction history

### Methods Included

- `deposit()`
- `withdraw()`
- `transfer()`
- `show_history()`

---

### `SavingsAccount` (Subclass)

Extends `BankAccount`.

#### Additional Features
- Interest calculation
- Minimum balance rules

---

### `CheckingAccount` (Subclass)

Extends `BankAccount`.

#### Additional Features
- Checking-specific withdrawal rules
- Optional overdraft handling
- Possible transaction fees

---

# Added Transaction History with Timestamps

The system now:

- Imports the `datetime` module
- Stores every transaction in a list
- Records:
  - Transaction type
  - Amount
  - Exact date and time

Example:
```python
2026-05-18 10:30AM - Deposited $50
```

---

# Continuous Menu Loop

The program now uses:

```python
while True:
```

This allows the menu to continuously run until the user chooses to exit.

Benefits:
- Users can perform multiple actions without restarting the program
- Creates a true menu-driven banking system

---

# Banking Logic

## Deposits
- Balances update correctly after deposits

## Withdrawals
- The system checks for insufficient funds before allowing withdrawals

## Transfers
Accounts can now transfer money between each other.

The system:
1. Withdraws from the sender
2. Deposits into the receiver
3. Logs both transactions

---

# Support for Multiple Accounts

The system now supports:

- Multiple bank accounts
- Different account types
- Account lookup using account numbers

Example:
```python
accounts = {}
```

---
