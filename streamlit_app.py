import streamlit as st

st.set_page_config(page_title="QR Code Quiz 3", page_icon="🧠")
st.title("🧩 College Corps Mid-Year Workshop!")
st.markdown("<h3 style='color:#4CAF50;'>Let's see if you can solve this!</h3>", unsafe_allow_html=True)

question = "How many campuses have a College Corps Program?"
choices = ["39", "41", "42", "44"]
correct_answer = "44"
success_message = "✅ Correct! Great job!"
try_again_message = "❌ Try again!"


if "answered_correctly" not in st.session_state:
    st.session_state.answered_correctly = False

st.subheader(question)
user_choice = st.radio("Choose your answer:", choices, index=None)

if st.button("Submit"):
    if user_choice == correct_answer:
        st.session_state.answered_correctly = True
        st.success(success_message)
    else:
        st.warning(try_again_message)

if st.session_state.answered_correctly:
    st.balloons()
    st.info("You solved this question! You can close this tab or scan the next QR.")
