import random

from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "GET":
       cookie = request.cookies.get("secret_number")
       response = make_response(render_template("index.html", cookie=cookie))
       if not cookie:
           secret_number = random.randint(1,30)
           response.set_cookie("secret_number", str(secret_number))
       return response
    elif request.method == "POST":
        number = request.form.get(str("number"))
        secret_number = request.cookies.get("secret_number")
        if number == secret_number:
            message = "Bravo pogodio si broj"
            response = make_response(render_template("čestitka.html", message=message))
            response.set_cookie("secret_number", str(random.randint(1,30)))
            return response
        elif number < secret_number:
            message = "Probaj s većim brojem"
            return render_template("rezultat.html", message=message)
        elif number > secret_number:
            message = "Probaj s manjim brojem"
            return render_template("rezultat.html", message=message)
if __name__ == "__main__":
    app.run(use_reloader=True)