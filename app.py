# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                        FinAI · Finance Advisor                              ║
# ║                   AI-Powered Indian Personal Finance App                    ║
# ║                                                                              ║
# ║  Sections in this file (in order):                                           ║
# ║    1. Imports & Page Config                                                  ║
# ║    2. Session State Setup                                                    ║
# ║    3. Global CSS Styling                                                     ║
# ║    4. Navigation Bar                                                         ║
# ║    5. Hero Section + Ticker + Stats + Features                               ║
# ║    6. AI Chat Section                                                        ║
# ║    7. Financial Calculators (SIP / EMI / Retirement)                        ║
# ║    8. Footer                                                                 ║
# ╚══════════════════════════════════════════════════════════════════════════════╝


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 1 · IMPORTS & PAGE CONFIG
# ──────────────────────────────────────────────────────────────────────────────

import streamlit as st
from chatbot1 import chat  # Groq backend that handles AI responses

st.set_page_config(
    page_title="FinAI · Finance Advisor",
    page_icon="💹",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 2 · SESSION STATE SETUP
# Session state persists data across reruns (like a global variable in Streamlit)
# ──────────────────────────────────────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []       # Stores chat history

if "calc_tab" not in st.session_state:
    st.session_state.calc_tab = "SIP"   # Default calculator tab


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 3 · GLOBAL CSS STYLING
# All visual styles are defined here using CSS variables for easy theming.
# Fonts used: Playfair Display (headings), IBM Plex Mono (labels), Outfit (body)
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=IBM+Plex+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap');

/* --- Color Variables --- */
:root {
    --bg:         #080c12;
    --bg2:        #0d1117;
    --surface:    #111820;
    --surface2:   #161e28;
    --surface3:   #1c2636;
    --border:     #1f2d3d;
    --border2:    #253447;
    --text:       #e2e8f2;
    --muted:      #5a7190;
    --muted2:     #7a94b0;
    --accent:     #00d4aa;
    --accent2:    #00a87d;
    --accent-dim: rgba(0,212,170,.08);
    --gold:       #f0b429;
    --red:        #ff5566;
}

/* --- Reset & Base --- */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
    font-family: 'Outfit', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text) !important;
}

/* --- Hide Streamlit default chrome --- */
#MainMenu, footer, header { visibility: hidden !important; }
.block-container { padding: 0 1rem 5rem !important; max-width: 820px !important; }
section[data-testid="stSidebar"] { display: none !important; }

/* --- Navigation Bar --- */
.topnav {
    position: sticky; top: 0; z-index: 999;
    background: rgba(13,17,23,.95); backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
    padding: .75rem 1.5rem;
    display: flex; align-items: center; justify-content: space-between;
    margin: 0 -1rem;
}
.logo-wrap {
    display: flex; align-items: center; gap: 10px;
    font-family: 'Playfair Display', serif; font-size: 1.2rem; color: var(--text);
}
.logo-mark {
    width: 34px; height: 34px; border-radius: 9px;
    background: linear-gradient(135deg, var(--accent), #007a5e);
    display: flex; align-items: center; justify-content: center;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 13px; font-weight: 500; color: #020d09;
}
.nav-badge {
    font-family: 'IBM Plex Mono', monospace; font-size: 10px;
    color: var(--accent); background: var(--accent-dim);
    border: 1px solid rgba(0,212,170,.2); border-radius: 99px; padding: 3px 10px;
}

/* --- Pulse Dot Animation (used in nav and chat header) --- */
.pulse-dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--accent); display: inline-block;
    animation: pulse-anim 2.2s ease-in-out infinite;
}
@keyframes pulse-anim { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.35;transform:scale(.65)} }

/* --- Hero Section --- */
.hero {
    position: relative; padding: 5rem 2rem 4rem;
    text-align: center; overflow: hidden;
}
.hero-bg {
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 60% 50% at 50% 0%, rgba(0,212,170,.07) 0%, transparent 70%);
    pointer-events: none;
}
.hero-grid {
    position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(0,212,170,.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,212,170,.03) 1px, transparent 1px);
    background-size: 50px 50px; pointer-events: none;
}
.hero-eyebrow {
    display: inline-flex; align-items: center; gap: 7px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px; letter-spacing: .18em; text-transform: uppercase;
    color: var(--accent); background: var(--accent-dim);
    border: 1px solid rgba(0,212,170,.2);
    border-radius: 99px; padding: 5px 14px; margin-bottom: 2rem; position: relative;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.8rem, 7vw, 5rem);
    line-height: 1.07; color: var(--text); margin-bottom: 1.4rem; position: relative;
}
.hero-title .italic { font-style: italic; color: var(--accent); }
.hero-sub {
    font-size: 1rem; font-weight: 300; color: var(--muted2);
    max-width: 480px; margin: 0 auto; line-height: 1.8; position: relative;
}

