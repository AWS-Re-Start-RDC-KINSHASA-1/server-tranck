from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Remplacer les valeurs par défaut
        if username == "tracy" and password == "1234":
            return redirect(url_for("home"))
        else:
            return render_template("error.html")
    return render_template("login.html")

@app.route("/home")
def home():
    return "<h1>Bienvenue sur la page d'accueil</h1>"

@app.route("/logout")
def logout():
    # Déconnectez l'utilisateur (supprimez les informations de session, etc.)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
