import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template

# Database Setup
engine = create_engine(f'postgres://postgres:slfpostgres2435!@localhost:5432/auto_ins_test')
# I need to hide my password but need assistance here
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Test tables in db
print(Base.classes.keys())

# Save reference to the table
AutoInsurance = Base.classes.auto_ins

# Create session
session = Session(engine)


# Flask Setup
app = Flask (__name__)

# Flask Routes
@app.route("/")
def welcome():
    return (
        f"Welcome to the Auto Insurance Data API!<br/>"
        f"Available Routes:<br/>"
        f"/education"
        f"/insured_education_level"
    )


@app.route("/education")    # Depricated
def education():
    """Return counts of education level as json"""
    result = session.query(
        AutoInsurance.insured_education_level,
        func.count(AutoInsurance.insured_education_level)
        ).group_by(AutoInsurance.insured_education_level).all()
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
        AutoInsurance.insured_education_level,
         ).all()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True) 
    