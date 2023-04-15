from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Seoul, Korea',
    'salary': '60,000,000 Won'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Busan, Korea',
    'salary': '50,000,000 Won'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '50,000,000 Won'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'SF, USA',
    'salary': '$ 100,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS,
                        company_name='Happy JW')

# Use /api to differentiate files are not html 
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  