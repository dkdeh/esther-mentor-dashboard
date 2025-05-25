import streamlit as st
import json
import os

st.set_page_config(page_title="Mentor Dashboard", layout="centered")
st.title("👩‍🏫 Mentor Dashboard: Support Esther’s Journey")

profile_path = "data/esther_profile.json"
result_path = "data/esther_ai_results.json"

if os.path.exists(profile_path):
    with open(profile_path) as f:
        profile = json.load(f)
else:
    st.error("Esther's profile not found. Please ensure the survey has been completed.")
    st.stop()

st.header("Esther’s Career Direction")
st.markdown(f"**Name:** {profile.get('name', '')}")
st.markdown(f"**Career Interest:** {profile.get('career_interest', '')}")
st.markdown(f"**Dream Class:** {profile.get('custom_class', '')}")
st.markdown(f"**Skills to Grow:** {', '.join(profile.get('skills', []))}")

st.header("How Mentors Can Help")
st.markdown("""
- Share real stories from the field Esther is interested in  
- Recommend hands-on projects or starter kits  
- Suggest free or low-cost tools, videos, or events  
- Help her explore what working in that field looks like  
""")

if os.path.exists(result_path):
    with open(result_path) as f:
        ai_results = json.load(f)
    st.subheader("🎯 AI Mentor Insights")
    st.warning(ai_results.get("mentor_advice", "No AI mentor guidance yet."))
else:
    st.info("Mentor-specific tips from the AI will be added when available.")

st.header("📬 Message Area")
st.text_area("Leave a note, link, or idea to encourage Esther’s exploration.", height=150)

st.markdown("---")
st.caption("Mentor Dashboard | Esther AI Journey")
