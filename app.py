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

if __name__ == "__main__":
    app.run(debug=True)