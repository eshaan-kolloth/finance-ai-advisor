import streamlit as st
from chatbot1 import chat  # ← your Groq backend

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FinAI · Finance Advisor",
    page_icon="💹",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Session state ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state: st.session_state.messages = []
if "calc_tab" not in st.session_state: st.session_state.calc_tab = "SIP"

# ══════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=IBM+Plex+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap');

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

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
    font-family: 'Outfit', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text) !important;
}

#MainMenu, footer, header { visibility: hidden !important; }
.block-container { padding: 0 1rem 5rem !important; max-width: 820px !important; }
section[data-testid="stSidebar"] { display: none !important; }

/* NAV */
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
.pulse-dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--accent); display: inline-block;
    animation: pulse-anim 2.2s ease-in-out infinite;
}
@keyframes pulse-anim { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.35;transform:scale(.65)} }

/* HERO */
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

/* TICKER */
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

/* STATS */
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

/* SECTION HEADER */
.sh { padding: 1rem 0 1.4rem; }
.sh-tag {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px; letter-spacing: .16em; text-transform: uppercase;
    color: var(--accent); margin-bottom: .45rem;
}
.sh-title { font-family: 'Playfair Display', serif; font-size: 1.7rem; font-weight: 700; color: var(--text); line-height: 1.2; }
.sh-sub { font-size: .82rem; color: var(--muted2); margin-top: .35rem; font-weight: 300; }

/* FEATURE GRID */
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

/* DIVIDER */
.divider { display: flex; align-items: center; gap: 1rem; margin: 3rem 0 2rem; }
.dline { flex: 1; height: 1px; background: var(--border); }
.dlabel { font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: .18em; text-transform: uppercase; color: var(--muted); white-space: nowrap; }

/* CHAT HEADER */
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

/* MESSAGES */
.msg-user {
    background: var(--accent); color: #020d09;
    border-radius: 12px 12px 3px 12px;
    padding: .85rem 1.1rem; font-size: .85rem; line-height: 1.8; font-weight: 500;
    margin-bottom: .6rem; margin-left: 15%; word-wrap: break-word;
}
.chat-note { text-align: center; font-size: 11px; color: var(--muted); margin-top: .5rem; }

/* CALC */
.calc-panel { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; overflow: hidden; margin-bottom: 1rem; }
.calc-tabbar { display: flex; border-bottom: 1px solid var(--border); background: var(--bg2); }
.ctab { flex: 1; padding: .9rem .5rem; text-align: center; font-size: .76rem; font-weight: 500; color: var(--muted); border-bottom: 2px solid transparent; }
.ctab.on { color: var(--accent); border-bottom-color: var(--accent); background: var(--accent-dim); }
.calc-title { font-family: 'Playfair Display', serif; font-size: 1.25rem; font-weight: 700; color: var(--text); margin-bottom: .3rem; }
.calc-sub { font-size: .78rem; color: var(--muted2); margin-bottom: 1.5rem; }
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

/* STREAMLIT OVERRIDES */
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

