# Pre-Consultation Chatbot - Streamlit Replica

This is a Streamlit replica of the Pre-Consultation Chatbot interface for CS3249 Assignment 2. I did NOT design the chatbot. The teaching team did and I used AI to replicate the design so that my user participants can try it to get a feel without using the actual chatbot.

## Features

- Student login interface
- Version indicator (Version B)
- Student ID input with character counter
- Input validation for student ID format
- Expandable instructions section
- Responsive design with custom styling

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Run the Streamlit app with:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Student ID Format

The expected format for student ID is: **A0123456X**
- Must start with 'A'
- Followed by 7 digits
- Ends with a letter or digit
- Total length: 9 characters
