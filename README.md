# AI Growth Copilot

AI Growth Copilot is an AI-powered product analytics application that analyzes user funnel data and generates actionable growth recommendations to improve activation, retention, and organic referrals.

## Live Demo
Deployed Streamlit link: https://aigrowthcopilot-kq63sa7npuyff89wmxahwq.streamlit.app/

## Project Overview

Product and growth teams often need to identify where users drop off and decide which experiments to run next. This application automates that workflow by:

1. Accepting product funnel data in CSV format
2. Calculating key product metrics
3. Identifying the largest growth bottleneck
4. Generating recommended experiments
5. Creating an A/B test plan
6. Producing a mini Product Requirements Document (PRD)

The application uses OpenAI's API to generate recommendations and includes a fallback recommendation engine to ensure uninterrupted functionality if the API is unavailable.

## Key Features

- CSV upload for product funnel data
- Automated KPI calculation
- AI-generated growth recommendations
- A/B testing plan generation
- Mini PRD generation
- OpenAI API integration
- Fallback recommendation engine
- Interactive web interface built with Streamlit

## Product Metrics Calculated

- Total Users
- Onboarding Rate
- Activation Rate
- Day 1 Retention
- Day 7 Retention
- Referral Rate
- Subscription Rate
- Revenue

## Tech Stack

- Python
- Pandas
- Streamlit
- OpenAI API

## Input Schema

The application expects a CSV file with the following columns:

- `user_id`
- `signup_date`
- `onboarding_complete`
- `activated`
- `retained_day1`
- `retained_day7`
- `referred_friend`
- `referral_converted`
- `subscribed`
- `revenue`

## Example Output

### Biggest Bottleneck
Identifies the most critical growth issue (e.g., low activation, retention, or referral performance).

### Recommended Experiments
Generates product experiments such as:
- Simplifying onboarding
- Introducing progress indicators
- Sending re-engagement notifications
- Adding referral incentives

### A/B Test Plan
Defines:
- Control and variant
- Primary success metric
- Expected impact

### Mini PRD
Provides a concise product requirement statement describing the feature to build and the business objective it supports.

## Project Structure

```text
ai-growth-copilot/
├── app.py
├── metrics.py
├── ai_insights.py
├── user_events.csv
├── requirements.txt
└── README.md