/* --- Ticker Strip (scrolling market data) --- */
.ticker-strip {
    background: var(--surface);
    border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
    padding: 9px 0; overflow: hidden; margin: 2.5rem -1rem;
}
.ticker-inner {
    display: flex; gap: 3rem; white-space: nowrap;
    animation: ticker-scroll 35s linear infinite;
}
@keyframes ticker-scroll { from{transform:translateX(0)} to{transform:translateX(-50%)} }
.t-item {
    font-family: 'IBM Plex Mono', monospace; font-size: 11px;
    display: inline-flex; gap: 8px; align-items: center; color: var(--muted2);
}
.t-sym { color: var(--text); font-weight: 500; }
.t-up  { color: var(--accent); }
.t-dn  { color: var(--red); }

/* --- Stats Row (4 boxes showing key numbers) --- */
.stats-row {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 1px; background: var(--border);
    border: 1px solid var(--border); border-radius: 14px;
    overflow: hidden; margin-bottom: 3rem;
}
.stat-box {
    background: var(--surface); padding: 1.6rem 1rem;
    display: flex; flex-direction: column; gap: 5px; text-align: center;
}
.stat-num { font-family: 'Playfair Display', serif; font-size: 2.2rem; color: var(--text); font-style: italic; }
.stat-num span { color: var(--accent); }
.stat-lbl { font-size: 11px; color: var(--muted); letter-spacing: .04em; }

/* --- Section Header (used before each major block) --- */
.sh { padding: 1rem 0 1.4rem; }
.sh-tag {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px; letter-spacing: .16em; text-transform: uppercase;
    color: var(--accent); margin-bottom: .45rem;
}
.sh-title { font-family: 'Playfair Display', serif; font-size: 1.7rem; font-weight: 700; color: var(--text); line-height: 1.2; }
.sh-sub { font-size: .82rem; color: var(--muted2); margin-top: .35rem; font-weight: 300; }

/* --- Feature Grid (2x2 overview cards) --- */
.feat-grid {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 1px; background: var(--border);
    border: 1px solid var(--border); border-radius: 14px;
    overflow: hidden; margin-bottom: 3rem;
}
.fc { background: var(--surface); padding: 1.6rem; display: flex; flex-direction: column; gap: .65rem; transition: background .2s; }
.fc:hover { background: var(--surface2); }
.ficon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 18px; }
.fi-t { background: rgba(0,212,170,.1);  border: 1px solid rgba(0,212,170,.2); }
.fi-b { background: rgba(77,159,255,.1); border: 1px solid rgba(77,159,255,.2); }
.fi-y { background: rgba(240,180,41,.1); border: 1px solid rgba(240,180,41,.2); }
.fi-r { background: rgba(255,85,102,.1); border: 1px solid rgba(255,85,102,.2); }
.fc-t { font-size: .9rem; font-weight: 600; color: var(--text); }
.fc-d { font-size: .78rem; color: var(--muted2); line-height: 1.75; font-weight: 300; }

/* --- Divider (horizontal line with label between sections) --- */
.divider { display: flex; align-items: center; gap: 1rem; margin: 3rem 0 2rem; }
.dline { flex: 1; height: 1px; background: var(--border); }
.dlabel { font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: .18em; text-transform: uppercase; color: var(--muted); white-space: nowrap; }

