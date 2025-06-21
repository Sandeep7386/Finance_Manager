import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finance Manager", layout="centered")
st.title("💸 Personal Finance Manager")

# Initialize the session state
if "transactions" not in st.session_state:
    st.session_state.transactions = pd.DataFrame(columns=["Description", "Amount"])

# Transaction Entry Form
with st.form("transaction_form"):
    col1, col2 = st.columns(2)
    with col1:
        description = st.text_input("Description")
    with col2:
        amount = st.number_input("Amount", step=0.01, format="%.2f")
    submit = st.form_submit_button("Add Transaction")

# Add the transaction
if submit:
    if description:
        new_transaction = pd.DataFrame([[description, amount]], columns=["Description", "Amount"])
        st.session_state.transactions = pd.concat([
            new_transaction,
            st.session_state.transactions
        ], ignore_index=True)
        st.success(f"Transaction added: {description} (${amount:.2f})")
    else:
        st.warning("Please enter a description.")

# Display total balance
total = st.session_state.transactions["Amount"].sum()
st.markdown(f"### 💰 Total Balance: ${total:.2f}")

# Display transaction history
st.subheader("📋 Transaction History")
if not st.session_state.transactions.empty:
    st.dataframe(st.session_state.transactions, use_container_width=True)
else:
    st.info("No transactions yet. Add one above.")
