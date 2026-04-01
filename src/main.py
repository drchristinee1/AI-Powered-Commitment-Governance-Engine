import pandas as pd
from risk_rules import *
from ai_summary import generate_summary

# Load sample data
df = pd.read_csv("../data/sample_commitment_data.csv")

# Apply FinOps logic
df = calculate_utilization(df)
df = detect_underutilization(df)
df = detect_coverage_gap(df)

# Build risk register
risk_df = build_risk_register(df)

# Generate summary
summary = generate_summary(risk_df)

# Save outputs
df.to_csv("../outputs/inventory.csv", index=False)
risk_df.to_csv("../outputs/risks.csv", index=False)

with open("../outputs/summary.md", "w") as f:
    f.write(summary)

print("✅ Engine run complete")
