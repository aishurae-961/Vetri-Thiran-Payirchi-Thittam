# PocketSmart AI – Project Details

## 1. Project Title

PocketSmart AI: Your Smart Budget & Recommendation Assistant

## 2. Project Overview

PocketSmart AI is a Generative AI-based budget and recommendation assistant.

The system helps users make practical budget-based decisions for different needs such as:

- Home Interior Planning
- Party Planning
- Jewelry Selection

The application uses Google Gemini AI to analyze user inputs and generate personalized recommendations.

## 3. Problem Statement

Choosing suitable products and services within a limited budget can be difficult because of the large number of choices and different price ranges.

PocketSmart AI solves this problem by understanding the user's budget, preferences and requirements and providing suitable AI-generated recommendations.

## 4. Objectives

- Provide personalized budget-based recommendations.
- Help users plan expenses effectively.
- Generate practical recommendations using Generative AI.
- Support multiple planning categories.
- Store previous recommendations for future reference.
- Provide a simple and user-friendly interface.

## 5. Main Modules

### Home Planner

The user provides:

- Budget
- Room Type
- Item
- Quantity

The AI generates a suitable recommendation based on the available budget and requirements.

### Party Planner

The user provides:

- Budget
- Number of Guests
- Event Type
- Venue

The AI provides suggestions for food, decoration and other basic arrangements.

### Jewelry Planner

The user provides:

- Budget
- Occasion
- Style

The AI recommends suitable jewelry based on the user's budget, occasion and preferred style.

## 6. AI Integration

Google Gemini API is integrated into the application through a dedicated Gemini utility service.

The AI receives the user's requirements through carefully designed prompts and generates practical recommendations.

## 7. Technology Stack

### Backend
- Python
- FastAPI
- Uvicorn

### Frontend
- HTML
- CSS
- Jinja2 Templates

### Database
- SQLite

### AI
- Google Gemini API

### Security and Configuration
- python-dotenv
- Password hashing
- Session management

## 8. Project Architecture

```text
PocketSmartAI/
│
├── main.py
│
├── models/
│   └── database.py
│
├── services/
│   └── gemini_utils.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── home.html
│   ├── party.html
│   ├── jewelry.html
│   └── history.html
│
├── static/
│
├── .gitignore
├── README.md
└── PROJECT_DETAILS.md
