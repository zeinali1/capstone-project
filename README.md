# 🎟️ EventEase

## 🧩 Project Overview and Description

**EventEase** is a web-based event management platform built with Django.  
It allows users to **create, view, search, and join events** while keeping track of upcoming and past activities.  
EventEase simplifies event organization and participation through a clean interface, user authentication, and registration tracking.

### Core Features
- User registration, login, and logout
- Event creation with date picker
- Upcoming and past event categorization
- Join or leave events (except those you created)
- Search events by **title** or **date**
- View attendee count for each event
- Admin panel for managing users and events

---

## 🛠️ Tech Stack

| Category | Technology Used |
|-----------|----------------|
| **Backend Framework** | Django (Python) |
| **Frontend** | HTML, CSS |
| **Database** | PostgreSQL |
| **Authentication** | Django's built-in User model |
| **Environment** | Virtualenv |
| **Admin Interface** | Django Admin |

---

## 🧱 ERD Diagram

The following Entity Relationship Diagram (ERD) represents the core database design:

User (Django default)
│
├──< Event
│ ├── id (PK)
│ ├── title
│ ├── description
│ ├── event_date
│ ├── created_by (FK → User)
│ ├── created_at
│
└──< Registration
├── id (PK)
├── user (FK → User)
├── event (FK → Event)
├── timestamp


**Relationships:**
- A **User** can create many **Events**.
- A **User** can join multiple **Events**.
- Each **Registration** links one user to one event.

---

## ⚙️ Installation Guide

Follow these steps to set up and run the project locally.

### 1. Clone the Repository
```bash
git clone https://git.generalassemb.ly/zeinali/capstone-project
cd capstone-project

2. Create and Activate a Virtual Environment

Windows

python -m venv eventease-venv
eventease-venv\Scripts\activate


Mac/Linux

python3 -m venv eventease-venv
source eventease-venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure the Database

Create a PostgreSQL database called eventease_db using pgAdmin 4 or psql.

Update the DATABASES section in your settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eventease_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

6. Create a Superuser
python manage.py createsuperuser

7. Run the Server
python manage.py runserver


Then visit: http://127.0.0.1:8000/

👥 User Stories & Features
As a User, I can:

Register for an account.

Log in and log out securely.

Browse all upcoming and past events.

Search for events by title or date.

Join or cancel registration for events I didn’t create.

View how many attendees are registered for each event.

As an Organizer, I can:

Create new events using a date picker.

Edit or delete my events.

Automatically see that I’m the creator (cannot join my own event).

Track registrations to my events.

🔍 Search & Filter

Users can search events directly from the home page:

Search by title keyword (case-insensitive)

Filter by event date

Example search usage:

Type “Hackathon” → filters all events with “Hackathon” in title

Select a specific date → shows only events happening on that day

🧩 Optional Improvements

Future enhancements could include:

Event images or banners

Pagination for large event lists

Email or in-app notifications for new registrations

RSVP limits and waitlists

Google Calendar integration

REST API endpoints for mobile integration

⚠️ Challenges & Solutions
Challenge	Solution
TemplateSyntaxError for checking joined events	Moved logic into the view instead of the template
Logout not working	Updated base.html to include correct URL name and form method
Event creator joining their own event	Added condition in home view to hide “Join” button for event creator
Missing search functionality	Implemented q and date query filters in the view
Styling inconsistencies	Rebuilt base.html and style.css with a clean, consistent layout

🧭 File Structure
eventease/
│
├── events/                     # Main app
│   ├── models.py               # Event & Registration models
│   ├── views.py                # FBVs and CBVs
│   ├── templates/events/       # HTML templates
│   │   ├── home.html
│   │   ├── event_form.html
│   │   ├── my_registrations.html
│   │   └── base.html
│   ├── forms.py                # EventForm
│   ├── urls.py                 # App routes
│
├── static/css/style.css        # Styling
├── eventease/settings.py       # Django settings
├── manage.py
└── README.md                   # Project documentation

🧑‍💻 Admin Panel Access

Visit: http://127.0.0.1:8000/admin

Login using the superuser credentials created earlier.

🏁 Conclusion

EventEase provides a simple yet efficient system for managing and participating in events.
It demonstrates core Django functionality such as authentication, CRUD operations, and relational data modeling — making it an ideal base for expanding into a full-featured event management platform.