from flask import Flask, render_template, redirect, flash, request, session
import jinja2
import melons


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = jinja2.StrictUndefined #for debugging purposes

@app.route("/") #the route for the homepage
def homepage():
    return render_template("base.html")

@app.route("/melons") #the route to get to all melons
def all_melons():
    melon_list = melons.get_melons()
   
    return render_template("all_melons.html", melon_list = melon_list)

@app.route("/melon/<melon_id>")
def melon_details(melon_id): #returns a page that displays a melons info, and an add to cart button.
    melon = melons.get_by_id(melon_id)
    return render_template("melon_details.html", melon = melon)

@app.route("/add_to_cart<melon_id>")
def add_to_cart(melon_id): #function adds a melon to the cart.
    if "cart" not in session: #this initiates the session if not already running.
        session["cart"] = {}
    cart = session["cart"]
    cart[melon_id] = cart.get(melon_id, 0) + 1 #this line increases the total num of melons in the cart each time one is added.
    session.modified = True #makes sure the sessions updates correctly.
    flash(f"Melon {melon_id} added to cart.") 
    print(cart)
    
    return redirect("/cart")

@app.route("/cart")
def cart():
    order_total = 0
    cart_melons = []
    
    cart = session.get("cart", {}) #get cart dictionary from session or an empty one if doesnt exist yet.
    
    for melon_id, quantity in cart.items(): #loops through items in cart looking for melon_id and the quantity of each melon.
        melon = melons.get_by_id(melon_id) #calls func to get each mellon by id.
        
        total_cost = quantity * melon.price #calculates total cost of each type of melons.
        order_total += total_cost #add melon total to cart total
        
        melon.quantity = quantity # add quantity as an attribute of the Melon object.
        melon.total_cost = total_cost # add total_cost as an attribute of Melon object.
        
        cart_melons.append(melon) #appends the cart.csv with each melon addition.
        
    return render_template("cart.html", cart_melons=cart_melons, order_total=order_total) #displays appended cart page information.




if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")