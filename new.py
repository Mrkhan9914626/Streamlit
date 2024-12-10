import streamlit as st

class BankAccount:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        self.accounts[account_number] = {"balance": initial_balance}
        return "Account created successfully."

    def deposit(self, acc_no, amount):
        if acc_no not in self.accounts:
            return "Account does not exist."
        else:
            self.accounts[acc_no]["balance"] += amount
            return f"{amount} deposited successfully."

    def withdraw(self, acc_no, amount):
        if acc_no not in self.accounts:
            return "Account does not exist."
        else:
            if amount > self.accounts[acc_no]["balance"]:
                return "Insufficient balance."
            else:
                self.accounts[acc_no]["balance"] -= amount
                return f"{amount} withdrawn successfully."

    def check_balance(self, acc_no):
        if acc_no not in self.accounts:
            return "Account does not exist."
        else:
            return f"Your balance is: {self.accounts[acc_no]['balance']}"

# Initialize BankAccount in session state
if "bank_account" not in st.session_state:
    st.session_state.bank_account = BankAccount()

# Access the stored BankAccount instance
account = st.session_state.bank_account

# Streamlit UI
st.title("Bank Account Management System")

menu = ["Create Account", "Deposit", "Withdraw", "Check Balance", "Exit"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Account":
    st.subheader("Create a New Account")
    acc_no = st.text_input("Enter Account Number")
    balance = st.number_input("Enter Initial Balance", min_value=0.0, step=0.01)
    if st.button("Create Account"):
        if acc_no and balance >= 0:
            result = account.create_account(acc_no, balance)
            st.success(result)
        else:
            st.error("Please provide valid inputs.")

elif choice == "Deposit":
    st.subheader("Deposit Money")
    acc_no = st.text_input("Enter Account Number")
    amount = st.number_input("Enter Deposit Amount", min_value=1.0, step=0.01)
    if st.button("Deposit"):
        if acc_no and amount > 0:
            result = account.deposit(acc_no, amount)
            st.success(result)
        else:
            st.error("Please provide valid inputs.")

elif choice == "Withdraw":
    st.subheader("Withdraw Money")
    acc_no = st.text_input("Enter Account Number")
    amount = st.number_input("Enter Withdrawal Amount", min_value=1.0, step=0.01)
    if st.button("Withdraw"):
        if acc_no and amount > 0:
            result = account.withdraw(acc_no, amount)
            st.success(result)
        else:
            st.error("Please provide valid inputs.")

elif choice == "Check Balance":
    st.subheader("Check Account Balance")
    acc_no = st.text_input("Enter Account Number")
    if st.button("Check Balance"):
        if acc_no:
            result = account.check_balance(acc_no)
            st.info(result)
        else:
            st.error("Please provide a valid account number.")

elif choice == "Exit":
    st.subheader("Thank you for using the bank!")
    st.stop()

