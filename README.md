# Expense Management System

The Expense Management System is a full-stack application designed to help users track, manage, and analyze their daily expenses. It features a Streamlit-based frontend for intuitive user interactions and a FastAPI backend that handles data storage and retrieval.

## Project Structure

- **backend/**: Contains backend services using FastAPI
- **frontend/**: Streamlit UI for user interaction
- **tests/**: Contains test cases for frontend and backend
- **requirements.txt**: Lists the Python dependencies
- **README.txt**: Text version of project info

## Setup Instructions

1. **Clone the Repository:**:
   ```bash
   git clone https://github.com/your-username/project-expense-tracker.git
   cd project-expense-tracker
   ```

1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
   
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server:app --reload
   ```
   
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