/* AI response markdown styling */
.stMarkdown h2 { font-family:'Playfair Display',serif; font-size:1.1rem; color:var(--text) !important; margin:.8rem 0 .4rem; }
.stMarkdown h3 { font-family:'Outfit',sans-serif; font-size:.9rem; color:var(--accent) !important; margin:.6rem 0 .3rem; font-weight:600; }
.stMarkdown ul, .stMarkdown ol { padding-left:1.2rem; margin:.3rem 0; }
.stMarkdown li { font-size:.85rem !important; color:var(--text) !important; line-height:1.7; }
.stMarkdown strong { color:var(--text) !important; }
.stMarkdown hr { border-color:var(--border) !important; margin:.5rem 0 !important; }
.stMarkdown blockquote { border-left:3px solid var(--accent); padding-left:.8rem; color:var(--muted2) !important; font-style:italic; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# NAV
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="topnav">
    <div class="logo-wrap"><div class="logo-mark">FA</div>FinAI</div>
    <div class="nav-badge">India · Personal Finance</div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HERO + TICKER + STATS + FEATURES
# ══════════════════════════════════════════════════════════════════════════════
TICKERS = [
    ("SENSEX","79,218","+0.42%",True), ("NIFTY 50","24,010","+0.38%",True),
    ("BTC/INR","52,14,200","+3.1%",True), ("GOLD","72,450","-0.2%",False),
    ("USD/INR","83.42","-0.05%",False), ("RELIANCE","2,948","+1.1%",True),
    ("HDFC BANK","1,612","-0.3%",False), ("INFY","1,820","+0.8%",True),
    ("TCS","4,120","+0.5%",True), ("NIFTY BANK","51,200","+0.2%",True),
    ("ETH/INR","2,70,450","+2.1%",True), ("SILVER","88,200","+0.3%",True),
]
ticker_html = "".join(
    f'<span class="t-item"><span class="t-sym">{s}</span><span>{p}</span>'
    f'<span class="{"t-up" if u else "t-dn"}">{"▲" if u else "▼"} {c}</span></span>'
    for s, p, c, u in TICKERS
)

st.markdown(f"""
<div class="hero">
    <div class="hero-bg"></div><div class="hero-grid"></div>
    <div class="hero-eyebrow"><span class="pulse-dot"></span>AI-Powered · Indian Markets · Real Insights</div>
    <h1 class="hero-title">Your money,<br><span class="italic">intelligently</span> guided</h1>
    <p class="hero-sub">Ask anything about SIPs, mutual funds, taxes, EMI, or retirement planning. Expert-level answers — no jargon.</p>
</div>
<div class="ticker-strip"><div class="ticker-inner">{ticker_html * 2}</div></div>
<div class="stats-row">
    <div class="stat-box"><div class="stat-num"><span>50K</span>+</div><div class="stat-lbl">Questions answered</div></div>
    <div class="stat-box"><div class="stat-num"><span>98</span>%</div><div class="stat-lbl">Satisfaction rate</div></div>
    <div class="stat-box"><div class="stat-num"><span>24</span>/7</div><div class="stat-lbl">Always available</div></div>
    <div class="stat-box"><div class="stat-num"><span>3</span></div><div class="stat-lbl">Calculators</div></div>
</div>
<div class="sh">
    <div class="sh-tag">What you get</div>
    <div class="sh-title">Everything in one place</div>
    <div class="sh-sub">From beginner budgeting to advanced tax planning</div>
</div>
<div class="feat-grid">
    <div class="fc"><div class="ficon fi-t">💬</div><div class="fc-t">AI Finance Chat</div><div class="fc-d">Ask anything — SIP, ELSS, PPF, NPS, 80C, budgeting. Context-aware answers for Indian investors.</div></div>
    <div class="fc"><div class="ficon fi-y">📊</div><div class="fc-t">SIP Calculator</div><div class="fc-d">See how your monthly SIP grows. Maturity value, returns, and wealth gained — instantly.</div></div>
    <div class="fc"><div class="ficon fi-b">🏠</div><div class="fc-t">EMI Calculator</div><div class="fc-d">Calculate home, car, or personal loan EMIs. Know your total interest before committing.</div></div>
    <div class="fc"><div class="ficon fi-r">🎯</div><div class="fc-t">Retirement Planner</div><div class="fc-d">Inflation-adjusted corpus with a monthly SIP target — know exactly what to save.</div></div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CHAT SECTION
# ══════════════════════════════════════════════════════════════════════════════
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

# ── Topic chips: 4-column grid = clean 2 rows of 4 ────────────────────────────
TOPICS = [
    ("📈", "SIP & Mutual Funds"), ("🧾", "Tax Planning 80C"),
    ("🏠", "Home Loan & EMI"),   ("🎯", "Retirement Planning"),
    ("₿",  "Crypto in India"),   ("📊", "Portfolio Strategy"),
    ("🔄", "ELSS vs PPF"),       ("💡", "Index Funds"),
]
topic_cols = st.columns(4)
for i, (icon, label) in enumerate(TOPICS):
    with topic_cols[i % 4]:
        if st.button(f"{icon} {label}", key=f"tp_{i}", use_container_width=True):
            q = f"Explain {label} in the Indian personal finance context"
            st.session_state.messages.append({"role": "user", "content": q})
            with st.spinner("FinAI is thinking…"):
                rep = chat(q)
            st.session_state.messages.append({"role": "assistant", "content": rep})
            st.rerun()

st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

# ── Messages ───────────────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown(
        '<p style="text-align:center;color:#5a7190;font-style:italic;padding:1.2rem 0 .5rem">'
        'Start a conversation below ↓</p>',
        unsafe_allow_html=True
    )
else:
    for m in st.session_state.messages:
        if m["role"] == "user":
            # user bubble in teal
            st.markdown(f'<div class="msg-user">{m["content"]}</div>', unsafe_allow_html=True)
        else:
            # AI reply: let Streamlit render markdown (bold, lists, headers, ---) natively
            st.markdown(m["content"])

# ── Input row ──────────────────────────────────────────────────────────────────
st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
ci, cs, cc = st.columns([6, 1.5, 1])
with ci:
    user_in = st.text_input(
        "", placeholder="Ask about SIP, taxes, mutual funds, EMI…",
        key="chat_input", label_visibility="collapsed"
    )
with cs:
    send = st.button("Send →", key="send_btn", use_container_width=True)
with cc:
    if st.button("Clear", key="clear_btn", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if send and user_in.strip():
    st.session_state.messages.append({"role": "user", "content": user_in})
    with st.spinner("FinAI is thinking…"):
        rep = chat(user_in)
    st.session_state.messages.append({"role": "assistant", "content": rep})
    st.rerun()

st.markdown(
    '<div class="chat-note">⚠ For educational purposes only — not SEBI-registered financial advice</div>',
    unsafe_allow_html=True
)


# ══════════════════════════════════════════════════════════════════════════════
# CALCULATORS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="divider"><div class="dline"></div><div class="dlabel">🧮 &nbsp; Calculators</div><div class="dline"></div></div>
<div class="sh">
    <div class="sh-tag">Plan with precision</div>
    <div class="sh-title">Financial Calculators</div>
    <div class="sh-sub">Real formulas, instant results</div>
</div>
""", unsafe_allow_html=True)

tab = st.session_state.calc_tab
def _s(t): return "on" if tab == t else ""

st.markdown(f"""
<div class="calc-panel">
  <div class="calc-tabbar">
    <div class="ctab {_s('SIP')}">📈 SIP Calculator</div>
    <div class="ctab {_s('EMI')}">🏠 EMI Calculator</div>
    <div class="ctab {_s('Retirement')}">🎯 Retirement Planner</div>
  </div>
</div>
""", unsafe_allow_html=True)

tc1, tc2, tc3 = st.columns(3)
with tc1:
    if st.button("📈 SIP Calculator",     key="tab_sip", use_container_width=True): st.session_state.calc_tab = "SIP"; st.rerun()
with tc2:
    if st.button("🏠 EMI Calculator",     key="tab_emi", use_container_width=True): st.session_state.calc_tab = "EMI"; st.rerun()
with tc3:
    if st.button("🎯 Retirement Planner", key="tab_ret", use_container_width=True): st.session_state.calc_tab = "Retirement"; st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

def fmt(x):
    x = round(x)
    if x >= 1_00_00_000: return f"₹{x/1_00_00_000:.2f} Cr"
    if x >= 1_00_000:    return f"₹{x/1_00_000:.2f} L"
    return f"₹{x:,}"

# ── SIP ────────────────────────────────────────────────────────────────────────
if tab == "SIP":
    st.markdown('<div class="calc-title">SIP Calculator</div><div class="calc-sub">How much will your monthly SIP grow to over time?</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: monthly = st.number_input("Monthly Investment (₹)", 500, 1_000_000, 5_000, 500, key="sip_m")
    with c2: rate    = st.number_input("Expected Return (% p.a.)", 1.0, 30.0, 12.0, 0.5, key="sip_r")
    with c3: years   = st.number_input("Period (years)", 1, 40, 10, 1, key="sip_y")
    if st.button("Calculate →", key="sip_go", use_container_width=True):
        r = rate / 100 / 12; n = int(years * 12)
        fv = monthly * (((1 + r) ** n - 1) / r) * (1 + r)
        iv = monthly * n; re = fv - iv; gp = re / iv * 100
        st.markdown(f"""<div class="res-card">
            <div class="res-num">{fmt(fv)}</div><div class="res-cap">Total maturity value</div>
            <div class="res-row">
                <div class="rc"><div class="rc-v">{fmt(iv)}</div><div class="rc-l">Amount Invested</div></div>
                <div class="rc"><div class="rc-v" style="color:var(--accent)">{fmt(re)}</div><div class="rc-l">Est. Returns</div></div>
                <div class="rc"><div class="rc-v" style="color:var(--gold)">{gp:.1f}%</div><div class="rc-l">Total Gain</div></div>
            </div></div>""", unsafe_allow_html=True)

# ── EMI ────────────────────────────────────────────────────────────────────────
elif tab == "EMI":
    st.markdown('<div class="calc-title">EMI Calculator</div><div class="calc-sub">What will your monthly loan repayment be?</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: principal = st.number_input("Loan Amount (₹)", 10_000, 100_000_000, 2_000_000, 10_000, key="emi_p")
    with c2: rate_i    = st.number_input("Interest Rate (% p.a.)", 1.0, 30.0, 8.5, 0.1, key="emi_r")
    with c3: tenure    = st.number_input("Tenure (years)", 1, 30, 20, 1, key="emi_t")
    if st.button("Calculate →", key="emi_go", use_container_width=True):
        r = rate_i / 100 / 12; n = int(tenure * 12)
        emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
        tot = emi * n; int_paid = tot - principal
        st.markdown(f"""<div class="res-card">
            <div class="res-num">₹{emi:,.0f}<span style="font-size:.9rem;color:var(--muted);font-style:normal"> /mo</span></div>
            <div class="res-cap">Monthly EMI</div>
            <div class="res-row">
                <div class="rc"><div class="rc-v">{fmt(principal)}</div><div class="rc-l">Principal</div></div>
                <div class="rc"><div class="rc-v" style="color:var(--red)">{fmt(int_paid)}</div><div class="rc-l">Total Interest</div></div>
                <div class="rc"><div class="rc-v">{fmt(tot)}</div><div class="rc-l">Total Payment</div></div>
            </div></div>""", unsafe_allow_html=True)

# ── RETIREMENT ─────────────────────────────────────────────────────────────────
elif tab == "Retirement":
    st.markdown('<div class="calc-title">Retirement Planner</div><div class="calc-sub">How much corpus do you need to retire comfortably?</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        cur_age     = st.number_input("Current Age",                    18,  60,  25, 1,      key="r_ca")
        ret_age     = st.number_input("Retirement Age",                 45,  75,  60, 1,      key="r_ra")
        monthly_exp = st.number_input("Monthly Expenses Today (₹)", 5_000, 500_000, 30_000, 1_000, key="r_me")
    with c2:
        inflation   = st.number_input("Expected Inflation (% p.a.)", 1.0, 15.0,  6.0, 0.5, key="r_inf")
        inv_return  = st.number_input("Investment Return (% p.a.)",  1.0, 20.0, 12.0, 0.5, key="r_ret")
        life_exp    = st.number_input("Life Expectancy",             70,  100,   85,  1,    key="r_le")
    if st.button("Plan My Retirement →", key="ret_go", use_container_width=True):
        ytr = ret_age - cur_age; yir = life_exp - ret_age
        if ytr <= 0:
            st.error("Retirement age must be greater than current age.")
        else:
            future_monthly = monthly_exp * (1 + inflation / 100) ** ytr
            corpus = future_monthly * 12 * yir
            r_m = inv_return / 100 / 12; n_m = ytr * 12
            sip_needed = corpus * r_m / (((1 + r_m) ** n_m) - 1)
            st.markdown(f"""<div class="res-card">
                <div class="res-num">{fmt(corpus)}</div><div class="res-cap">Retirement corpus required</div>
                <div class="res-row">
                    <div class="rc"><div class="rc-v">{fmt(future_monthly)}</div><div class="rc-l">Monthly Exp. at Retirement</div></div>
                    <div class="rc"><div class="rc-v" style="color:var(--accent)">₹{sip_needed:,.0f}</div><div class="rc-l">Monthly SIP Needed</div></div>
                    <div class="rc"><div class="rc-v" style="color:var(--gold)">{ytr} yrs</div><div class="rc-l">Years to Save</div></div>
                </div></div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
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