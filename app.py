from flask import Flask, render_template, jsonify
from database import load_jobs

app = Flask(__name__)


@app.route('/')
def index():
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs, company_name='MyCaptain')


@app.route('/api/jobs')
def jobs():
    return jsonify(load_jobs())


if __name__ == "__main__":
    app.run(debug=True)
