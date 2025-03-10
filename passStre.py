import streamlit as st
import re
import random
import string

# Check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check uppercase and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Check digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Check special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Suggest strong password
def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.markdown("Check how secure your password is and get tips to improve it.")

password = st.text_input("Enter your password", type="password")

if password:
    # Blacklist check
    blacklist = ["password", "123456", "qwerty", "admin", "password123"]
    if password.lower() in blacklist:
        st.error("❌ This is a commonly used password. Choose something more unique.")
    else:
        score, feedback = check_password_strength(password)

        # Display result
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider improving it.")
            for f in feedback:
                st.write(f)
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below:")
            for f in feedback:
                st.write(f)

    # Strong password suggestion
    st.markdown("---")
    st.write("Need help? Click below to generate a strong password:")
    if st.button("🔄 Generate Strong Password"):
        strong_password = generate_strong_password()
        st.code(strong_password, language="text")
