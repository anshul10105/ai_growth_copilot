def calculate_metrics(df):
    return {
        "Total Users": len(df),
        "Onboarding Rate": df["onboarding_complete"].mean() * 100,
        "Activation Rate": df["activated"].mean() * 100,
        "Day 1 Retention": df["retained_day1"].mean() * 100,
        "Day 7 Retention": df["retained_day7"].mean() * 100,
        "Referral Rate": df["referred_friend"].mean() * 100,
        "Subscription Rate": df["subscribed"].mean() * 100,
        "Revenue": int(df["revenue"].sum()),
    }
