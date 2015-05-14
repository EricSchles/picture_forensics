from flask import request, render_template, Flask

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == 'POST':
        test = request.form.get("test")
        print test
        return render_template("test.html")
    return render_template("test.html")

app.run(debug=True)
