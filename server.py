from flask import Flask, render_template, url_for, redirect
from cupcakes import read_cupcake_file, find_a_cupcake, add_to_order, view_a_cupcake

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/orders')
def orders():
    return render_template('orders.html', cupcakes = read_cupcake_file("orders.csv"))

@app.route('/cupcakes')
def cupcakes():
    return render_template('cupcakes.html', cupcakes = read_cupcake_file("display.csv"))

@app.route('/view_cupcake/<name>')
def view_cupcake(name):
    cupcake = find_a_cupcake("display.csv", name)

    if cupcake:
        view_a_cupcake("view.csv", cupcake)
        return render_template('view_cupcake.html', cupcake = read_cupcake_file("view.csv"))

    else:
        "Sorry! That cupcake was not found!"

@app.route('/add_cupcake/<name>')
def add_cupcake(name):
    cupcake = find_a_cupcake("display.csv", name)
    
    if cupcake:
        add_to_order("orders.csv", cupcake)
        return redirect(url_for("orders"))

    else:
        "Sorry! That cupcake was not found!"


if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost") 



