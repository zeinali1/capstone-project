# EventEase – Online Event Management System

## 📘 Project Overview
EventEase is a modern web-based event management system built with Django.  
It allows users to **create, browse, join, and manage events** easily.  
Visitors can explore upcoming events, while registered users can host, edit, and participate in events.

---

## 🧩 Features & User Stories

### 👥 As a Visitor (Not Logged In)
- View a list of all upcoming public events.  
- Register for an account using email and password.  
- Log in to access personalized event features.

### 🙋‍♀️ As a Registered User
- View all available events on the homepage.  
- Search for events by **name, date, or location**.  
- View detailed event pages (title, description, date, location, and attendees).  
- Join or leave events easily with one click.  
- View all joined events in one place.  
- Create new events with details like title, date, and location.  
- Edit or delete only events they created.

### 🧑‍💼 As an Event Creator
- See how many people joined each of their events.  
- Update or cancel events they created.  
- Maintain accurate event information for attendees.

### 🔐 As a System (Authentication)
- Restrict event creation/joining to logged-in users.  
- Ensure users can only modify or delete their own events.

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | Django 5.x |
| **Frontend** | HTML5, CSS3, Django Templates |
| **Database** | PostgreSQL |
| **Auth System** | Django Authentication |
| **Language** | Python 3.12+ |
| **Hosting (Optional)** | Render |

---

## 🗂️ Data Model (ERD Overview)

**Entities:**
- **User** (Django default user model)
- **Event**
  - title
  - description
  - location
  - event_date
  - created_by → User
- **Registration**
  - user → User
  - event → Event
  - registered_at (timestamp)

**Relationships:**
- One **User** can create many **Events**.
- Many **Users** can join many **Events** (via **Registration**).

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/eventease.git
cd eventease
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv eventease-venv
source eventease-venv/bin/activate  # (Windows: eventease-venv\Scripts\activate)
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL
Create a database in **pgAdmin 4** (e.g., `eventease_db`),  
then update `settings.py` → `DATABASES` section with your credentials.

### 5️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server
```bash
python manage.py runserver
```

Access the app at: **http://127.0.0.1:8000/**

---

## 🧭 Folder Structure

```
eventease/
│
├── eventease/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── events/                 # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── events/
|   |   └── registration/
│   └── static/css/
│       └── style.css
│
├── manage.py
└── README.md
```

---

## 🚀 Challenges & Solutions

| Challenge | Solution |
|------------|-----------|
| Implementing event join/leave logic | Used a `Registration` model to handle M2M relationships manually |
| Restricting edit/delete to event creators | Implemented `UserPassesTestMixin` and request-user validation |
| Displaying attendee count | Aggregated registrations per event in templates |
| Filtering upcoming vs past events | Used `timezone.now()` comparison in the view |
| Search feature | Implemented `icontains` filters on title, location, and date |

---

## 🧭 Future Improvements / Stretch Goals

- **Event Reminders & Notifications** – Send users email or in-app reminders before events.  
- **User Profiles** – Let users manage profiles and view event history.  
- **RSVP Comments / Chat** – Enable attendee interaction within events.    
- **Map Integration** – Display event locations using Google Maps or Leaflet.  
- **Dark Mode** – Add a theme switch for better UX.  
- **Pagination / Infinite Scroll** – Handle large event lists efficiently.  
- **Admin Dashboard** – Provide analytics and management tools.  
- **Mobile Optimization** – Fully responsive design for all devices.  

---

## 🏁 Summary
EventEase delivers a clean and intuitive event management experience with secure authentication, flexible participation, and full CRUD event control.  
It’s a simple yet powerful foundation for real-world event platforms.
