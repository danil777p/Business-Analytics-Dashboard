import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:26102007danil!@127.0.0.1/for_dashboard")

org = pd.read_csv("organizations.csv")
dep = pd.read_csv("departments.csv")
emp = pd.read_csv("employees.csv")
proj = pd.read_csv("projects.csv")

org.to_sql("organizations", engine, if_exists="append", index=False)
dep.to_sql("departments", engine, if_exists="append", index=False)
emp.to_sql("employees", engine, if_exists="append", index=False)
proj.to_sql("projects", engine, if_exists="append", index=False)