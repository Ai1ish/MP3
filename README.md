# Python Mini-Projects (MP3)
By: 
BUMATAY, GERMIONE GUINEVERE RIELLE
MACULANGAN, ALEIA
NARVASA, AILISH SOPHIA 
PEDRIALVA, BYRON RAMIL

This repository contains a collection of three interactive, text-based Python applications built as part of a school project. Each program demonstrates different programming concepts, including Object-Oriented Programming (OOP), complex data structures (like nested dictionaries), and interactive command-line menus.

## 1. Maya Bank System (`MP3-BankSystem-G9.py`)
A comprehensive banking simulation built using Object-Oriented Programming. It utilizes a parent `BankAccount` class and specialized child classes to enforce specific banking rules.

**Key Features:**
*   **Account Types:** Create `SavingsAccount` (requires a minimum balance and earns interest) or `CheckingAccount` (allows overdrafts up to a certain limit).
*   **Transactions:** Deposit, withdraw, and transfer funds between different accounts.
*   **Transaction Logging:** Automatically timestamps and records every action taken on an account, which can be viewed in the transaction history.

## 2. Gradebook Manager (`MP3-GradeBook-G9.py`)
A relational data management system that acts as a digital gradebook for teachers. It uses Python dictionaries to link students, assignment categories, and specific grades together.

**Key Features:**
*   **Student Management:** Add, view, and remove students from the roster.
*   **Category Weighting:** Create categories (e.g., Homework, Exams) and assign them specific percentage weights towards the final grade.
*   **Grading & Statistics:** Enter grades for specific assignments, view class averages, and find the highest/lowest grades.
*   **Report Cards:** Automatically generate and print detailed report cards for individual students or the entire class, displaying weighted averages and final letter grades.

## 3. Inventory Management System (`MP3-InventorySystem-G9.py`)
A practical business tool designed to handle the complete lifecycle of store products and track sales. 

**Key Features:**
*   **Stock Tracking:** Add new products, update existing information, and automatically deduct from stock when a sale is recorded.
*   **Financial Calculator:** Calculate the total value of all items in the warehouse.
*   **VAT & Discounts:** Apply dynamic percentage-based or fixed discounts, as well as VAT calculations during checkout.
*   **Low Stock Alerts:** Automatically scans the inventory and warns the user if any product falls to 5 items or below.
*   **Sales History:** Keeps a running log of all successful sales transactions.

---

### How to Run
To run any of these applications, open your terminal or command prompt, navigate to the folder containing the files, and run them using Python:

```bash
python bankSystem.py
python mp3-gradebook.py
python MP3-InventorySystem-G9.py
```
