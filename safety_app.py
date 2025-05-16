import streamlit as st
import numpy as np

st.title("🛡️ School Stop Safety Tool")

st.header("🚏 Stop Safety Evaluation")

# User inputs
road_type = st.selectbox("Road Type", ["residential", "arterial", "intersection"])
lighting = st.slider("Lighting Score", 1, 5, 3)
visibility = st.slider("Visibility Score", 1, 5, 3)
intersection = st.slider("Intersection Risk", 1, 5, 3)
weather = st.slider("Weather Risk", 1, 5, 3)

# Safety scoring formula
road_scores = {"residential": 1, "arterial": 3, "intersection": 5}
road_score = road_scores[road_type]

stop_score = (
    road_score * 0.4 +
    lighting * 0.3 +
    visibility * 0.2 +
    intersection * 0.1
)

# Display score
st.subheader("✅ Stop Safety Score")
st.write(f"**{stop_score:.2f}**")

if stop_score > 6.5:
    st.warning("⚠️ High Crash Risk Detected")
else:
    st.success("🟢 Stop is Relatively Safe")

# Community impact section
st.header("🚐 Community Risk Impact")

evan_rate = st.slider("E-Van Adoption Rate", 0.0, 1.0, 0.3)
teen_driver_rate = st.slider("Teen/Parent Driver Rate", 0.0, 1.0, 0.5)

# Risk model formula
risk_score = (teen_driver_rate * 5) - (evan_rate * 3) - (stop_score * 2)

st.subheader("📉 Estimated Community Risk Score")
st.write(f"**{risk_score:.2f}**  (Lower is better)")
