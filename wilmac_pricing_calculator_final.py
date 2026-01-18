
# Wilmac Technologies Pricing Calculator – Final Version

import streamlit as st

# ---------- Title ----------
st.title("SaaS Pricing Calculator")
st.caption("Estimate annual pricing based on plan, usage, and add-ons")


# ---------- Plan Selection ----------
st.sidebar.header("Step 1: Choose a Plan")
plans = {
    "Launch": {"price": 9900, "volume": "Up to 1M", "storage": "250 GB", "connectors": "Manual Upload Only"},
    "Growth": {"price": 27000, "volume": "Up to 10M", "storage": "2 TB", "connectors": "1 Connector"},
    "Scale": {"price": 75000, "volume": "Up to 50M", "storage": "5 TB", "connectors": "2 Connectors"},
    "Enterprise": {"price": 150000, "volume": "50M+", "storage": "10+ TB", "connectors": "Unlimited Connectors"}
}

plan_choice = st.sidebar.selectbox("Select a Plan", list(plans.keys()))
base_price = plans[plan_choice]["price"]
st.markdown(f"### Selected Plan: {plan_choice}")
st.write(f"💾 Storage: {plans[plan_choice]['storage']}")
st.write(f"📈 Volume: {plans[plan_choice]['volume']}")
st.write(f"🔌 Connectors Included: {plans[plan_choice]['connectors']}")
st.write(f"💰 Base Price: ${base_price:,.0f}")

# ---------- Modality Add-ons ----------
st.sidebar.header("Step 2: Select Modalities (All are add-ons)")
modalities = {
    "Voice": 1250,
    "Screens": 1250,
    "Chat": 1250,
    "Email": 1250,
    "Text/WhatsApp": 1250,
    "Video": 3500
}

modality_selected = st.sidebar.multiselect("Select modalities to include", modalities.keys())
modality_cost = sum([modalities[m] for m in modality_selected])
st.markdown("🧩 **Modalities Selected:**")

if modality_selected:
   st.markdown(" ".join([f"`{m}`" for m in modality_selected]))
else:
    st.write("None")

st.write(f"Modality Add-on Cost: ${modality_cost:,.0f}")

# ---------- Compliance & Analytics ----------
st.sidebar.header("Step 3: Add Compliance & Analytics")
compliance = st.sidebar.checkbox("Compliance Bundle ($6,800/year)")
analytics = st.sidebar.checkbox("Analytics & Reporting Bundle ($7,500/year)")
compliance_cost = 6800 if compliance else 0
analytics_cost = 7500 if analytics else 0
st.write(f"✅ Compliance Bundle: {'Included' if compliance else 'No'}")
st.write(f"📊 Analytics Bundle: {'Included' if analytics else 'No'}")

# ---------- AI Features ----------
st.sidebar.header("Step 4: AI Feature Usage")
transcription_hours = st.sidebar.number_input("Transcription (hrs)", 0, 10000, 0)
real_time_hours = st.sidebar.number_input("Real-Time Transcription (hrs)", 0, 10000, 0)
redaction_minutes = st.sidebar.number_input("Redaction (mins)", 0, 10000, 0)
summarization_minutes = st.sidebar.number_input("Text Summarization (mins)", 0, 10000, 0)
sentiment_analysis = st.sidebar.checkbox("Sentiment Analysis ($250/month flat)")

ai_cost = (
    transcription_hours * 0.70 +
    real_time_hours * 1.20 +
    redaction_minutes * 0.25 +
    min(summarization_minutes * 0.05, 300) +
    (250 * 12 if sentiment_analysis else 0)
)

st.write(f"🧠 AI Features Total: ${ai_cost:,.2f}")

# ---------- Total Cost ----------
total = base_price + modality_cost + compliance_cost + analytics_cost + ai_cost
st.markdown("## 💵 Total Estimated Annual Cost")
st.markdown(f"### ${total:,.2f}")
