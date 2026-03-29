import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import plotly.graph_objects as go
from ai_insights import *
from func_ai_insights import get_ai_insights
from prompts import *


from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
)

st.title = "Business Analytics Dashboard"


org = pd.read_sql("SELECT COUNT(*) AS total FROM organizations", engine)
emp = pd.read_sql("select sum(organizations.employees) as total_employees from organizations", engine)
proj = pd.read_sql("SELECT COUNT(*) AS total_projects FROM projects", engine)
budget = pd.read_sql("SELECT sum(budget) AS total_budget FROM projects", engine)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Organizations", int(org.iloc[0,0]))
col2.metric("Employees", int(emp.iloc[0,0]))
col3.metric("Projects", int(proj.iloc[0,0]))
col4.metric("Project Budget", int(budget.iloc[0,0]))




query = "select department_name,budget from departments order by budget limit 10"
budget_df = pd.read_sql(query, engine)

budget_result = analyze_budgets(budget_df)

fig = px.bar(
    budget_df,
    x="department_name",
    y="budget",
    color = "department_name",
    title = "Budgets by Department",
    color_discrete_map={'gold':'yellow', 'silver':'grey'}
)

    
   


col1, col2,col3 = st.columns([1, 2, 1])

with col1:
    st.markdown("### Observation")
    

    st.markdown("""
    <div style="height:500px; overflow-y: auto;">
    
    This chart shows the differences in budgets across departments.<br><br>

    Marketing has the highest budget, while HR has the lowest.
    This difference may be explained by the varying importance or investment focus of each department.<br><br>

    Finance and Operations are in the middle, with relatively similar budget levels.
    Both departments play essential roles in an organization, but in some companies,
    Finance may receive more funding due to its direct impact on financial performance and decision-making.
    
    </div>
    """, unsafe_allow_html=True)

with col2:
    fig.update_layout(height=500,
    xaxis_title = "Departments",
    xaxis = dict(title_font = dict(size = 21)),
    yaxis_title = "Budget",
    yaxis = dict(title_font = dict(size = 21)),
    title = dict(
    text = "Budgets by Department",
    x = 0.5,
    xanchor = 'center',
    font = dict(size = 24)))
    st.plotly_chart(fig, width= 'stretch')

with col3:
    st.markdown("### AI Insight")

    if st.button("Generate Insights"):
        prompt = build_budget_prompt(budget_result)
        ai_text = get_ai_insights(prompt)
        st.markdown(f"""
        <div style="
            height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        ">
        {ai_text}
        </div>
        """, unsafe_allow_html=True)
st.divider()






query = """
select count(employees.name) as number_of_empl, department_name
from departments
join employees
on departments.department_id = employees.department_id
group by department_name
order by number_of_empl desc
limit 10"""
employees_df =  pd.read_sql(query, engine)

employees_result = analyze_employees(employees_df)

fig = fig = px.bar(
    employees_df,
    x="department_name",
    y="number_of_empl",
    title="Employees by Department",
    color="department_name",
    color_discrete_map={
        "HR": "red",
        "IT": "blue",
        "Sales": "green",
        "Finance": "orange"
    }
)


col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.markdown("### Observation")
    st.markdown(""" 
    <div style="height:500px; overflow-y: auto;">
    The Operations department has the highest number of employees.
    This likely reflects the operational nature of the business, where
    more staff is required to manage core processes.
    This may indicate higher operational costs and suggests a need to evaluate
    efficiency and productivity within this department.
    </div>""",unsafe_allow_html=True)
with col2:
    fig.update_layout(
    xaxis_title = "Departments",
    xaxis = dict(title_font = dict(size = 21)),
    yaxis_title = "Number Of Employees",
    yaxis = dict(title_font = dict(size = 21)),
    height = 500,
    title = dict(text = "Employees by Department",
    x = 0.5,
    xanchor = 'center',
    font = dict(size = 24))
    )
    st.plotly_chart(fig, width='stretch',)
