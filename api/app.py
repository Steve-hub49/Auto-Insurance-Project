import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine(f'postgres://postgres:slfpostgres2435!@localhost:5432/auto_ins_test')

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
@app.route("/education")
def insured_education_level():
    """Return the auto insurance data as json"""
    # TODO: Need to add policyholder ID
    result = session.query(AutoInsurance.insured_education_level).all()
    return jsonify(result)
    # return jsonify(auto_insurance_education_data)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Auto Insurance Data API!<br/>"
        f"Available Routes:<br/>"
        f"/PROJECT 2_INSURANCE/auto_insurance/data/QuickDBD-export.sql/insured_education_level"
    )


if __name__ == '__main__':
    app.run(debug=True) 
    