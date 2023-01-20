from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/cupcakes')
def cupcakes():
    return render_template('cupcakes.html')


@app.route('/view_cupcake')
def view_cupcake():
    return render_template('view_cupcake.html')

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost") 



