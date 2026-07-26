import streamlit as st
from database import connect_database, account_number_genrator
from style import apply_theme

# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="CodexBank",
    page_icon="🖤",
    layout="centered",
)

# ------------------------------------------------------------------
# APPLY BLACK-GLASS 3D THEME
# ------------------------------------------------------------------
apply_theme()

# ------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------
st.markdown('<div class="main-title">🖤 CodexBank</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#9ca3af; margin-top:-15px;">Dark Mode Banking</p>', unsafe_allow_html=True)

# ------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ------------------------------------------------------------------
menu = st.sidebar.radio(
    "Choose an action",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Account Details",
        "Update Details",
        "Delete Account",
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption("CodexBank · Black Glass UI")


def glass_start():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)


def glass_end():
    st.markdown('</div>', unsafe_allow_html=True)


def is_valid_pin(pin):
    """Checks the PIN box actually has a 4 digit number in it,
    so we never try int() on empty or weird text."""
    return pin.isdigit() and len(pin) == 4


# ------------------------------------------------------------------
# 1. CREATE ACCOUNT
# ------------------------------------------------------------------
if menu == "Create Account":
    glass_start()
    st.subheader("📝 Create a New Account")

    with st.form("create_account_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        mobile_no = st.text_input("Mobile Number")
        email = st.text_input("Email ID")
        address = st.text_area("Permanent Address")
        pin = st.text_input("Set a 4 digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Create Account")

    if submitted:
        if not name or not mobile_no or not email or not address:
            st.error("Please fill in all the fields.")
        elif age < 18:
            st.error("Age must be 18 or above to open an account.")
        elif not (pin.isdigit() and len(pin) == 4):
            st.error("PIN must be exactly 4 digits.")
        else:
            account_number = account_number_genrator()
            conn = connect_database()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (
                    account_number, full_name, age, mobile, email,
                    address, balance, pin
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (account_number, name, age, mobile_no, email, address, 0, int(pin)))
            conn.commit()
            conn.close()
            st.success("Account created successfully! 🎉")
            st.info(f"Your Account Number is: **{account_number}**")

    glass_end()

# ------------------------------------------------------------------
# 2. DEPOSIT MONEY
# ------------------------------------------------------------------
elif menu == "Deposit Money":
    glass_start()
    st.subheader("💰 Deposit Money")

    with st.form("deposit_form"):
        account = st.text_input("Account Number")
        pin = st.text_input("4 digit PIN", type="password", max_chars=4)
        amount = st.number_input("Amount to Deposit", min_value=1, step=1)
        submitted = st.form_submit_button("Deposit")

    if submitted:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT pin, balance FROM users WHERE account_number = ?", (account,))
        data = cursor.fetchone()
        if data is None:
            st.error("Account number is not correct.")
        elif not is_valid_pin(pin):
            st.error("Please enter your 4 digit PIN.")
        elif int(pin) != data[0]:
            st.error("Incorrect PIN.")
        else:
            new_balance = data[1] + amount
            cursor.execute("UPDATE users SET balance = ? WHERE account_number = ?", (new_balance, account))
            conn.commit()
            st.success("Deposit successful! ✅")
            st.markdown(f'<div class="balance-box">New Balance: ₹{new_balance}</div>', unsafe_allow_html=True)
        conn.close()

    glass_end()

# ------------------------------------------------------------------
# 3. WITHDRAW MONEY
# ------------------------------------------------------------------
elif menu == "Withdraw Money":
    glass_start()
    st.subheader("💸 Withdraw Money")

    with st.form("withdraw_form"):
        account = st.text_input("Account Number")
        pin = st.text_input("4 digit PIN", type="password", max_chars=4)
        amount = st.number_input("Amount to Withdraw", min_value=1, step=1)
        submitted = st.form_submit_button("Withdraw")

    if submitted:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT pin, balance FROM users WHERE account_number = ?", (account,))
        data = cursor.fetchone()
        if data is None:
            st.error("Account number is not correct.")
        elif not is_valid_pin(pin):
            st.error("Please enter your 4 digit PIN.")
        elif int(pin) != data[0]:
            st.error("Incorrect PIN.")
        elif amount > data[1]:
            st.error("Insufficient balance.")
        else:
            new_balance = data[1] - amount
            cursor.execute("UPDATE users SET balance = ? WHERE account_number = ?", (new_balance, account))
            conn.commit()
            st.success("Withdraw successful! ✅")
            st.markdown(f'<div class="balance-box">New Balance: ₹{new_balance}</div>', unsafe_allow_html=True)
        conn.close()

    glass_end()

# ------------------------------------------------------------------
# 4. ACCOUNT DETAILS
# ------------------------------------------------------------------
elif menu == "Account Details":
    glass_start()
    st.subheader("📋 Account Details")

    with st.form("details_form"):
        account = st.text_input("Account Number")
        pin = st.text_input("4 digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("View Details")

    if submitted:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT pin FROM users WHERE account_number = ?", (account,))
        data = cursor.fetchone()
        if data is None:
            st.error("Account number is not correct.")
        elif not is_valid_pin(pin):
            st.error("Please enter your 4 digit PIN.")
        elif int(pin) != data[0]:
            st.error("Incorrect PIN.")
        else:
            cursor.execute("SELECT * FROM users WHERE account_number = ?", (account,))
            row = cursor.fetchone()
            cols = ["Account Number", "Name", "Age", "Mobile", "Email", "Address", "Balance", "PIN"]
            for label, value in zip(cols, row):
                if label == "PIN":
                    continue
                st.write(f"**{label}:** {value}")
        conn.close()

    glass_end()

# ------------------------------------------------------------------
# 5. UPDATE DETAILS
# ------------------------------------------------------------------
elif menu == "Update Details":
    glass_start()
    st.subheader("✏️ Update Details")

    account = st.text_input("Account Number", key="upd_acc")
    pin = st.text_input("4 digit PIN", type="password", max_chars=4, key="upd_pin")
    field = st.selectbox("What do you want to update?", ["Mobile Number", "Email", "PIN"])

    if field == "Mobile Number":
        with st.form("update_mobile_form"):
            old_mobile = st.text_input("Old Mobile Number")
            new_mobile = st.text_input("New Mobile Number")
            submitted = st.form_submit_button("Update Mobile")
        if submitted:
            conn = connect_database()
            cursor = conn.cursor()
            cursor.execute("SELECT pin, mobile FROM users WHERE account_number = ?", (account,))
            data = cursor.fetchone()
            if data is None:
                st.error("Account number is not correct.")
            elif not is_valid_pin(pin):
                st.error("Please enter your 4 digit PIN.")
            elif int(pin) != data[0]:
                st.error("Incorrect PIN.")
            elif old_mobile != data[1]:
                st.error("Old mobile number did not match.")
            else:
                cursor.execute("UPDATE users SET mobile = ? WHERE account_number = ?", (new_mobile, account))
                conn.commit()
                st.success("Mobile number updated successfully! ✅")
            conn.close()

    elif field == "Email":
        with st.form("update_email_form"):
            old_email = st.text_input("Old Email")
            new_email = st.text_input("New Email")
            submitted = st.form_submit_button("Update Email")
        if submitted:
            conn = connect_database()
            cursor = conn.cursor()
            cursor.execute("SELECT pin, email FROM users WHERE account_number = ?", (account,))
            data = cursor.fetchone()
            if data is None:
                st.error("Account number is not correct.")
            elif not is_valid_pin(pin):
                st.error("Please enter your 4 digit PIN.")
            elif int(pin) != data[0]:
                st.error("Incorrect PIN.")
            elif old_email != data[1]:
                st.error("Old email did not match.")
            else:
                cursor.execute("UPDATE users SET email = ? WHERE account_number = ?", (new_email, account))
                conn.commit()
                st.success("Email updated successfully! ✅")
            conn.close()

    elif field == "PIN":
        with st.form("update_pin_form"):
            new_pin = st.text_input("New 4 digit PIN", type="password", max_chars=4)
            submitted = st.form_submit_button("Update PIN")
        if submitted:
            conn = connect_database()
            cursor = conn.cursor()
            cursor.execute("SELECT pin FROM users WHERE account_number = ?", (account,))
            data = cursor.fetchone()
            if data is None:
                st.error("Account number is not correct.")
            elif not is_valid_pin(pin):
                st.error("Please enter your current 4 digit PIN.")
            elif int(pin) != data[0]:
                st.error("Incorrect current PIN.")
            elif not (new_pin.isdigit() and len(new_pin) == 4):
                st.error("New PIN must be exactly 4 digits.")
            else:
                cursor.execute("UPDATE users SET pin = ? WHERE account_number = ?", (int(new_pin), account))
                conn.commit()
                st.success("PIN updated successfully! ✅")
            conn.close()

    glass_end()

# ------------------------------------------------------------------
# 6. DELETE ACCOUNT
# ------------------------------------------------------------------
elif menu == "Delete Account":
    glass_start()
    st.subheader("🗑️ Delete Account")

    with st.form("delete_form"):
        account = st.text_input("Account Number")
        pin = st.text_input("4 digit PIN", type="password", max_chars=4)
        confirm = st.checkbox("I confirm I want to permanently delete this account")
        submitted = st.form_submit_button("Delete Account")

    if submitted:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("SELECT pin FROM users WHERE account_number = ?", (account,))
        data = cursor.fetchone()
        if data is None:
            st.error("Account number is not correct.")
        elif not is_valid_pin(pin):
            st.error("Please enter your 4 digit PIN.")
        elif int(pin) != data[0]:
            st.error("Incorrect PIN.")
        elif not confirm:
            st.warning("Please check the confirmation box to delete your account.")
        else:
            cursor.execute("DELETE FROM users WHERE account_number = ?", (account,))
            conn.commit()
            st.success("Account deleted successfully.")
        conn.close()

    glass_end()