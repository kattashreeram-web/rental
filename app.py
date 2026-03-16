from flask import Flask, render_template, request

app = Flask(__name__)

cars = [
    {"name": "Hyundai i20", "price": "₹1999/day"},
    {"name": "Volkswagen Polo", "price": "₹1999/day"},
    {"name": "Maruti Swift", "price": "₹999/day"},
    {"name": "Baleno", "price": "₹999/day"},
    {"name": "Ertiga (7 Seater)", "price": "₹1499/day"}  
]

@app.route('/')
def home():
    return render_template("index.html", cars=cars)

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    car = request.form['car']
    return f"Booking Confirmed! {name} booked {car}"

if __name__ == '__main__':
    app.run(debug=True)
