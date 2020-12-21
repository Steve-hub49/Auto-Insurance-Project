from flask import Flask, jsonify

# Dictionary of auto insurance data
auto_insurance_data = [
    {"insured_education_level: "Associate", "College", "High School", "JD", "Masters", "MD", "PhD"}
]

# Flask Setup
app = Flask (__name__)

# Flask Routes
@app.route('/api/auto_insurance/data/QuickDBD-export.sql')
def insured_education_level():
    """Return the auto insurance data as json"""

    return jsonify(insured_education_level)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Auto Insurance Data API!<br/>"
        f"Available Routes:<br/>"
        f"/PROJECT 2_INSURANCE/auto_insurance/data/QuickDBD-export.sql/insured_education_level"
    )


if __name__ == '__main__':
    app.run(debug=True) 
    