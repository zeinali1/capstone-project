# 🎉 Event Management Web App

A Django-based web application for creating, managing, and joining events.  
Users can browse upcoming and past events, search by title or location, and manage their own events with a clean, responsive interface.

---

## 🚀 Features

✅ **User Authentication** – Login, logout, and access control for event interactions.  
✅ **Create & Manage Events** – Registered users can create, edit, and delete their own events.  
✅ **Join or Leave Events** – Users can RSVP to attend or leave any public event.  
✅ **Search & Filter** – Search events by **title, location, or date** directly from the homepage.  
✅ **Upcoming & Past Events** – Automatically separate events based on date and time.  
✅ **Responsive Design** – Styled with `style.css` and `base.html` for a clean modern layout.  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS (custom `style.css`) |
| **Backend** | Django (Python) |
| **Database** | SQLite (default) |
| **Templating** | Django Template Language |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```
event_management/
│
├── events/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── event_detail.html
│   │   ├── event_form.html
│   │   └── event_confirm_delete.html
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
│
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/event-management.git
   cd event-management
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # (or venv\Scripts\activate on Windows)
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Open in browser**

   ```
   http://127.0.0.1:8000/
   ```

---

## 💡 Usage

- **Create Account / Login** to add or join events.  
- **Search** for events by typing part of the title or location in the search bar.  
- **Filter by Date** using the date picker beside the search box.  
- **Join or Leave Events** directly from the homepage.  
- **Edit / Delete** your own created events.  
- **View Details** by clicking on an event title.

---

## 🧭 Future Improvements / Stretch Goals

- **Event Reminders & Notifications** – Send users email or in-app reminders before events.  
- **User Profiles** – Let users manage profiles and view event history.  
- **RSVP Comments / Chat** – Enable attendee interaction within events.  
- **Event Categories** – Filter events by tags (e.g., Workshop, Meetup, Conference).  
- **Map Integration** – Display event locations using Google Maps or Leaflet.  
- **Dark Mode** – Add a theme switch for better UX.  
- **Pagination / Infinite Scroll** – Handle large event lists efficiently.  
- **Admin Dashboard** – Provide analytics and management tools.  
- **Mobile Optimization** – Fully responsive design for all devices.  

---
