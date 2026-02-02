import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Aviator Trend Analyzer", layout="centered")

st.title("🚁 Aviator Strategy Helper")
st.markdown("### Pattern & Interval Analyzer")

# User Inputs
last_pink_time = st.text_input("Time of Last Pink (HH:MM:SS):", "20:01:56")
st.subheader("Last 3 Multipliers")
m1 = st.number_input("Most Recent Round:", value=9.41, step=0.1)
m2 = st.number_input("Second Recent Round:", value=3.42, step=0.1)
m3 = st.number_input("Third Recent Round:", value=1.46, step=0.1)

if st.button("Analyze Current Cycle"):
    # 1. Interval Calculation
    fmt = '%H:%M:%S'
    last_pink = datetime.strptime(last_pink_time, fmt)
    next_win = last_pink + timedelta(minutes=10)
    
    # 2. Pattern Detection Logic
    is_staircase = m1 > m2 > m3
    is_shadow = 8.0 <= m1 <= 9.99
    
    st.divider()
    
    # Logic Output
    st.write(f"📊 **Macro Cycle Alert:** Next major 10m window starts around **{next_win.strftime(fmt)}**")
    
    if is_staircase:
        st.success("🔥 STAIRCASE DETECTED: Multipliers are trending UP. Probability of a 'Breakout Pink' is HIGH.")
    
    if is_shadow:
        st.warning("⚠️ SHADOW PINK: The last round nearly hit 10x. The system is 'shaving' profit. Use a 5x Auto-Cashout.")

    if m1 < 1.2 and m2 < 1.2:
        st.error("❄️ COLLECTION MODE: Two 'Instant Crashes' detected. STOP betting for 3-5 minutes.")

st.info("Disclaimer: This tool uses community patterns and probability. It cannot guarantee results as Aviator uses RNG.")
