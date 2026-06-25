# AI Growth Copilot

AI Growth Copilot is an AI-powered product analytics application that analyzes product funnel data and generates actionable growth recommendations using a Large Language Model (LLM).
The application enables product managers and growth teams to identify user drop-offs, understand key performance metrics, and receive AI-generated recommendations, A/B testing strategies, Mini PRDs, and downloadable reports.

## Live Demo
Deployed Streamlit link: https://aigrowthcopilot-kq63sa7npuyff89wmxahwq.streamlit.app/

## Screenshots
<img width="1847" height="490" alt="image" src="https://github.com/user-attachments/assets/802fd562-1211-49df-85ac-f21ea08b61f7" />
<img width="1708" height="636" alt="image" src="https://github.com/user-attachments/assets/f258bbcb-ce73-48bb-b033-6e683afeaed3" />
<img width="1746" height="677" alt="image" src="https://github.com/user-attachments/assets/bae4d974-3373-49ae-ad81-857987a1a9d6" />
<img width="1767" height="760" alt="image" src="https://github.com/user-attachments/assets/97892883-6f44-4928-a37e-74cbebeca2ab" />
<img width="1738" height="756" alt="image" src="https://github.com/user-attachments/assets/ad082054-fa7c-4b38-a64d-2c32291a7aea" />
<img width="406" height="87" alt="image" src="https://github.com/user-attachments/assets/12ef2175-cff7-499f-b142-1a15600b4867" />










## Key Features

- Upload product funnel datasets in CSV format
- Calculate key product growth metrics
- Interactive Product Funnel visualization
- AI-generated Executive Summary
- AI-generated Product Recommendations
- A/B Test Plan generation
- Fallback recommendation engine
- Interactive web interface built with Streamlit
- Mini PRD generation
- Business Impact analysis
- Download AI report as PDF
- Fallback recommendation engine when AI is unavailable

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
- Plotly
- Groq API (Llama 3.3)
- OpenAI Python SDK
- ReportLab

## Input Dataset
Expected CSV columns:

-user_id
-signup_date
-onboarding_complete
-activated
-retained_day1
-retained_day7
-referred_friend
-referral_converted
-subscribed
-revenue

## Workflow 
-Upload a CSV dataset.
-Product KPIs are calculated automatically.
-Product Funnel visualization is generated.
-AI analyzes the product metrics.
-Executive Summary is created.
-Growth experiments are recommended.
-A/B Test Plan is generated.
-Mini PRD is created.
-Business impact is estimated.
-AI report can be downloaded as a PDF.

## Project Structure

ai-growth-copilot/ 
│
├── app.py 
├── ai_insights.py
├── metrics.py
├── pdf_report.py 
├── user_events.csv 
├── requirements.txt
└── README.md