with col3:
    st.markdown("### Ai Insight")
    if st.button("Generate Insights(1)"):
        prompt = build_employees_prompt(employees_result)
        ai_text = get_ai_insights(prompt)
        st.markdown(f"""
        <div style="
            height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        ">
        {ai_text}
        </div>
        """, unsafe_allow_html=True)

st.divider()






query = """select organization_name, annual_revenue
from organizations
order by annual_revenue desc
limit 10"""
df = pd.read_sql(query,engine)

revenue_result = analyze_revenue(df)

st.title = "Organizations with highest annual revenue"
fig = px.bar(
    df,
    x="annual_revenue",
    y="organization_name",
    orientation="h",
    color = "organization_name",
    title="Annuel revenue for each organization",
    
    color_continuous_scale="annual_revenue"
)

col1, col2, col3 = st.columns([4,9,4])
with col1:
    st.markdown("### Observation")
    st.markdown(""" 
    <div style="height:500px; overflow-y: auto;">
    The chart shows a group of organizations with fairly similar annual revenues, 
    indicating a balanced and competitive environment.
     While there is a clear ranking from highest to lowest, the differences between companies are not extreme.
    At the top, a few organizations slightly outperform the rest, but they do not dominate the market. 
    Most companies fall into a closely grouped middle range, suggesting consistent performance levels across the industry. The lowest-performing organizations are only marginally behind, reinforcing the idea of a tight revenue distribution.
    </div>""",unsafe_allow_html=True)
with col2:
    fig.update_layout(
    xaxis_title = "Annual Revenue",
    xaxis = dict(title_font = dict(size = 21)),
    yaxis_title = "Organizations",
    yaxis = dict(title_font = dict(size = 21)),
    title = dict(text = " Revenue Per Organization",
    x = 0.5,
    xanchor = 'center',
    font = dict(size = 24)))
    st.plotly_chart(fig,width='stretch')
with col3:
    st.markdown("### AI Insight")
    if st.button("Generate Insights(2)"):
        prompt = build_revenue_prompt(revenue_result)
        ai_text = get_ai_insights(prompt)
        st.markdown(f"""
        <div style="
            height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        ">
        {ai_text}
        </div>
        """, unsafe_allow_html=True)

st.divider()



query = """select count(organization_name) as number_of_orgs, country
from organizations
group by country
order by number_of_orgs desc
limit 10"""
df = pd.read_sql(query,engine)

orgs_result = analyze_organizations(df)


st.title = "Organizations in countries"
fig = px.pie(
    df,
    values="number_of_orgs",
    names="country",
    title="Organizations by Country"
)
col1,col2,col3 = st.columns([9,20,9])
with col1:
    st.markdown("### Observation")
    st.markdown(""" <div style="height:500px; overflow-y: auto;">
    The chart illustrates the distribution of organizations across different countries
    showing a largely even spread with most countries contributing a similar share
    The majority of countries each account for approximately 11.1% of the total, 
    indicating that organizations are fairly evenly distributed geographically. 
    This suggests no single country dominates in terms of organizational presence.
    A smaller portion of countries contributes around 5.6% each, representing a slightly
    lower level of representation. However, these differences are not substantial enough to indicate a major imbalance.</div>""",unsafe_allow_html=True)
with col2:
    fig.update_layout(title =dict(text = "Organizations by Country",
     x = 0.5,
     xanchor = 'center',
     font = dict(size = 24)))
    st.plotly_chart(
    fig,
    config={"responsive": True}
)
with col3:
    st.markdown("### AI Insight")
    if st.button("Generate Insights(3)"):
        prompt = build_orgs_prompt(orgs_result)
        ai_text = get_ai_insights(prompt)
        st.markdown(f"""
        <div style="
            height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        ">
        {ai_text}
        </div>
        """, unsafe_allow_html=True)

st.divider()





