import streamlit as st
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Pre-Consultation Chatbot",
    page_icon="💬",
    layout="centered"
)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'student_id' not in st.session_state:
    st.session_state.student_id = ""
if 'session_id' not in st.session_state:
    st.session_state.session_id = f"session_{random.randint(1000000000, 9999999999)}"
if 'turns_used' not in st.session_state:
    st.session_state.turns_used = 0
if 'include_history' not in st.session_state:
    st.session_state.include_history = True
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Custom CSS for styling
st.markdown("""
    <style>
    
    /* Version badge styling */
    .version-badge {
        display: inline-block;
        background-color: #c8e6c9;
        color: #2e7d32;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 2rem;
    }
            
    /* Number styling in sidebar */
    .number {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

def isValidStudentID(student_id):
    if len(student_id) != 9:
        return False
    if student_id[0].upper() != 'A':
        return False
    if not student_id[1:8].isdigit():
        return False
    if not student_id[8].isalnum():
        return False
    return True

# Function to show login page
def show_login_page(key=None):
    # Header section
    st.header("Pre-Consultation Chatbot")
    #st.badge("Version: Version B", color="green")

    st.markdown('<div class="version-badge">Version: Version B</div>', unsafe_allow_html=True)

    # Add horizontal line
    st.markdown("---")

    # Main content
    st.header("Student Login")

    # Info message
    st.info("Please log in with your student ID to access the mental health pre-consultation chatbot.")

    with st.form("login_form", border=True):
        # Student ID input
        student_id = st.text_input(
            "Student ID",
            placeholder="e.g., A0123456X",
            max_chars=9,
            help="Enter your 9-character student ID (format: A0123456X)"
        )

        # Character counter
        if student_id:
            char_count = len(student_id)
        else:
            char_count = 0

        # Login button (submit button must be inside the form)
        submitted = st.form_submit_button("Login", type="secondary", width="stretch")
        
    # Handle form submission (validation happens outside the form context)
    if submitted:
        if not student_id:
            st.warning("Please enter your student ID")
        elif not isValidStudentID(student_id):
            st.error("Invalid student ID format. Please use format like: A0123456X")
        else:
            # Get valid student ID from environment variable
            valid_student_id = os.getenv("VALID_STUDENT_ID", "A1234567Q")
            
            if student_id.upper() != valid_student_id.upper():
                st.error("Invalid student ID")
            else:
                st.session_state.logged_in = True
                st.session_state.student_id = student_id.upper()
                st.rerun()

    # Instructions expander
    with st.expander("ℹ️ Instructions"):
        st.markdown("**How to use this system:**")
        st.markdown("""
        1. Enter your registered student ID (format: A0123456X)
        2. Each student has a maximum of 50 conversation turns per version
        3. Please use the system responsibly for the assignment
        """)
        
        st.markdown("**Important notes:**")
        st.markdown("""
        - This is a pre-consultation support system, not a replacement for professional help
        - The system cannot provide medical diagnoses or treatment
        - In case of emergency, please contact professional services immediately
        """)


# Function to show chatbot page
def show_chatbot_page():
    # Sidebar
    with st.sidebar:
        st.markdown("## 📊 Usage Statistics")
        #st.write("Turns Used")
        st.markdown(f'Turns Used<div class="number">{st.session_state.turns_used}/50</div>', unsafe_allow_html=True)
        #st.write("Remaining")
        st.markdown(f'Remaining<div class="number">{50 - st.session_state.turns_used}</div>', unsafe_allow_html=True)
        
        st.divider()
        
        st.caption(f"Session ID: {st.session_state.session_id}")
                
        st.markdown("## ⚙️ Settings")
        st.toggle(
            "Include conversation history",
            key="include_history",
            value=st.session_state.include_history,
            help="Include previous messages in the conversation context"
        )
        
        if st.button("Reset conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        st.divider()
        
        st.markdown("## ⚠️ Important")
        st.markdown("""
        - This is for Assignment 2 research only
        - After refreshing the page, you need to log in again.
        - Please allocate the quota reasonably for each participant.
        - You can close the left sidebar during the experiment.
        - Input length limits (500 chars)
        - Output token limits (300 tokens)
        """)
    
    st.title("Pre-Consultation Chatbot")
    # Main chat area
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown(f"Student: {st.session_state.student_id}")
    with col2:
        st.markdown('<div class="version-badge">Version B</div>', unsafe_allow_html=True)
    with col3:
       if st.button("Logout", key="logout_btn", width="stretch"):
            st.session_state.logged_in = False
            st.session_state.student_id = ""
            st.session_state.messages = []
            st.session_state.turns_used = 0
            st.rerun()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message (max 500 characters)...", max_chars=500):
        # Check if user has turns remaining
        if st.session_state.turns_used >= 50:
            st.error("You have reached the maximum number of conversation turns (50).")
        else:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Simulate assistant response
            with st.chat_message("assistant"):
                response = "AI will respond here (demo)."
                st.markdown(response)

            # Add assistant message
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Increment turn counter
            st.session_state.turns_used += 1

            st.rerun()


# Main app logic
if not st.session_state.logged_in:
    show_login_page()
else:
    show_chatbot_page()

