from flask import Flask, render_template, request, redirect
from scraper import get_sydney_events

app = Flask(__name__)
emails = []

@app.route('/')
def index():
    events = get_sydney_events()
    return render_template('index.html', events=events)

@app.route('/get_tickets', methods=['POST'])
def get_tickets():
    email = request.form.get('email')
    event_link = request.form.get('event_link')
    if email:
        with open("emails.txt", "a") as f:
            f.write(email + "\n")
    return redirect(event_link)

if __name__ == '__main__':
    app.run(debug=True)
