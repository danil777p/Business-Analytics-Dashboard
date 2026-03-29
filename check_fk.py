
import pandas as pd

organizations = pd.read_csv("organizations.csv")
departments = pd.read_csv("departments.csv")
employees = pd.read_csv("employees.csv")
projects = pd.read_csv("projects.csv")

employees["department_id"].isin(
    departments["department_id"]
).all()
departments["organization_id"].isin(
    organizations["organization_id"]
).all()
projects["department_id"].isin(
    departments["department_id"]
).all()


