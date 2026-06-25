import os
import traceback
import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


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

1. Reduce onboarding steps.
2. Add a progress indicator.
3. Improve first-time user experience.
4. Send reminder notifications.
5. Introduce referral rewards.

### A/B Test

- Control: Current onboarding
- Variant: Simplified onboarding
- Primary Metric: Activation Rate

### Mini PRD

Build a simplified onboarding experience to improve activation and retention.
"""


def generate_insights(metrics):

    prompt = f"""
You are a Senior Product Manager at a SaaS company.

Analyze these product metrics:

{metrics}

Generate:

1. Biggest Bottleneck
2. Five Product Experiments
3. A/B Test Plan
4. Mini PRD
5. Expected Business Impact

Return the answer in Markdown.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
        )

        return response.choices[0].message.content

    except Exception as e:
        st.error(f"Groq Error: {e}")
        st.code(traceback.format_exc())
        return fallback_recommendations(metrics)

