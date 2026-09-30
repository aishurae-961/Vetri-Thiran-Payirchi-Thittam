# PocketSmart AI

PocketSmart AI is a smart budget and recommendation assistant developed using Generative AI.

## Project Description

PocketSmart AI helps users plan their budget for different activities and provides practical recommendations using Google Gemini AI.

The application provides personalized recommendations based on the user's budget and requirements.

## Features

- User Registration and Login
- Secure Password Hashing
- Home Planner
- Party Planner
- Jewelry Planner
- AI-powered Recommendations using Google Gemini
- Recommendation History
- Logout
- Responsive and User-friendly Interface

## Modules

### Home Planner
Users can enter:
- Budget
- Room Type
- Item
- Quantity

The system generates a practical recommendation based on the given budget.

### Party Planner
Users can enter:
- Budget
- Number of Guests
- Event Type
- Venue

The system provides suitable suggestions for food, decoration and arrangements.

### Jewelry Planner
Users can enter:
- Budget
- Occasion
- Style

The system provides a suitable jewelry recommendation using Generative AI.

## Technologies Used

- Python
- FastAPI
- HTML
- CSS
- Jinja2
- SQLite
- Google Gemini API
- Uvicorn
- Python-dotenv

## Project Structure

```text
PocketSmartAI/
│
├── main.py
├── models/
│   └── database.py
├── services/
│   └── gemini_utils.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── home.html
│   ├── party.html
│   ├── jewelry.html
│   └── history.html
├── static/
├── .gitignore
└── README.md
