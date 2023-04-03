from flask import Flask, render_template, redirect, flash, request
import jinja2

app = Flask(__name__)
app.jinja_env.undefined = jinja2.StrictUndefined #for debugging purposes

@app.route("/") #the route for the homepage
def homepage():
    return render_template("base.html")

@app.route("/melons") #the route to get to all melons
def all_melons():
    return render_template("all_melons.html")

@app.route("/melon/<melon_id>")
def melon_details(melon_id): #returns a page that displays a melons info, and an add to cart button.
    return render_template("melon_details.html")

@app.route("/add_to_cart<melon_id>")
def add_to_cart(melon_id): #add a melon to the cart.
    return f"{melon_id} has been added to your cart."

@app.route("/cart")
def cart():
    return render_template("cart.html")


if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")