import datetime

# User History Data
history = [
    {"mult": 22.85, "time": "23:20:15"}, # Pink 1
    {"mult": 2.19,  "time": "23:21:08"}, 
    {"mult": 2.91,  "time": "23:21:36"}, 
    {"mult": 1.73,  "time": "23:22:07"}, 
    {"mult": 11.07, "time": "23:24:27"}, # Pink 2
    {"mult": 1.47,  "time": "23:25:12"}, 
    {"mult": 1.00,  "time": "23:25:36"}, 
    {"mult": 4.85,  "time": "23:25:56"}  # Last round
]

def check_pink_signals(data):
    # 1. TIME-BASED ALERT: 4-5 MINUTE RULE
    # Patterns often repeat at 4-5 minute intervals.
    last_pink = [r for r in data if r["mult"] >= 10.0][-1]
    lp_time = datetime.datetime.strptime(last_pink["time"], "%H:%M:%S")
    current_time = datetime.datetime.strptime("23:28:45", "%H:%M:%S") # Simulate current time
    time_diff = (current_time - lp_time).total_seconds() / 60
    
    is_timing_window = 4.0 <= time_diff <= 5.5

    # 2. SEQUENCE TRIGGER: 3-BLUE RECOVERY
    # High multipliers often follow 3+ "Blue" rounds (below 2.0x).
    recent_mults = [r["mult"] for r in data[-3:]]
    blues_count = sum(1 for m in recent_mults if m < 2.0)
    
    # 3. RECOVERY TRIGGER: THE FEEDER ROUND
    # A multiplier between 4x and 8x often "feeds" a coming Pink.
    last_mult = data[-1]["mult"]
    is_feeder = 4.0 <= last_mult < 10.0

    # SIGNAL OUTPUT
    if is_timing_window and (blues_count >= 2 or is_feeder):
        return "🔥 SIGNAL: HIGH PROBABILITY. Time interval and sequence aligned."
    elif is_timing_window:
        return "⚠️ SIGNAL: Timing window active. Watch for next sequence trigger."
    elif is_feeder:
        return "⚡ SIGNAL: Feeder round detected (4.85x). Wait for timing window."
    else:
        return "--- STATUS: Pattern developing. No active signal."

print(check_pink_signals(history))