/* --- Chat Header Bar --- */
.chat-header {
    background: var(--surface2); border: 1px solid var(--border);
    border-radius: 12px; padding: .9rem 1.3rem; margin-bottom: 1rem;
    display: flex; align-items: center; gap: 12px;
}
.ai-av {
    width: 36px; height: 36px; border-radius: 9px;
    background: linear-gradient(135deg, var(--accent2), #007a5e);
    display: flex; align-items: center; justify-content: center;
    font-family: 'IBM Plex Mono', monospace; font-size: 12px; font-weight: 500; color: #020d09; flex-shrink: 0;
}
.ai-name { font-size: .9rem; font-weight: 600; color: var(--text); }
.ai-sub  { font-size: .68rem; color: var(--muted); }
.online-chip {
    margin-left: auto; display: flex; align-items: center; gap: 5px;
    font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: var(--accent);
    background: var(--accent-dim); border: 1px solid rgba(0,212,170,.2);
    border-radius: 99px; padding: 3px 10px;
}
.odot { width: 6px; height: 6px; border-radius: 50%; background: var(--accent); animation: pulse-anim 2s ease-in-out infinite; }

/* --- Chat Message Bubbles --- */
.msg-user {
    background: var(--accent); color: #020d09;
    border-radius: 12px 12px 3px 12px;
    padding: .85rem 1.1rem; font-size: .85rem; line-height: 1.8; font-weight: 500;
    margin-bottom: .6rem; margin-left: 15%; word-wrap: break-word;
}
.chat-note { text-align: center; font-size: 11px; color: var(--muted); margin-top: .5rem; }

/* --- Calculator Panel & Tabs --- */
.calc-panel { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; overflow: hidden; margin-bottom: 1rem; }
.calc-tabbar { display: flex; border-bottom: 1px solid var(--border); background: var(--bg2); }
.ctab { flex: 1; padding: .9rem .5rem; text-align: center; font-size: .76rem; font-weight: 500; color: var(--muted); border-bottom: 2px solid transparent; }
.ctab.on { color: var(--accent); border-bottom-color: var(--accent); background: var(--accent-dim); }
.calc-title { font-family: 'Playfair Display', serif; font-size: 1.25rem; font-weight: 700; color: var(--text); margin-bottom: .3rem; }
.calc-sub { font-size: .78rem; color: var(--muted2); margin-bottom: 1.5rem; }

/* --- Calculator Result Card --- */
.res-card {
    background: var(--bg2); border: 1px solid var(--border);
    border-top: 2px solid var(--accent); border-radius: 12px;
    padding: 1.6rem; margin-top: 1.5rem; text-align: center;
}
.res-num { font-family: 'Playfair Display', serif; font-size: 2.6rem; font-weight: 700; font-style: italic; color: var(--accent); line-height: 1.1; margin-bottom: .25rem; }
.res-cap { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: .1em; margin-bottom: 1.3rem; }
.res-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; }
.rc { background: var(--surface); padding: .9rem .5rem; text-align: center; }
.rc-v { font-family: 'Playfair Display', serif; font-size: 1.05rem; font-weight: 700; color: var(--text); margin-bottom: .2rem; }
.rc-l { font-size: 10px; color: var(--muted); text-transform: uppercase; letter-spacing: .07em; }

/* --- Streamlit Widget Overrides (inputs, buttons, labels) --- */
div[data-testid="stTextInput"] > div > div > input,
div[data-testid="stNumberInput"] input {
    background: var(--surface3) !important; border: 1.5px solid var(--border2) !important;
    border-radius: 9px !important; color: var(--text) !important;
    font-family: 'Outfit', sans-serif !important; font-size: .87rem !important;
    padding: .72rem .95rem !important; transition: border-color .18s !important;
}
div[data-testid="stTextInput"] > div > div > input:focus,
div[data-testid="stNumberInput"] input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(0,212,170,.09) !important; outline: none !important;
}
div[data-testid="stButton"] > button {
    background: var(--accent) !important; color: #020d09 !important;
    border: none !important; border-radius: 9px !important;
    font-family: 'Outfit', sans-serif !important; font-weight: 600 !important;
    font-size: .84rem !important; padding: .68rem 1.1rem !important;
    transition: all .18s !important; width: 100% !important;
}
div[data-testid="stButton"] > button:hover { background: var(--accent2) !important; transform: translateY(-1px) !important; }
div[data-testid="stButton"] > button:active { transform: translateY(0) !important; }
label, .stTextInput label { color: var(--muted2) !important; font-size: .76rem !important; font-family: 'Outfit', sans-serif !important; font-weight: 500 !important; }
p, .stMarkdown p { color: var(--muted2) !important; font-size: .86rem !important; }
div[data-testid="stNumberInput"] button { background: var(--border2) !important; border: none !important; color: var(--muted2) !important; padding: .2rem .4rem !important; width: auto !important; }
div[data-testid="stNumberInput"] button:hover { background: var(--border) !important; transform: none !important; }
.stColumns [data-testid="column"] { padding: .2rem .3rem !important; }

