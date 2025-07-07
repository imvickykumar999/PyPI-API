## VickClass - Bank\_Account Utility

**VickClass** is a simple Python package that provides a basic simulation of a bank account.
It allows users to **deposit**, **withdraw**, and **check balance**, making it great for beginner-level understanding of object-oriented programming in Python.

---

### 📦 Installation

Install directly from PyPI:

```bash
pip install VickClass
```

---

### 🧠 Features

* Deposit money
* Withdraw money (with insufficient balance check)
* Display current balance

---

### 🧪 Usage Example

```python
from vicksclass.vicks import Bank_Account

# Create an account with an optional initial balance
account = Bank_Account(balance=1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Display balance
account.display()
```

---

### 📁 Class Reference

#### `Bank_Account(balance=0)`

Initializes the account with a balance. Default is `0`.

#### `.deposit(amount)`

Adds the specified amount to the balance.

#### `.withdraw(amount)`

Subtracts the specified amount if sufficient balance is available. Otherwise, prints a warning.

#### `.display()`

Prints the current available balance.

---

### 🧑‍💻 Author

[Vicky Kumar](https://github.com/imvickykumar999)
Email: [imvickykumar999@gmail.com](mailto:imvickykumar999@gmail.com)

---

### 🪪 License

This project is licensed under the [MIT License](./License.txt)
