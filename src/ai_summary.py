def generate_summary(risk_df):

    if risk_df.empty:
        return "No major risks detected."

    summary = "Executive Summary:\n\n"

    summary += f"{len(risk_df)} risks detected.\n\n"

    for _, row in risk_df.iterrows():
        summary += f"- {row['type']} detected for {row['commitment_id']} with impact ${row['impact']}\n"

    summary += "\nRecommendation:\nReview underutilized commitments and reduce on-demand leakage."

    return summary