query = """select organization_name, employees
from organizations
order by employees desc
limit 10"""
df = pd.read_sql(query,engine)
employees_org_result = analyze_employees_org(df)



fig = px.bar(
    df,
    x="employees",
    y="organization_name",
    orientation="h",
    title="Top Employees Organizations by Employees",
    color = "organization_name",
    color_discrete_map = {
    "Shaw, Kelley and Green": "red",
    "Hamilton, Stone and Briggs": "blue",
    "Cohen PLC": "green",
    "Robinson Ltd": "orange",
    "Ortiz PLC": "purple",
    "Jones-Boone": "brown",
    "Anderson, Ponce and Mclaughlin": "lightblue",
    "Ford-Williams": "pink",
    "Frost-Meyers": "turquoise",
    "Wright, Wagner and Fritz": "lightgreen"
}



)


col1, col2, col3 = st.columns([1.5, 3, 2])

with col1:
    st.markdown("### Observation")
    st.markdown("""
    The chart presents the distribution of employee counts across the top organizations...
    Most organizations have employee counts clustered within a similar range...
    The top organization leads, but differences are not significant...
    Mid and lower-tier organizations remain relatively close in size.
    """)

with col2:
    fig.update_layout(
        height=750,
        xaxis_title="Employees",
        xaxis = dict(title_font = dict(size = 21)),
        yaxis_title="Organizations",
        yaxis = dict(title_font = dict(size = 21)),
        title=dict(
            text="Top Organizations by Employees",
            x=0.5,
            xanchor='center',
            font=dict(size=20)
        )
    )

    st.plotly_chart(
    fig,
    config={"responsive": True}
)
with col3:
    st.markdown("### AI Insight")
    if st.button("Generate Insights(4)"):
        prompt = build_employees_org_prompt(employees_org_result)
        ai_text = get_ai_insights(prompt)
        st.markdown(f"""
        <div style="
            height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        ">
        {ai_text}
        </div>
        """, unsafe_allow_html=True)



st.divider()






query = """SELECT department_name, AVG(salary) AS average_salary
FROM employees
JOIN departments
ON employees.department_id = departments.department_id
GROUP BY department_name"""
df = pd.read_sql(query,engine)

salary_result = analyze_salary(df)

title = "Average Salary by Department"
fig = go.Figure()
fig.add_trace(go.Scatter(
    x = df["average_salary"],
    y = df["department_name"],
    mode = "markers",
    marker = dict(size = 12, color = "orange"),
))
for i in range(len(df)):
    fig.add_shape(
        type = "line",
        x0 = 0,
        y0 = i,
        x1 = df["average_salary"][i],
        y1 = i,
        line = dict(width = 2, color = "lightblue")
    )

col1,col2,col3 = st.columns([1.8,4,2])
with col1:
    st.markdown("### Observation")
    st.markdown("""<div style="height:500px; overflow-y: auto;">
    The chart displays the average salary across different departments, showing
    a high level of consistency in compensation levels throughout the organization.
    All departments fall within a narrow salary range close to the upper end, indicating 
    that pay structures are relatively uniform. IT and HR appear to have slightly higher average salaries, 
    while Finance, Operations, and Marketing are just marginally lower. However, these differences are minimal.</div>""",unsafe_allow_html=True)
    
with col2:
    fig.update_layout(
    height = 700,
    xaxis_title = "Average Salary",
    xaxis = dict(title_font = dict(size = 21)),
    yaxis_title = "Department",
    yaxis = dict(title_font = dict(size = 21)),
    title = dict(text = "Average Salary by Department",
    x = 0.5,
    xanchor = 'center',
    font = dict(size = 24))
)
    st.plotly_chart(
    fig,
    config={"responsive": True}
)
with col3:
    st.markdown("### AI Insight")
    if st.button("Generate Insights(5)"):
        prompt = build_salary_prompt(salary_result)
        ai_text = get_ai_insights(prompt)
        st.markdown(f"""
        <div style="
            height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        ">
        {ai_text}
        </div>
        """, unsafe_allow_html=True)
    
