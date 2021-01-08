from flask import Flask, jsonify, render_template
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from config import USERNAME, PASSWORD, HOST, PORT, DB 


# Database Setup
conn_str = f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
engine = create_engine(conn_str)
# automatically detect tables
Base = automap_base()
Base.prepare(engine, reflect=True)
print(Base.classes.keys())

# # Save reference to the table
# AutoInsurance = Base.classes.auto_ins

# # Create session
# session = Session(engine)

# # Flask Setup
# app = Flask(__name__)

# # Flask Routes
# @app.route("/")
# def welcome():
#     return render_template("index.html")


# @app.route("/education")    # Depricated
# def education():
#     """Return counts of education level as json"""
#     result = session.query(
#         AutoInsurance.insured_education_level,
#         func.count(AutoInsurance.insured_education_level)
#         ).group_by(AutoInsurance.insured_education_level).all()
#     results = []
#     for policy_holder, n in result:
#         temp = {}
#         temp['policy_holder'] = policy_holder
#         temp['n'] = n
#         results.append(temp)
#     print(results)
#     return jsonify(results)


# @app.route("/insured_education_level")    
# def insured_education_level():
#     """Return the insured_education_level column as json"""
#     result = session.query(
#         AutoInsurance.insured_education_level,
#          ).all()
#     return jsonify(result)


# if __name__ == '__main__':
#     app.run(debug=True) 
    