import os
import traceback
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def fallback_recommendations(metrics):
    activation = metrics.get("Activation Rate", 0)

    if activation < 50:
        bottleneck = "Activation after onboarding is the biggest bottleneck."
    else:
        bottleneck = "Retention is the main opportunity area."

    return f"""
### Biggest Bottleneck
{bottleneck}

### Recommended Experiments
1. Reduce onboarding steps from 5 to 3.
2. Add a progress bar during onboarding.
3. Show example content immediately after signup.
4. Send a reminder notification after 24 hours.
5. Add referral rewards for inviting friends.

### A/B Test Plan
- **Control:** Current onboarding
- **Variant:** Simplified onboarding
- **Primary Metric:** Activation Rate
- **Expected Impact:** +10% to +20%

### Mini PRD
Build a simplified onboarding flow to improve user activation and downstream retention.
"""


def generate_insights(metrics):
    try:
        prompt = f"""
You are a senior product manager and growth strategist.

Analyze the following product metrics:

{metrics}

Provide:
1. The biggest growth bottleneck
2. Five recommended experiments
3. An A/B test plan
4. A short Mini PRD

Return the response in Markdown.
"""

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        return response.output_text

    except Exception as e:
        st.error(f"OpenAI Error: {e}")
        st.code(traceback.format_exc())
        return fallback_recommendations(metrics)

