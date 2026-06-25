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
## Executive Summary

The uploaded product metrics indicate that the product is functioning well overall,
but there is an opportunity to improve long-term engagement and user growth.

## Biggest Bottleneck

{bottleneck}

## Recommended Experiments

1. Reduce onboarding steps.
2. Add a progress indicator during onboarding.
3. Improve the first-time user experience.
4. Send reminder notifications after signup.
5. Introduce referral rewards.

## A/B Test Plan

**Control**
- Existing onboarding flow

**Variant**
- Simplified onboarding with fewer steps

**Primary Success Metric**
- Activation Rate

**Expected Outcome**
- Increase activation by 10–20%.

## Mini PRD

**Problem**

Users are dropping before becoming long-term active users.

**Goal**

Increase activation and improve retention.

**Proposed Solution**

Simplify onboarding and improve early user engagement.

**Success Metrics**

- Higher activation rate
- Better Day 7 retention
- Increased subscriptions

## Business Impact

Improving activation and retention is expected to increase
subscription conversions and overall revenue.
"""


def generate_insights(metrics):

    prompt = f"""
You are a Senior Product Manager at a fast-growing SaaS company.

Analyze the following product metrics.

Total Users: {metrics['Total Users']}
Onboarding Rate: {metrics['Onboarding Rate']:.2f}%
Activation Rate: {metrics['Activation Rate']:.2f}%
Day 1 Retention: {metrics['Day 1 Retention']:.2f}%
Day 7 Retention: {metrics['Day 7 Retention']:.2f}%
Referral Rate: {metrics['Referral Rate']:.2f}%
Subscription Rate: {metrics['Subscription Rate']:.2f}%
Revenue: ₹{metrics['Revenue']}

Generate a professional product analytics report.

Use exactly these headings.

## Executive Summary

Summarize overall product health in 4-5 concise sentences.

## Biggest Bottleneck

Identify the weakest metric and explain why it matters.

## Recommended Experiments

Suggest five practical product experiments.

For each experiment include:
- Objective
- Reasoning
- Expected Impact

## A/B Test Plan

Include:
- Control
- Variant
- Primary Success Metric
- Expected Outcome

## Mini PRD

Include:
- Problem Statement
- Goal
- Proposed Solution
- Success Metrics

## Business Impact

Estimate how implementing these recommendations could improve:
- Activation
- Retention
- Revenue

Return everything in Markdown.

Do not include introductory text or disclaimers.
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
            temperature=0.4,
            max_tokens=1500
        )

        return response.choices[0].message.content

    except Exception as e:
        st.error(f"Groq Error: {e}")
        st.code(traceback.format_exc())
        return fallback_recommendations(metrics)

