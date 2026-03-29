def analyze_status(df):
    status_counts = df['status'].value_counts()
    
    most_common = status_counts.idxmax()
    least_common = status_counts.idxmin()
    
    status_pct = (status_counts / status_counts.sum()) * 100
    
    completed = status_pct.get('Completed', 0)
    in_progress = status_pct.get('In Progress', 0)
    cancelled = status_pct.get('Cancelled', 0)
    
    if cancelled > 30:
        insight = "⚠️ High cancellation rate"
    elif completed > 60:
        insight = "✅ Strong completion performance"
    else:
        insight = "⚖️ Moderate performance"
    
    return {
        "most": most_common,
        "least": least_common,
        "completed": completed,
        "in_progress": in_progress,
        "cancelled": cancelled,
        "insight": insight
    }

def analyze_budgets(budget_df):
    max_budget = budget_df.loc[budget_df['budget'].idxmax()]
    min_budget = budget_df.loc[budget_df['budget'].idxmin()]
    average_budget = budget_df['budget'].mean()
    difference_budget = max_budget['budget'] - min_budget['budget']
    return{
        "max": max_budget,
        "min": min_budget,
        "avg": average_budget,
        "difference": difference_budget
    }

def analyze_employees(employees_df):
    most_empl = employees_df.loc[employees_df['number_of_empl'].idxmax()]
    least_empl = employees_df.loc[employees_df['number_of_empl'].idxmin()]
    avg_empl = employees_df['number_of_empl'].mean()
    return{
        "most": most_empl,
        "least": least_empl,
        "average": avg_empl
    }

def analyze_revenue(df):
    top_row = df.loc[df['annual_revenue'].idxmax()]
    bottom_row = df.loc[df['annual_revenue'].idxmin()]
    spread = df['annual_revenue'].max() - df['annual_revenue'].min()
    return {
       "top": top_row.to_dict(),
       "bottom": bottom_row.to_dict(),
        "spread": spread
    }

def analyze_organizations(df):
    largest_share = df.loc[df['number_of_orgs'].idxmax()]
    smallest_share = df.loc[df['number_of_orgs'].idxmin()]
    
    total = df['number_of_orgs'].sum()
    
    largest_pct = (largest_share['number_of_orgs'] / total) * 100
    smallest_pct = (smallest_share['number_of_orgs'] / total) * 100

    if largest_pct > 50:
        distribution = "Highly unbalanced"
    elif largest_pct > 35:
        distribution = "Moderately unbalanced"
    else:
        distribution = "Balanced distribution"

    return {
        "largest_share": largest_share,
        "smallest_share": smallest_share,
        "largest_pct": largest_pct,
        "smallest_pct": smallest_pct,
        "distribution": distribution
    }

def analyze_employees_org(df):
    
    most = df.loc[df['employees'].idxmax()]
    least = df.loc[df['employees'].idxmin()]

    
    max_val = df['employees'].max()
    min_val = df['employees'].min()
    spread = max_val - min_val
    avg = df['employees'].mean()

    
    if spread < avg * 0.3:
        clustering = "Highly clustered (similar sizes)"
    elif spread < avg:
        clustering = "Moderately clustered"
    else:
        clustering = "Not clustered (large differences)"

    
    return {
        "largest_org": most['organization_name'],
        "smallest_org": least['organization_name'],
        "max_employees": max_val,
        "min_employees": min_val,
        "average": avg,
        "spread": spread,
        "clustering": clustering
    }
def analyze_salary(df):
    highest = df.loc[df['average_salary'].idxmax()]
    lowest = df.loc[df['average_salary'].idxmin()]
    difference = df['average_salary'].max() - df['average_salary'].min()
    return{
        "highest": highest,
        "lowest": lowest,
        "difference":difference
    }

def analyze_projects(df):
    most_proj = df.loc[df['number_of_projects'].idxmax()]
    least_proj = df.loc[df['number_of_projects'].idxmin()]
    max_val = df['number_of_projects'].max()
    min_val = df['number_of_projects'].min()
    spread = df['number_of_projects'].max() - df['number_of_projects'].min()
    avg = df['number_of_projects'].mean()
    if spread < avg * 0.3:
        result = "Balanced workload"
    elif spread < avg:
        result = "Moderately balanced"
    else:
        result = "Unbalanced workload (some departments overloaded)"
    return{
        "top_department": most_proj['department_name'],
        "least_department": least_proj['department_name'],
        "max_projects": max_val,
        "min_projects": min_val,
        "average_projects": avg,
        "spread": spread,
        "workload_distribution": result

    }