/* --- AI Response Markdown Styling --- */
.stMarkdown h2 { font-family:'Playfair Display',serif; font-size:1.1rem; color:var(--text) !important; margin:.8rem 0 .4rem; }
.stMarkdown h3 { font-family:'Outfit',sans-serif; font-size:.9rem; color:var(--accent) !important; margin:.6rem 0 .3rem; font-weight:600; }
.stMarkdown ul, .stMarkdown ol { padding-left:1.2rem; margin:.3rem 0; }
.stMarkdown li { font-size:.85rem !important; color:var(--text) !important; line-height:1.7; }
.stMarkdown strong { color:var(--text) !important; }
.stMarkdown hr { border-color:var(--border) !important; margin:.5rem 0 !important; }
.stMarkdown blockquote { border-left:3px solid var(--accent); padding-left:.8rem; color:var(--muted2) !important; font-style:italic; }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 4 · NAVIGATION BAR
# Sticky top bar with logo and region badge
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="topnav">
    <div class="logo-wrap"><div class="logo-mark">FA</div>FinAI</div>
    <div class="nav-badge">India · Personal Finance</div>
</div>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 5 · HERO + TICKER + STATS + FEATURES
# ──────────────────────────────────────────────────────────────────────────────

# --- Market Ticker Data ---
# Format: (Symbol, Price, Change%, IsPositive)
TICKERS = [
    ("SENSEX",    "79,218",    "+0.42%", True),
    ("NIFTY 50",  "24,010",    "+0.38%", True),
    ("BTC/INR",   "52,14,200", "+3.1%",  True),
    ("GOLD",      "72,450",    "-0.2%",  False),
    ("USD/INR",   "83.42",     "-0.05%", False),
    ("RELIANCE",  "2,948",     "+1.1%",  True),
    ("HDFC BANK", "1,612",     "-0.3%",  False),
    ("INFY",      "1,820",     "+0.8%",  True),
    ("TCS",       "4,120",     "+0.5%",  True),
    ("NIFTY BANK","51,200",    "+0.2%",  True),
    ("ETH/INR",   "2,70,450",  "+2.1%",  True),
    ("SILVER",    "88,200",    "+0.3%",  True),
]

# Build ticker HTML: each item shows symbol, price, and colored change
ticker_html = "".join(
    f'<span class="t-item">'
    f'<span class="t-sym">{symbol}</span>'
    f'<span>{price}</span>'
    f'<span class="{"t-up" if is_up else "t-dn"}">{"▲" if is_up else "▼"} {change}</span>'
    f'</span>'
    for symbol, price, change, is_up in TICKERS
)

