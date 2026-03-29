import pandas as pd
import random
from faker import Faker

fake = Faker()

NUM_ORGS = 50
NUM_DEPARTMENTS = 200
NUM_EMPLOYEES = 2000
NUM_PROJECTS = 500

industries = ["Technology", "Finance", "Healthcare", "Retail", "Education"]
departments = ["IT", "HR", "Finance", "Marketing", "Operations"]
jobs = ["Manager", "Engineer", "Analyst", "Specialist", "Director"]

# Organizations
orgs = []
for i in range(1, NUM_ORGS + 1):
    orgs.append({
        "organization_id": i,
        "organization_name": fake.company(),
        "industry": random.choice(industries),
        "country": fake.country(),
        "founded_year": random.randint(1980, 2023),
        "employees": random.randint(50, 5000),
        "annual_revenue": random.randint(1000000, 500000000)
    })

org_df = pd.DataFrame(orgs)

# Departments
dept_list = []
for i in range(1, NUM_DEPARTMENTS + 1):
    dept_list.append({
        "department_id": i,
        "organization_id": random.randint(1, NUM_ORGS),
        "department_name": random.choice(departments),
        "budget": random.randint(50000, 5000000)
    })

dept_df = pd.DataFrame(dept_list)

# Employees
emp_list = []
for i in range(1, NUM_EMPLOYEES + 1):
    emp_list.append({
        "employee_id": i,
        "department_id": random.randint(1, NUM_DEPARTMENTS),
        "name": fake.name(),
        "job_title": random.choice(jobs),
        "salary": random.randint(40000, 150000),
        "hire_date": fake.date_between(start_date="-10y", end_date="today")
    })

emp_df = pd.DataFrame(emp_list)

# Projects
proj_list = []
for i in range(1, NUM_PROJECTS + 1):
    proj_list.append({
        "project_id": i,
        "department_id": random.randint(1, NUM_DEPARTMENTS),
        "project_name": fake.bs(),
        "budget": random.randint(10000, 1000000),
        "start_date": fake.date_between(start_date="-3y", end_date="-1y"),
        "end_date": fake.date_between(start_date="-1y", end_date="today"),
        "status": random.choice(["completed", "in progress", "cancelled"])
    })

proj_df = pd.DataFrame(proj_list)

# Save datasets
org_df.to_csv("organizations.csv", index=False)
dept_df.to_csv("departments.csv", index=False)
emp_df.to_csv("employees.csv", index=False)
proj_df.to_csv("projects.csv", index=False)

print("Organization dataset generated!")