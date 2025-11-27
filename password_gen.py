import streamlit as st
import random
import string

# --- Setup ---
st.set_page_config(page_title="Password Generator", page_icon="🔐")

# Initialize session state so the password persists (doesn't change when sliding)
if 'password' not in st.session_state:
    st.session_state['password'] = ""

# --- Logic Function ---
def generate_password():
    # We read the values from the session_state widgets
    length = st.session_state.length_slider
    use_digits = st.session_state.digits_toggle
    use_symbols = st.session_state.symbols_toggle

    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Update the password in session state
    st.session_state['password'] = ''.join(random.choice(characters) for _ in range(length))

# --- UI Layout ---
st.title("🔐 Password Generator")

with st.container(border=True):
    st.write("### Customize your password")
    
    # 1. Slider and Number Display
    col_slide, col_num = st.columns([4, 1])
    
    with col_slide:
        # Added key="length_slider" to access this value in the callback
        st.slider("Characters", min_value=4, max_value=35, value=20, 
                  label_visibility="collapsed", key="length_slider")
    
    with col_num:
        st.button(f"{st.session_state.length_slider}", disabled=True, use_container_width=True)

    # 2. Toggles
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.toggle("Numbers", value=True, key="digits_toggle")
    with t_col2:
        st.toggle("Symbols", value=False, key="symbols_toggle")

    st.divider()

    # 3. Generate Button (Primary Action)
    # The password will ONLY change when this button is clicked
    if st.button("Generate Password", type="primary", use_container_width=True):
        generate_password()

    # 4. Display & Copy
    st.write("### Generated password")
    
    if st.session_state['password']:
        # st.code creates a box with a working Copy button in the top right
        st.code(st.session_state['password'], language=None)
        
        # 5. Strength Meter
        strength_len = len(st.session_state['password'])
        if strength_len < 8:
            st.markdown(":red[🔴 Weak] _(Less than 8 characters)_")
        elif strength_len < 16:
            st.markdown(":orange[🟡 Strong] _(Between 8 and 15 characters)_")
        else:
            st.markdown(":green[🟢 Super Strong] _(16+ characters)_")
    else:
        st.info("Click 'Generate Password' to start.")

    st.write("") # Spacer