st.divider()






query = """SELECT 
    COUNT(project_name) AS number_of_projects, department_name
FROM
    projects
        JOIN
    departments ON departments.department_id = projects.department_id
GROUP BY department_name
ORDER BY number_of_projects DESC
LIMIT 10"""
df = pd.read_sql(query,engine)

projects_result = analyze_projects(df)

title = "Quantity Of Projects By Department"
fig = go.Figure()
fig.add_trace(go.Scatter(
    x = df["number_of_projects"],
    y = df["department_name"],
    mode = "markers",
    marker = dict(size = 12, color = "red"),
))
for i in range(len(df)):
    fig.add_shape(
        type = "line",
        x0 = 0,
        y0 = i,
        x1 = df["number_of_projects"][i],
        y1 = i,
        line = dict(width = 2, color = "blue")
    )
col1,col2,col3 = st.columns([1.8,3,2])
with col1:
    st.markdown("### Observation")
    st.markdown("""<div style="height:500px; overflow-y: auto;">
The chart illustrates the number of projects handled by each department, revealing clear
 differences in workload distribution across the organization.
Operations leads with the highest number of projects,
indicating it is the most workload-intensive department. HR and Marketing also manage a relatively high
volume of projects, forming a strong upper tier in terms of activity levels. 
IT follows with a moderate number of projects, while Finance handles the fewest.</div>""",unsafe_allow_html=True)
with col2:
    fig.update_layout(
    height =700,
    xaxis_title = "Number Of Projects",
    xaxis = dict(title_font = dict(size = 21)),
    yaxis_title = "Department Name",
    yaxis = dict(title_font = dict(size = 21)),
    title = dict(text = " Projects By Department",
    x = 0.5,
    xanchor = 'center',
    font = dict(size = 24))
)
    st.plotly_chart(
    fig,
    config={"responsive": True}
)
with col3:
     st.markdown("### AI Insight")
     if st.button("Generate Insights(6)"):
        prompt = build_projects_prompt(projects_result)
        ai_text = get_ai_insights(prompt)
        st.markdown(f"""
        <div style="
            height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        ">
        {ai_text}
        </div>
        """, unsafe_allow_html=True)
        

st.divider()





query = """SELECT 
status,
COUNT(*) AS project_count
FROM projects
GROUP BY status
ORDER BY project_count DESC"""
df = pd.read_sql(query,engine)

status_result = analyze_status(df)

fig = px.pie(
    df,
    names = "status",
    values = "project_count",
    hole = 0.5,
    title = "Project Status Distribution"
)
col1,col2,col3 = st.columns([2,4,2])
with col1:
    st.markdown("### Observation")
    st.markdown("""<div style="height:300px; overflow-y: auto;">
    The chart presents the distribution of project statuses, showing a relatively balanced
    split across all categories with no single status overwhelmingly dominant.
    Cancelled projects account for the largest share, slightly 
    above one-third of the total. Projects that are in progress follow closely, while completed projects represent
    the smallest portion, though still a significant share. The differences between the three categories are 
    moderate rather than extreme.</div>""",unsafe_allow_html=True)
with col2:
    fig.update_layout(
    legend_title = "Status",
    title = dict(
        text = "Project Status Distribution",
        x = 0.5,
        xanchor = 'center',
        font = dict(size = 24))

)
    st.plotly_chart(
    fig,
    config={"responsive": True}
)
with col3:
    st.markdown("### AI Insight")
    if st.button("Generate Insights(7)"):
        prompt = build_status_prompt(status_result)
        ai_text = get_ai_insights(prompt)
        st.markdown(f"""
        <div style="
            height: 500px;
            overflow-y: auto;
            padding-right: 10px;
        ">
        {ai_text}
        </div>
        """, unsafe_allow_html=True)

st.divider()


