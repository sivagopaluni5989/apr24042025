from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    heroes = [
        {
            "title": "Late.",
            "name": "Subba Rao",
            "image": "subba_rao.jpg",
            "History": ["DOB", "SPOUSE", "CHILDRENS"]
        },
        {
            "title": "Mr.",
            "name": "Radha Krishna Murthy",
            "image": "radha_krishna.jpg",
            "History": ["DOB", "SPOUSE", "CHILDRENS"]
        },  # <--- this comma was missing
        {
            "name": "Raghu Kumar",
            "title": "Late Sri.",
            "image": "raghukumar.jpg",
            "History": ["DOB", "SPOUSE", "CHILDRENS"]
        },
        {
            "name": "Girija",
            "title": "Srimathi",
            "image": "girija.jpg",
            "History": ["DOB", "SPOUSE", "CHILDRENS"]
        },
        {
            "name": "Krishnamma",
            "title": "Srimathi",
            "image": "krishnamma.jpg",
            "History": ["DOB", "SPOUSE", "CHILDRENS"]
        },
        {
            "name": "Maheswari",
            "title": "Srimathi",
            "image": "maheswari.jpg",
            "History": ["DOB", "SPOUSE", "CHILDRENS"]
        }
    ]
    return render_template('index.html', heroes=heroes)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