# Render Hero + Ticker + Stats + Feature Grid
st.markdown(f"""
<div class="hero">
    <div class="hero-bg"></div>
    <div class="hero-grid"></div>
    <div class="hero-eyebrow"><span class="pulse-dot"></span>AI-Powered · Indian Markets · Real Insights</div>
    <h1 class="hero-title">Your money,<br><span class="italic">intelligently</span> guided</h1>
    <p class="hero-sub">Ask anything about SIPs, mutual funds, taxes, EMI, or retirement planning. Expert-level answers — no jargon.</p>
</div>

<!-- Scrolling Market Ticker (duplicated for seamless loop) -->
<div class="ticker-strip">
    <div class="ticker-inner">{ticker_html * 2}</div>
</div>

<!-- Stats Row -->
<div class="stats-row">
    <div class="stat-box"><div class="stat-num"><span>50K</span>+</div><div class="stat-lbl">Questions answered</div></div>
    <div class="stat-box"><div class="stat-num"><span>98</span>%</div><div class="stat-lbl">Satisfaction rate</div></div>
    <div class="stat-box"><div class="stat-num"><span>24</span>/7</div><div class="stat-lbl">Always available</div></div>
    <div class="stat-box"><div class="stat-num"><span>3</span></div><div class="stat-lbl">Calculators</div></div>
</div>

<!-- Features Section Header -->
<div class="sh">
    <div class="sh-tag">What you get</div>
    <div class="sh-title">Everything in one place</div>
    <div class="sh-sub">From beginner budgeting to advanced tax planning</div>
</div>

<!-- Feature Cards Grid (2x2) -->
<div class="feat-grid">
    <div class="fc"><div class="ficon fi-t">💬</div><div class="fc-t">AI Finance Chat</div><div class="fc-d">Ask anything — SIP, ELSS, PPF, NPS, 80C, budgeting. Context-aware answers for Indian investors.</div></div>
    <div class="fc"><div class="ficon fi-y">📊</div><div class="fc-t">SIP Calculator</div><div class="fc-d">See how your monthly SIP grows. Maturity value, returns, and wealth gained — instantly.</div></div>
    <div class="fc"><div class="ficon fi-b">🏠</div><div class="fc-t">EMI Calculator</div><div class="fc-d">Calculate home, car, or personal loan EMIs. Know your total interest before committing.</div></div>
    <div class="fc"><div class="ficon fi-r">🎯</div><div class="fc-t">Retirement Planner</div><div class="fc-d">Inflation-adjusted corpus with a monthly SIP target — know exactly what to save.</div></div>
</div>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# SECTION 6 · AI CHAT SECTION
# ──────────────────────────────────────────────────────────────────────────────

# --- Section divider and header ---
st.markdown("""
<div class="divider"><div class="dline"></div><div class="dlabel">💬 &nbsp; AI Chat</div><div class="dline"></div></div>
<div class="sh">
    <div class="sh-tag">AI Advisor</div>
    <div class="sh-title">Chat with FinAI</div>
    <div class="sh-sub">Specialized in Indian personal finance — ask anything</div>
</div>
<div class="chat-header">
    <div class="ai-av">AI</div>
    <div><div class="ai-name">FinAI Advisor</div><div class="ai-sub">Powered by LLaMA 3.3-70B · Groq</div></div>
    <div class="online-chip"><div class="odot"></div> Online</div>
</div>
""", unsafe_allow_html=True)

# --- Quick Topic Chips ---
# Clicking a topic auto-sends a pre-written question to the chat
TOPICS = [
    ("📈", "SIP & Mutual Funds"),
    ("🧾", "Tax Planning 80C"),
    ("🏠", "Home Loan & EMI"),
    ("🎯", "Retirement Planning"),
    ("₿",  "Crypto in India"),
    ("📊", "Portfolio Strategy"),
    ("🔄", "ELSS vs PPF"),
    ("💡", "Index Funds"),
]

topic_cols = st.columns(4)  # 4 columns = 2 rows of 4 chips

for i, (icon, label) in enumerate(TOPICS):
    with topic_cols[i % 4]:
        if st.button(f"{icon} {label}", key=f"tp_{i}", use_container_width=True):
            question = f"Explain {label} in the Indian personal finance context"
            st.session_state.messages.append({"role": "user", "content": question})
            with st.spinner("FinAI is thinking…"):
                response = chat(question)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

# --- Chat Message Display ---
if not st.session_state.messages:
    # Show placeholder when no messages yet
    st.markdown(
        '<p style="text-align:center;color:#5a7190;font-style:italic;padding:1.2rem 0 .5rem">'
        'Start a conversation below ↓</p>',
        unsafe_allow_html=True
    )
else:
    for message in st.session_state.messages:
        if message["role"] == "user":
            # User message: styled teal bubble
            st.markdown(f'<div class="msg-user">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            # AI response: rendered as native Streamlit markdown (supports bold, lists, headers)
            st.markdown(message["content"])

# --- Chat Input Row ---
st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

input_col, send_col, clear_col = st.columns([6, 1.5, 1])

with input_col:
    user_input = st.text_input(
        "", placeholder="Ask about SIP, taxes, mutual funds, EMI…",
        key="chat_input", label_visibility="collapsed"
    )
with send_col:
    send_clicked = st.button("Send →", key="send_btn", use_container_width=True)

with clear_col:
    if st.button("Clear", key="clear_btn", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- Handle Send Button ---
if send_clicked and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("FinAI is thinking…"):
        response = chat(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()

# Disclaimer below chat
st.markdown(
    '<div class="chat-note">⚠ For educational purposes only — not SEBI-registered financial advice</div>',
    unsafe_allow_html=True
)


# ============================================================
# SECTION 7 · FINANCIAL CALCULATORS
# Three calculators: SIP, EMI, Retirement Planner
# ============================================================

import streamlit as st  # Import streamlit to build the web app

# ----- Show the section heading on the page -----
st.markdown("""
<div class="divider"><div class="dline"></div><div class="dlabel">🧮 &nbsp; Calculators</div><div class="dline"></div></div>
<div class="sh">
    <div class="sh-tag">Plan with precision</div>
    <div class="sh-title">Financial Calculators</div>
    <div class="sh-sub">Real formulas, instant results</div>
</div>
""", unsafe_allow_html=True)

# ----- Read which tab is currently active from session state -----
# session_state remembers values even when the page re-runs
active_tab = st.session_state.calc_tab  # Will be "SIP", "EMI", or "Retirement"

# ----- Show the visual tab bar (just for looks, HTML only) -----
# We highlight the active tab by adding class "on" to it
sip_class        = "on" if active_tab == "SIP"        else ""  # "on" = highlighted
emi_class        = "on" if active_tab == "EMI"        else ""
retirement_class = "on" if active_tab == "Retirement" else ""

st.markdown(f"""
<div class="calc-panel">
  <div class="calc-tabbar">
    <div class="ctab {sip_class}">📈 SIP Calculator</div>
    <div class="ctab {emi_class}">🏠 EMI Calculator</div>
    <div class="ctab {retirement_class}">🎯 Retirement Planner</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ----- Real clickable buttons to switch tabs -----
# Streamlit can't click HTML, so we need actual buttons
tab_col1, tab_col2, tab_col3 = st.columns(3)  # 3 equal columns side by side

with tab_col1:
    if st.button("📈 SIP Calculator", key="tab_sip", use_container_width=True):
        st.session_state.calc_tab = "SIP"  # Save the clicked tab
        st.rerun()                          # Refresh the page to show SIP section

with tab_col2:
    if st.button("🏠 EMI Calculator", key="tab_emi", use_container_width=True):
        st.session_state.calc_tab = "EMI"  # Save the clicked tab
        st.rerun()                          # Refresh the page to show EMI section

with tab_col3:
    if st.button("🎯 Retirement Planner", key="tab_ret", use_container_width=True):
        st.session_state.calc_tab = "Retirement"  # Save the clicked tab
        st.rerun()                                  # Refresh to show Retirement section

st.markdown("<br>", unsafe_allow_html=True)  # Add a small gap below buttons


# ============================================================
# HELPER: Format big numbers in Indian style (Lakh / Crore)
# Example: 1500000 → ₹15.00 L,  10000000 → ₹1.00 Cr
# ============================================================

def fmt(amount):
    amount = round(amount)                     # Round off to nearest rupee

    if amount >= 1_00_00_000:                 # 1 Crore = 1,00,00,000
        return f"₹{amount / 1_00_00_000:.2f} Cr"

    if amount >= 1_00_000:                    # 1 Lakh = 1,00,000
        return f"₹{amount / 1_00_000:.2f} L"

    return f"₹{amount:,}"                     # Below 1 Lakh → show with commas


# ============================================================
# TAB 1: SIP CALCULATOR
# Formula: FV = P × [((1+r)^n − 1) / r] × (1+r)
#   P = monthly investment
#   r = monthly interest rate (annual rate ÷ 12 ÷ 100)
#   n = total number of months
# ============================================================

if active_tab == "SIP":

    # Show title and description
    st.markdown(
        '<div class="calc-title">SIP Calculator</div>'
        '<div class="calc-sub">How much will your monthly SIP grow to over time?</div>',
        unsafe_allow_html=True
    )

    # Input fields in 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        monthly = st.number_input(
            "Monthly Investment (₹)",
            min_value=500, max_value=1_000_000,
            value=5_000, step=500, key="sip_m"
        )  # How much you invest every month

    with col2:
        rate = st.number_input(
            "Expected Return (% p.a.)",
            min_value=1.0, max_value=30.0,
            value=12.0, step=0.5, key="sip_r"
        )  # Annual return rate you expect

    with col3:
        years = st.number_input(
            "Period (years)",
            min_value=1, max_value=40,
            value=10, step=1, key="sip_y"
        )  # Number of years you will invest

    # When user clicks Calculate
    if st.button("Calculate →", key="sip_go", use_container_width=True):

        # Step 1: Convert annual rate to monthly rate
        monthly_rate = rate / 100 / 12       # e.g. 12% → 0.01 per month

        # Step 2: Total number of months
        total_months = int(years * 12)        # e.g. 10 years → 120 months

        # Step 3: Apply SIP future value formula
        future_value = monthly * (((1 + monthly_rate) ** total_months - 1) / monthly_rate) * (1 + monthly_rate)

        # Step 4: Calculate how much YOU put in (no interest)
        amount_invested = monthly * total_months   # Simple multiplication

        # Step 5: Profit = final value - what you put in
        est_returns = future_value - amount_invested

        # Step 6: Gain % = profit ÷ invested × 100
        gain_percent = est_returns / amount_invested * 100

        # Show the result card
        st.markdown(f"""
        <div class="res-card">
            <div class="res-num">{fmt(future_value)}</div>
            <div class="res-cap">Total maturity value</div>
            <div class="res-row">
                <div class="rc"><div class="rc-v">{fmt(amount_invested)}</div><div class="rc-l">Amount Invested</div></div>
                <div class="rc"><div class="rc-v" style="color:var(--accent)">{fmt(est_returns)}</div><div class="rc-l">Est. Returns</div></div>
                <div class="rc"><div class="rc-v" style="color:var(--gold)">{gain_percent:.1f}%</div><div class="rc-l">Total Gain</div></div>
            </div>
        </div>""", unsafe_allow_html=True)


