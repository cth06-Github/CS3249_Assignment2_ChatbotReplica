import streamlit as st
import random

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
    /* Main title styling */
    h1 {
        color: #1f1f1f;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
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
        
    /* Input label styling */
    .stTextInput label {
        font-weight: 500;
        color: #424242;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background-color: white;
        color: #424242;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 0.75rem;
        font-weight: 500;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #f5f5f5;
        border-color: #bdbdbd;
    }
    
    /* Character counter styling */
    .char-counter {
        text-align: right;
        font-size: 0.85rem;
        color: #757575;
        margin-top: -0.5rem;
        margin-bottom: 1rem;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        font-weight: 500;
    }
    
    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #f5f5f5;
    }
    
    /* Chat input styling */
    .stChatInput {
        border-radius: 8px;
    }
    
    /* Header bar styling */
    .header-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
    }
    
    .student-info {
        font-size: 1rem;
        color: #424242;
    }
    
    /* Logout button styling */
    .logout-btn button {
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        padding: 0.5rem 2rem !important;
        width: auto !important;
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
def show_login_page():
    # Header section
    st.markdown("<h1>Pre-Consultation Chatbot</h1>", unsafe_allow_html=True)
    st.markdown('<div class="version-badge">Version: Version B</div>', unsafe_allow_html=True)

    # Add horizontal line
    st.markdown("---")

    # Main content
    st.markdown("## Student Login")

    # Info message
    st.info("Please log in with your student ID to access the mental health pre-consultation chatbot.")

    login_container = st.container(border=True)
    
    with login_container:
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

        st.markdown(f'<div class="char-counter">{char_count}/9</div>', unsafe_allow_html=True)

        # Login button
        if st.button("Login", type="secondary", use_container_width=True):
            if not student_id:
                st.warning("Please enter your student ID")
                return
            if not isValidStudentID(student_id):
                st.error("Invalid student ID format. Please use format like: A0123456X")
                return
            if student_id != "A1234567Q":
                st.error("Invalid student ID")
                return
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
        st.markdown("### 📊 Usage Statistics")
        st.markdown("**Turns Used**")
        st.markdown(f"## {st.session_state.turns_used}/50")
        st.markdown("**Remaining**")
        st.markdown(f"## {50 - st.session_state.turns_used}")
        
        st.markdown("---")
        
        st.markdown(f"**Session ID:** {st.session_state.session_id}")
        
        st.markdown("---")
        
        st.markdown("### ⚙️ Settings")
        st.session_state.include_history = st.toggle(
            "Include conversation history",
            value=st.session_state.include_history,
            help="Include previous messages in the conversation context"
        )
        
        if st.button("Reset conversation", use_container_width=True):
            st.session_state.messages = []
            st.session_state.turns_used = 0
            st.rerun()
        
        st.markdown("---")
        
        st.markdown("### ⚠️ Important")
        st.markdown("""
        - This is for Assignment 2 research only
        - After refreshing the page, you need to log in again.
        - Please allocate the quota reasonably for each participant.
        - You can close the left sidebar during the experiment.
        - Input length limits (500 chars)
        - Output token limits (300 tokens)
        """)
    
    # Main chat area
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown(f"<h1>Pre-Consultation Chatbot</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='padding-top: 1rem;'><span class='student-info'><strong>Student:</strong> {st.session_state.student_id}</span></div>", unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="version-badge" style="margin-top: 1rem;">Version: Version B</div>', unsafe_allow_html=True)
    
    # Logout button in top right
    cols = st.columns([6, 1])
    with cols[1]:
        if st.button("Logout", key="logout_btn"):
            st.session_state.logged_in = False
            st.session_state.student_id = ""
            st.session_state.messages = []
            st.session_state.turns_used = 0
            st.rerun()
    
    st.markdown("---")
    
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
            
            # Increment turn counter
            st.session_state.turns_used += 1
            
            # Simulate assistant response
            with st.chat_message("assistant"):
                response = "Thank you for sharing. This is a simulated response. In a real implementation, this would connect to an AI model to provide mental health support and guidance."
                st.markdown(response)
            
            # Add assistant message
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            st.rerun()


# Main app logic
if not st.session_state.logged_in:
    show_login_page()
else:
    show_chatbot_page()

