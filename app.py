import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from metrics import calculate_metrics
from ai_insights import generate_insights
from pdf_report import create_pdf

st.set_page_config(
    page_title="AI Growth Copilot",
    layout="wide"
)

st.title("AI Growth Copilot")

st.markdown("""
Analyze product funnel data to identify bottlenecks and generate
AI-powered growth recommendations.
""")

st.divider()

st.subheader("Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"],
    accept_multiple_files=False
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("user_events.csv")
    st.info("Using sample dataset")

metrics = calculate_metrics(df)

st.divider()

st.subheader("Key Metrics")

cols = st.columns(4)

for i, (k, v) in enumerate(metrics.items()):

    if isinstance(v, float):
        display = f"{v:.2f}%"
    else:
        display = str(v)

    cols[i % 4].metric(k, display)

st.divider()

st.subheader("Product Funnel")

fig = go.Figure(
    go.Funnel(
        y=[
            "Onboarding",
            "Activation",
            "Day 1 Retention",
            "Day 7 Retention",
            "Subscription"
        ],
        x=[
            metrics["Onboarding Rate"],
            metrics["Activation Rate"],
            metrics["Day 1 Retention"],
            metrics["Day 7 Retention"],
            metrics["Subscription Rate"]
        ]
    )
)

fig.update_layout(
    height=500,
    margin=dict(
        l=40,
        r=40,
        t=40,
        b=40
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

if st.button("Generate AI Recommendations"):

    insights = generate_insights(metrics)

    st.subheader("AI Recommendations")

    st.markdown(insights)

    # Create PDF
    pdf = create_pdf(insights)

    # Download PDF
    st.download_button(
        label="Download AI Report",
        data=pdf,
        file_name="AI_Growth_Report.pdf",
        mime="application/pdf"
    )
