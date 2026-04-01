import pandas as pd

def calculate_utilization(df):
    df["utilization_pct"] = df["effective_cost"] / df["on_demand_cost"]
    return df

def detect_underutilization(df):
    df["underutilized"] = df["utilization_pct"] < 0.7
    return df

def detect_coverage_gap(df):
    df["on_demand_leakage"] = df["on_demand_cost"] - df["effective_cost"]
    df["coverage_risk"] = df["on_demand_leakage"] > 200
    return df

def build_risk_register(df):
    risks = []

    for _, row in df.iterrows():

        if row["underutilized"]:
            risks.append({
                "commitment_id": row["commitment_id"],
                "type": "UNDERUTILIZATION",
                "impact": row["on_demand_cost"]
            })

        if row["coverage_risk"]:
            risks.append({
                "commitment_id": row["commitment_id"],
                "type": "COVERAGE_GAP",
                "impact": row["on_demand_leakage"]
            })

    return pd.DataFrame(risks)
