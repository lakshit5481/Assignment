# Assignment
#  Sydney Events Web App

Welcome! This is a simple web application that shows all the current and upcoming events happening in **Sydney, Australia**.  
The app pulls data from external event websites and presents them in a clean, easy-to-use interface.

---

##  What This App Does

- Automatically fetches the latest events happening in Sydney
- Displays them beautifully in a minimal and clean layout
- Lets users click a **"GET TICKETS"** button
- Before redirecting to the official ticket page, it asks for the user's email for opt-in
- The event list updates regularly, so it's always fresh!

---

## 🧱 Project Structure

sydney_events/
├── app.py # The main Flask app
├── scraper.py # Python script that scrapes event data
├── requirements.txt # List of required Python packages
└── templates/
└── index.html # The HTML page shown to users
