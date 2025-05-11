from flask import Flask, render_template, request
from stalkcompetitor.crew import build_crew

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    if request.method == "POST":
        company = request.form.get("company")
        crew = build_crew()
        result = crew.kickoff(inputs={"company_name": company})
        report = result
    return render_template("index.html", report=report)

if __name__ == "__main__":
    app.run(debug=True)
