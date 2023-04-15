from flask import Flask, render_template, request
from models.events_model import db, Event
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///events.db"
db.init_app(app)
@app.route('/')
def home():
    events = db.session.execute(db.select(Event).order_by(Event.name)).scalars()
    return render_template('index.html', events=events)

@app.route('/addevent', methods=['POST', 'GET'])
def add_event():
    if request.method == 'POST':
        event = Event(
            name=request.form['event_name'],
            category=request.form['event_category'],
            date=date.fromisoformat(request.form['event_date'])
        )
        db.session.add(event)
        db.session.commit()
        return render_template('add_event.html')
    else:
        return render_template('add_event.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
