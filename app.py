import os
from flask import Flask, jsonify, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# from config import USERNAME, PASSWORD, HOST, PORT, DB, TABLE_NAME
USERNAME = os.environ['PG_USERNAME']
PASSWORD = os.environ['PG_PASSWORD']
HOST = os.environ['HOST']
PORT = os.environ['PORT']
DB = os.environ['DB']
TABLE_NAME = os.environ['TABLE_NAME']


# Database Setup
conn_str = f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
engine = create_engine(conn_str)
# automatically detect tables
Base = automap_base()
Base.prepare(engine, reflect=True)
# Save reference to the table
InsuranceClaims = Base.classes[TABLE_NAME]
# Create session
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/education")    # Depricated
def education():
    """Return counts of education level as json"""
    result = session.query(
        InsuranceClaims.insured_education_level,
        func.count(InsuranceClaims.insured_education_level)
        ).group_by(InsuranceClaims.insured_education_level).all()
    results = []
    for policy_holder, n in result:
        temp = {}
        temp['policy_holder'] = policy_holder
        temp['n'] = n
        results.append(temp)
    print(results)
    return jsonify(results)


@app.route("/insured_education_level")    
def insured_education_level():
    """Return the insured_education_level column as json"""
    result = session.query(
        InsuranceClaims.insured_education_level,
         ).all()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True) 
    