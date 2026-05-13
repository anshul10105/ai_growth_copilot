import streamlit as st
import pandas as pd
from src.metrics import calculate_metrics
from src.ai_insights import generate_insights

st.set_page_config(page_title="AI Growth Copilot", layout="wide")
st.title("AI Growth Copilot")
st.write(
    "Analyze product funnel data and generate recommendations to improve "
    "activation, retention, and referral growth."
)

uploaded_file = st.file_uploader("Upload CSV", type=["csv"], accept_multiple_files=False)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/user_events.csv")
    st.info("Using sample dataset from data/user_events.csv")

metrics = calculate_metrics(df)

st.subheader("Key Metrics")
cols = st.columns(4)
for i, (k, v) in enumerate(metrics.items()):
    if isinstance(v, float):
        display = f"{v:.2f}%"
    else:
        display = str(v)
    cols[i % 4].metric(k, display)

if st.button("Generate Recommendations"):
    st.subheader("Recommended Experiments")
    st.markdown(generate_insights(metrics))
