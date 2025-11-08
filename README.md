# Pre-Consultation Chatbot - Streamlit Replica

This is a Streamlit replica of the Pre-Consultation Chatbot interface for CS3249 Assignment 2. I did NOT design the chatbot. The teaching team designed the actual chatbot. I used AI to replicate the design so that my user participants can try it to get a feel without using the actual chatbot.


## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file by copying the example:
```bash
cp .env.example .env
```

3. Edit the `.env` file and set your valid student ID:
```
VALID_STUDENT_ID=A1234567Q
```

**⚠️ IMPORTANT:** Never commit the `.env` file to Git! It's already in `.gitignore`.

## Running the Application

Run the Streamlit app with:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Security (Written by AI)

This application uses environment variables to protect sensitive information:
- **`.env`** - Contains your actual secrets (NOT committed to Git)
- **`.env.example`** - Template showing what variables are needed (safe to commit)
- **`.gitignore`** - Ensures `.env` is never committed to the repository

This allows you to safely publish the code to public repositories without exposing credentials.