# ============================================================
# TAB 2: EMI CALCULATOR
# Formula: EMI = P × r × (1+r)^n / ((1+r)^n − 1)
#   P = loan amount (principal)
#   r = monthly interest rate
#   n = total number of months
# ============================================================

elif active_tab == "EMI":

    # Show title and description
    st.markdown(
        '<div class="calc-title">EMI Calculator</div>'
        '<div class="calc-sub">What will your monthly loan repayment be?</div>',
        unsafe_allow_html=True
    )

    # Input fields in 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        principal = st.number_input(
            "Loan Amount (₹)",
            min_value=10_000, max_value=100_000_000,
            value=2_000_000, step=10_000, key="emi_p"
        )  # Total loan amount you are taking

    with col2:
        rate_i = st.number_input(
            "Interest Rate (% p.a.)",
            min_value=1.0, max_value=30.0,
            value=8.5, step=0.1, key="emi_r"
        )  # Annual interest rate on the loan

    with col3:
        tenure = st.number_input(
            "Tenure (years)",
            min_value=1, max_value=30,
            value=20, step=1, key="emi_t"
        )  # How many years to repay the loan

    # When user clicks Calculate
    if st.button("Calculate →", key="emi_go", use_container_width=True):

        # Step 1: Convert annual rate to monthly rate
        monthly_rate = rate_i / 100 / 12     # e.g. 8.5% → 0.00708 per month

        # Step 2: Total number of months
        total_months = int(tenure * 12)       # e.g. 20 years → 240 months

        # Step 3: Apply EMI formula
        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** total_months
            / ((1 + monthly_rate) ** total_months - 1)
        )

        # Step 4: Total amount you'll pay over all months
        total_payment = emi * total_months

        # Step 5: Total interest = total paid - original loan
        total_interest = total_payment - principal

        # Show the result card
        st.markdown(f"""
        <div class="res-card">
            <div class="res-num">₹{emi:,.0f}<span style="font-size:.9rem;color:var(--muted);font-style:normal"> /mo</span></div>
            <div class="res-cap">Monthly EMI</div>
            <div class="res-row">
                <div class="rc"><div class="rc-v">{fmt(principal)}</div><div class="rc-l">Principal</div></div>
                <div class="rc"><div class="rc-v" style="color:var(--red)">{fmt(total_interest)}</div><div class="rc-l">Total Interest</div></div>
                <div class="rc"><div class="rc-v">{fmt(total_payment)}</div><div class="rc-l">Total Payment</div></div>
            </div>
        </div>""", unsafe_allow_html=True)


