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

## Running the Application Locally

Run the Streamlit app with:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Deploying to Streamlit Community Cloud

When deploying to Streamlit Community Cloud, you **cannot** use the `.env` file. Instead, use **Streamlit Secrets**:

### Steps:

1. **Push your code to GitHub** (the `.env` file will NOT be committed due to `.gitignore`)

2. **Go to Streamlit Community Cloud** (https://share.streamlit.io/)

3. **Deploy your app** from your GitHub repository

4. **Add Secrets** in the Streamlit Cloud dashboard:
   - Click on your app
   - Go to **Settings** → **Secrets**
   - Add the following in TOML format:
   ```toml
   VALID_STUDENT_ID = "A1234567Q"
   ```
   - Click **Save**

5. Your app will automatically restart with the secrets loaded!

### How it Works:

- **Locally**: The app reads from `.env` file using `python-dotenv`
- **Streamlit Cloud**: The app reads from `st.secrets` (environment variables)
- Both methods use `os.getenv()` which works in both environments automatically

The code is already set up to handle both scenarios! ✨

## Security (Written by AI)

This application uses environment variables to protect sensitive information:

### For Local Development:
- **`.env`** - Contains your actual secrets (NOT committed to Git)
- **`.env.example`** - Template showing what variables are needed (safe to commit)
- **`.gitignore`** - Ensures `.env` is never committed to the repository

### For Streamlit Community Cloud:
- **Streamlit Secrets** - Configured in the app's dashboard settings
- Secrets are stored securely and never exposed in your public repository
- Access via Settings → Secrets in your deployed app

This allows you to safely publish the code to public repositories without exposing credentials, while still being able to deploy to the cloud! 🔒