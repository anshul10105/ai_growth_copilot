import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_insights(metrics):
    prompt = f"""
You are a senior product manager and growth strategist.

Analyze the following product metrics:
{metrics}

Provide:
1. The biggest growth bottleneck
2. Five recommended experiments
3. An A/B test plan
4. A short mini PRD
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text