# ============================================================
# TAB 3: RETIREMENT PLANNER
# 3 steps:
#   Step 1 → How much will your expenses be at retirement? (inflation adjusted)
#   Step 2 → How big a savings corpus (total money) do you need?
#   Step 3 → How much SIP per month do you need to reach that corpus?
# ============================================================

elif active_tab == "Retirement":

    # Show title and description
    st.markdown(
        '<div class="calc-title">Retirement Planner</div>'
        '<div class="calc-sub">How much corpus do you need to retire comfortably?</div>',
        unsafe_allow_html=True
    )

    # Input fields in 2 columns
    col1, col2 = st.columns(2)

    with col1:
        current_age = st.number_input(
            "Current Age",
            min_value=18, max_value=60,
            value=25, step=1, key="r_ca"
        )  # Your age right now

        retire_age = st.number_input(
            "Retirement Age",
            min_value=45, max_value=75,
            value=60, step=1, key="r_ra"
        )  # Age at which you want to retire

        monthly_exp = st.number_input(
            "Monthly Expenses Today (₹)",
            min_value=5_000, max_value=500_000,
            value=30_000, step=1_000, key="r_me"
        )  # What you spend per month RIGHT NOW

    with col2:
        inflation = st.number_input(
            "Expected Inflation (% p.a.)",
            min_value=1.0, max_value=15.0,
            value=6.0, step=0.5, key="r_inf"
        )  # How fast prices rise every year

        inv_return = st.number_input(
            "Investment Return (% p.a.)",
            min_value=1.0, max_value=20.0,
            value=12.0, step=0.5, key="r_ret"
        )  # Expected return from your SIP investments

        life_exp = st.number_input(
            "Life Expectancy",
            min_value=70, max_value=100,
            value=85, step=1, key="r_le"
        )  # How long you expect to live

    # When user clicks Plan
    if st.button("Plan My Retirement →", key="ret_go", use_container_width=True):

        # Basic time calculations
        years_to_retire = retire_age - current_age   # Years left before retirement
        years_in_retire = life_exp - retire_age       # Years you'll spend in retirement

        # Safety check: retirement age must be in the future
        if years_to_retire <= 0:
            st.error("Retirement age must be greater than current age.")

        else:
            # ── STEP 1: Inflate today's expenses to retirement date ──
            # Your ₹30,000 today will cost much more after inflation
            # Formula: Future Value = Present Value × (1 + inflation rate)^years
            future_monthly = monthly_exp * (1 + inflation / 100) ** years_to_retire

            # ── STEP 2: Total corpus needed ──
            # Simple estimate: inflated monthly expense × 12 months × retirement years
            corpus_needed = future_monthly * 12 * years_in_retire

            # ── STEP 3: Monthly SIP to reach that corpus ──
            # This is the reverse of the SIP formula — we know the target, find the monthly amount
            r_monthly  = inv_return / 100 / 12         # Monthly investment return rate
            n_months   = years_to_retire * 12           # Total months of investing
            sip_needed = corpus_needed * r_monthly / (((1 + r_monthly) ** n_months) - 1)

            # Show the result card
            st.markdown(f"""
            <div class="res-card">
                <div class="res-num">{fmt(corpus_needed)}</div>
                <div class="res-cap">Retirement corpus required</div>
                <div class="res-row">
                    <div class="rc"><div class="rc-v">{fmt(future_monthly)}</div><div class="rc-l">Monthly Exp. at Retirement</div></div>
                    <div class="rc"><div class="rc-v" style="color:var(--accent)">₹{sip_needed:,.0f}</div><div class="rc-l">Monthly SIP Needed</div></div>
                    <div class="rc"><div class="rc-v" style="color:var(--gold)">{years_to_retire} yrs</div><div class="rc-l">Years to Save</div></div>
                </div>
            </div>""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# SECTION 8 · FOOTER
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<div style="border-top:1px solid #1f2d3d;margin-top:3rem;padding:2.5rem 0 1.5rem;text-align:center;">
    <div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-style:italic;color:#e2e8f2;margin-bottom:.6rem;">FinAI</div>
    <p style="font-size:11px !important;color:#5a7190 !important;line-height:2.2 !important;">
        ⚠ For <strong style="color:#7a94b0">educational purposes only.</strong>
        Not SEBI-registered financial advice.<br>
        Always consult a qualified advisor before making investment decisions.
    </p>
</div>
""", unsafe_allow_html=True)