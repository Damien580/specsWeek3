from flask import Flask, render_template, redirect, flash, request, session
import jinja2
import melons
from forms import LoginForm
import customers


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
    if "username" not in session:
        return redirect("/login")
    
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

@app.route("/empty-cart")
def empty_cart():
    session["cart"] = {} #this empties the cart by rewriting the session with an empty dictionary.
    
    return redirect("/cart") #this reloads the cart page after emptying the cart.

@app.route("/login", methods=["GET", "POST"]) #creates an endpoint for the login page
def login():
    form = LoginForm(request.form) #sets the form variable.
    
    if form.validate_on_submit():  #requests the form data from the login.
        username = form.username.data
        password = form.password.data
        
        user = customers.get_by_username(username) #checks to see if registered user exists in the customer list and if passwrod matches user info.
        
        if not user or user["password"] != password: #if user does not exist or password is incorrect, displays error message and redirects to login page.
            flash("Invalid Username or Password!")
            return redirect("/login")
        
        session["username"] = user["username"] #assigns token to session under username for access if logged in.
        flash("Logged In!")
        return redirect("/melons") #redirects to all_melons page when logged in.
        
    return render_template("login.html", form=form) #reloads page if form not submitted or data invalid

@app.route("/logout") #endpoint for logout page
def logout(): #function to log out
    del session["username"] #deletes session token for the user
    flash("logged Out!")
    return redirect("/login") #redirects to login page when logged out.

@app.errorhandler(404) #.errorhandler creates an endpoint for an error code.
def error_404(e): #function that renders the html template for the error
    return render_template("404.html")






if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")