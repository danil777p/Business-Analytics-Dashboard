def build_budget_prompt(budget_result):
    return f"""
    You are a data analyst.

    You got these types of info:
    - Maximum budget: {budget_result['max']['budget']}
    - Minimum budget: {budget_result['min']['budget']}
    - Average budget: {budget_result['avg']:.1f}
    - Budget difference: {budget_result['difference']}

    Give 3 short business insights in bullet points.
    """

def build_employees_prompt(employees_result):
    return f""" 
 You are a data analyst.

    Employees Summary:
    - Department with most employees: {employees_result['most']['department_name']} ({employees_result['most']['number_of_empl']})
    - Department with least employees: {employees_result['least']['department_name']} ({employees_result['least']['number_of_empl']})
    - Average employees: {employees_result['average']:.1f}

    Focus on:
    - workload distribution
    - efficiency
    - balance between departments

    Give 3 short business insights in bullet points.
"""
def build_revenue_prompt(revenue_result):
    return f""" 
You are a data analyst.
Revenue Summary:
- The most revenue: {revenue_result['top']['organization_name']} ({revenue_result['top']['annual_revenue']})
- The least revenue: {revenue_result['bottom']['organization_name']} ({revenue_result['bottom']['annual_revenue']})
- Spread: {revenue_result['spread']}
Give 3 short business insights in bullet points. Focus on quality and rightness of information.
"""
def build_orgs_prompt(orgs_result):
    return f"""
You are a data analyst.

    Organization Distribution Summary:
    - Largest share: {orgs_result['largest_share']['country']} ({orgs_result['largest_pct']:.1f}%)
    - Smallest share: {orgs_result['smallest_share']['country']} ({orgs_result['smallest_pct']:.1f}%)
    - Distribution type: {orgs_result['distribution']}

    Interpretation guide:
    - If highly unbalanced → one region dominates
    - If balanced → global spread

    Give 3 short business insights in bullet points.
    """
def build_employees_org_prompt(employees_org_result):
    return f"""
You are a data analyst.

    Company Size Summary:
    - Largest company: {employees_org_result['largest_org']} ({employees_org_result['max_employees']} employees)
    - Smallest company: {employees_org_result['smallest_org']} ({employees_org_result['min_employees']} employees)
    - Average employees: {employees_org_result['average']:.1f}
    - Employee spread: {employees_org_result['spread']}
    - Clustering: {employees_org_result['clustering']}

    Focus on:
    - company size differences
    - scalability
    - market structure (dominance vs competition)

    Give 3 short business insights in bullet points.
    """
def build_salary_prompt(salary_result):
    return f"""
You are a data analyst.

    Salary Summary:
    - The highest salary: {salary_result['highest']['department_name']} ({salary_result['highest']['average_salary']})
    - The lowest salary:  {salary_result['lowest']['department_name']} ({salary_result['lowest']['average_salary']})
    - Salary difference: {salary_result['difference']}
Give 3 short business insights in bullet points.

 """
def build_projects_prompt(result):
    return f"""
    You are a data analyst.

    Project Workload Summary:
    - Department with most projects: {result['top_department']} ({result['max_projects']} projects)
    - Department with least projects: {result['least_department']} ({result['min_projects']} projects)
    - Average number of projects: {result['average_projects']:.1f}
    - Project spread: {result['spread']}
    - Workload distribution: {result['workload_distribution']}

    Focus on:
    - workload balance across departments
    - operational pressure
    - resource allocation efficiency

    Give 3 short business insights in bullet points.
    """
def build_status_prompt(result):
    return f"""
    You are a data analyst.

    Project Status Summary:
    - Most common status: {result['most']}
    - Least common status: {result['least']}

    Distribution:
    - Completed: {result['completed']:.1f}%
    - In Progress: {result['in_progress']:.1f}%
    - Cancelled: {result['cancelled']:.1f}%

    Interpretation rules:
    - High cancelled → operational issues 🚨
    - High completed → strong performance ✅

    Current situation:
    {result['insight']}

    Give 3 short business insights in bullet points.
    """
