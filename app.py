from flask import Flask, render_template, jsonify
#idk
app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Software Engineer",
    "company": "ABC Corporation",
    "location": "New York",
}, {
    "id": 2,
    "title": "Data Scientist",
    "company": "XYZ Inc.",
    "location": "San Francisco",
}, {
    "id": 3,
    "title": "Marketing",
    "company": "JHG Corporation",
    "location": "DELHI",
}, {
    "id": 4,
    "title": "Sales",
    "company": "DEF Corporation",
    "location": "Boston",
}]


@app.route('/')
def index():
    return render_template('index.html', jobs=JOBS, company_name='MyCaptain')


@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
