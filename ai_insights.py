def generate_insights(metrics):
    activation = metrics.get("Activation Rate", 0)
    if activation < 50:
        bottleneck = "Activation after onboarding is the biggest bottleneck."
    else:
        bottleneck = "Retention is the main opportunity area."

    return f'''
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
'''
