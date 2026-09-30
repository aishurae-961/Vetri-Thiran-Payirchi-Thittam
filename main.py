from urllib import request

from fastapi import FastAPI, Request, Form
from httpx import request
from models.database import create_users_table
from models.database import create_history_table
from models.database import get_db
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.gemini_utils import generate_recommendation
from starlette.middleware.sessions import SessionMiddleware
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
pwd_hash = password_hash
app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key="pocketsmart-secret-key"
    )
create_users_table()
create_history_table()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    username = request.session.get("username")

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "username": username
        }
    )


@app.get("/home", response_class=HTMLResponse)
async def home_planner(request: Request):

    if "username" not in request.session:
        return HTMLResponse("""
            <h2>Please login first 🔐</h2>
            <a href="/login">Go to Login</a>
        """)

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


@app.post("/home", response_class=HTMLResponse)
async def home_budget(
    request: Request,
    budget: float = Form(...),
    room_type: str = Form(...),
    item: str = Form(...),
    quantity: int = Form(...)
):
    prompt = f"""
You are a smart home budget recommendation assistant.

User details:
Budget: ₹{budget}
Room Type: {room_type}
Item: {item}
Quantity: {quantity}

Give a practical recommendation based on the user's budget.
Suggest a suitable type or quality of the item and give a short reason.
Keep the answer simple and easy to understand.
"""

    recommendation = generate_recommendation(prompt)
    print("LOGGED USER:", request.session.get("username"))
    conn = get_db()
    conn.execute(
        """
        INSERT INTO history
        (username, planner_type, input_data, recommendation)
        VALUES (?, ?, ?, ?)
        """,
        (
            request.session.get("username"),
            "Home",
            f"Budget: ₹{budget}, Room: {room_type}, Item: {item}, Quantity: {quantity}",
            recommendation
        )
    )
    conn.commit()
    conn.close()
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "budget": budget,
            "room_type": room_type,
            "item": item,
            "quantity": quantity,
            "recommendation": recommendation
        }
    )


@app.get("/party", response_class=HTMLResponse)
async def party_planner(request: Request):

    if "username" not in request.session:
        return HTMLResponse("""
            <h2>Please login first 🔐</h2>
            <a href="/login">Go to Login</a>
        """)

    return templates.TemplateResponse(
        request=request,
        name="party.html",
        context={}
    )
@app.post("/party", response_class=HTMLResponse)
async def party_budget(
    request: Request,
    budget: float = Form(...),
    guests: int = Form(...),
    event_type: str = Form(...),
    venue: str = Form(...)
):
    prompt = f"""
You are a smart party budget recommendation assistant.

User details:
Budget: ₹{budget}
Number of Guests: {guests}
Event Type: {event_type}
Venue: {venue}

Give a practical party planning recommendation based on the user's budget.
Suggest suitable food, decoration and basic arrangements.
Make sure the suggestions are reasonable for the number of guests and budget.
Keep the answer simple and easy to understand.
"""

    recommendation = generate_recommendation(prompt)
    conn = get_db()

    conn.execute(
        """
        INSERT INTO history
        (username, planner_type, input_data, recommendation)
        VALUES (?, ?, ?, ?)
        """,
        (
            request.session.get("username"),
            "Party",
            f"Budget: ₹{budget}, Guests: {guests}, Event: {event_type}, Venue: {venue}",
            recommendation
        )
    )

    conn.commit()
    conn.close()

    return templates.TemplateResponse(
        request=request,
        name="party.html",
        context={
            "budget": budget,
            "guests": guests,
            "event_type": event_type,
            "venue": venue,
            "recommendation": recommendation
        }
    )
    
@app.get("/jewelry", response_class=HTMLResponse)
async def jewelry_planner(request: Request):

    if "username" not in request.session:
        return HTMLResponse("""
            <h2>Please login first 🔐</h2>
            <a href="/login">Go to Login</a>
        """)

    return templates.TemplateResponse(
        request=request,
        name="jewelry.html",
        context={}
    )


@app.post("/jewelry", response_class=HTMLResponse)
async def jewelry_budget(
    request: Request,
    budget: float = Form(...),
    occasion: str = Form(...),
    style: str = Form(...)
):
    prompt = f"""
You are a smart jewelry budget recommendation assistant.

User details:
Budget: ₹{budget}
Occasion: {occasion}
Style: {style}

Give a practical jewelry recommendation based on the user's budget,
occasion and preferred style.

Suggest a suitable type of jewelry and briefly explain why it is suitable.
Keep the answer simple and easy to understand.
"""

    recommendation = generate_recommendation(prompt)
    conn = get_db()

    conn.execute(
        """
        INSERT INTO history
        (username, planner_type, input_data, recommendation)
        VALUES (?, ?, ?, ?)
        """,
        (
            request.session.get("username"),
            "Jewelry",
            f"Budget: ₹{budget}, Occasion: {occasion}, Style: {style}",
            recommendation
        )
    )

    conn.commit()
    conn.close()

    return templates.TemplateResponse(
        request=request,
        name="jewelry.html",
        context={
            "budget": budget,
            "occasion": occasion,
            "style": style,
            "recommendation": recommendation
        }
    )
from services.gemini_utils import generate_recommendation

@app.get("/test-ai")
async def test_ai():
    result = generate_recommendation(
        "Give me one short budget saving tip for a student."
    )
    return {"gemini_response": result}
@app.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="signup.html",
        context={}
    )


@app.post("/signup", response_class=HTMLResponse)
async def signup(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    conn = get_db()

    try:
        hashed_password = pwd_hash.hash(password)
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password)
        )
        conn.commit()
        message = "Account created successfully!"
    except Exception:
        message = "Username already exists."

    conn.close()

    return HTMLResponse(f"""
        <h2>{message}</h2>
        <a href="/login">Go to Login</a>
    """)
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


@app.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    conn = get_db()

    user = conn.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    if user:
        stored_password = user["password"]

        try:
            valid_password = password_hash.verify(
                password,
                stored_password
            )
        except Exception:
            valid_password = False

        # Old plain-text password account
        if not valid_password and stored_password == password:
            new_hash = password_hash.hash(password)

            conn.execute(
                "UPDATE users SET password = ? WHERE username = ?",
                (new_hash, username)
            )

            conn.commit()
            valid_password = True

        if valid_password:
            request.session["username"] = username
            message = "Login successful! 🎉"
        else:
            message = "Invalid username or password."
    else:
        message = "Invalid username or password."

    conn.close()

    return HTMLResponse(f"""
        <h2>{message}</h2>
        <a href="/">Go to Home</a>
    """)

    return HTMLResponse("""
        <h2>Invalid username or password ❌</h2>
        <a href="/login">Try Again</a>
    """)
@app.get("/history", response_class=HTMLResponse)
async def history_page(request: Request):

    username = request.session.get("username")

    if not username:
        return HTMLResponse("""
            <h2>Please login first 🔐</h2>
            <a href="/login">Go to Login</a>
        """)

    conn = get_db()

    history = conn.execute(
        "SELECT * FROM history WHERE username = ? ORDER BY id DESC",
        (username,)
    ).fetchall()

    conn.close()

    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={
            "history": history
        }
    )
@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    request.session.clear()

    return HTMLResponse("""
        <h2>Logged out successfully! 👋</h2>
        <a href="/">Go to Home</a>
    """)