from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        email = request.form['email']
        password = request.form['password']

        email_check = (email[0] == (email[0]).capitalize())
        pass_check = re.match("(([a-zA-Z]+[0-9]+)|([0-9]+[a-zA-Z]+))[a-zA-Z0-9]*", password)

        if email_check and pass_check:
            return render_template("success.html")
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)