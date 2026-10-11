from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cat")
def cat():
    return render_template(
        "cat.html",
        molly_name="Моллі",
        molly_age=7,
        molly_breed="мейн-кун",
        molly_weight="понад 10 кг",
        panya_name="Паня",
        panya_age=8,
        panya_breed="звичайна домашня кішка",
        panya_weight="понад 4 кг",
        panya_food="риба"
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)