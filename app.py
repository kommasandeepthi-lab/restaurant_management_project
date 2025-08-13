from flask import Flask, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

def init_cart():
    if "cart" not in session:
        session["cart"] = []

@app.route("/")
def homepage():
    init_cart()
    cart_count = len(session["cart"])
    return redirect(url_for("homepage"))

@app.route("/clear_cart")
def clear_cart():
    session.pop("cart", None)
    return redirect(url_for("homepage"))

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/about")
def about_page():
    restaurant_info = {
        "name": "The Gourmet Table",
        "history": "Founded in 1995, our restaurant began as a small family-owned eatery serving homemade recipes passed down for generations.",
        "mission": "To bring people together over delicious, freshly prepared meals made with locally sourced ingredients."
    }
    return render_template("about.html", info=restaurant_info)

if __name__ == "__main__":
    app.run(debug=True)