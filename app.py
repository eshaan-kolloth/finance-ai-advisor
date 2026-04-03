import streamlit as st
from chatbot1 import chat

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Finance Advisor",
    page_icon="💹",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Import fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

    /* ── Root palette ── */
    :root {
        --bg:          #0b0f1a;
        --surface:     #111827;
        --surface2:    #1a2236;
        --border:      #1f2d45;
        --accent:      #00e5a0;
        --accent2:     #00b4ff;
        --text:        #e8edf5;
        --muted:       #8896ab;
        --danger:      #ff5f7e;
        --gold:        #f5c542;
    }

    /* ── Global reset ── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        background-color: var(--bg) !important;
        color: var(--text) !important;
    }

    /* Remove Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container {
        padding: 2.5rem 1.5rem 4rem;
        max-width: 780px;
    }

    /* ── Animated grid background ── */
    body::before {
        content: '';
        position: fixed;
        inset: 0;
        background-image:
            linear-gradient(rgba(0,229,160,.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,229,160,.04) 1px, transparent 1px);
        background-size: 48px 48px;
        pointer-events: none;
        z-index: 0;
    }

    /* ── Hero header ── */
    .hero {
        text-align: center;
        padding: 3.5rem 0 2.5rem;
        position: relative;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: .45rem;
        background: linear-gradient(135deg,rgba(0,229,160,.12),rgba(0,180,255,.12));
        border: 1px solid rgba(0,229,160,.25);
        border-radius: 999px;
        padding: .3rem .9rem;
        font-size: .72rem;
        font-weight: 600;
        letter-spacing: .12em;
        text-transform: uppercase;
        color: var(--accent);
        margin-bottom: 1.4rem;
    }
    .hero-title {
        font-family: 'Syne', sans-serif;
        font-size: clamp(2.4rem, 6vw, 3.8rem);
        font-weight: 800;
        line-height: 1.05;
        background: linear-gradient(135deg, #e8edf5 30%, var(--accent) 75%, var(--accent2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: .8rem;
    }
    .hero-sub {
        color: var(--muted);
        font-size: 1.05rem;
        font-weight: 300;
        max-width: 420px;
        margin: 0 auto 2rem;
        line-height: 1.65;
    }

    /* ── Ticker tape ── */
    .ticker-wrap {
        overflow: hidden;
        border-top: 1px solid var(--border);
        border-bottom: 1px solid var(--border);
        padding: .55rem 0;
        margin-bottom: 2.8rem;
        background: var(--surface);
    }
    .ticker {
        display: flex;
        gap: 2.5rem;
        white-space: nowrap;
        animation: ticker 22s linear infinite;
    }
    .ticker-item {
        display: inline-flex;
        align-items: center;
        gap: .4rem;
        font-size: .78rem;
        font-weight: 500;
        color: var(--muted);
        letter-spacing: .04em;
    }
    .ticker-item .sym  { color: var(--text); font-weight: 600; }
    .ticker-item .up   { color: var(--accent); }
    .ticker-item .down { color: var(--danger); }
    @keyframes ticker {
        from { transform: translateX(0); }
        to   { transform: translateX(-50%); }
    }

    /* ── Feature chips ── */
    .chips {
        display: flex;
        flex-wrap: wrap;
        gap: .65rem;
        justify-content: center;
        margin-bottom: 2.5rem;
    }
    .chip {
        background: var(--surface2);
        border: 1px solid var(--border);
        border-radius: 999px;
        padding: .38rem .95rem;
        font-size: .78rem;
        color: var(--muted);
        display: flex;
        align-items: center;
        gap: .35rem;
    }
    .chip span { color: var(--accent); font-size: .95rem; }

    /* ── Card ── */
    .card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 2rem 2.2rem;
        margin-bottom: 1.6rem;
        position: relative;
        overflow: hidden;
    }
    .card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
    }
    .card-label {
        font-family: 'Syne', sans-serif;
        font-size: .72rem;
        font-weight: 700;
        letter-spacing: .14em;
        text-transform: uppercase;
        color: var(--accent);
        margin-bottom: .7rem;
    }

    /* ── Stremlit input override ── */
    div[data-testid="stTextInput"] > div > div > input {
        background: var(--surface2) !important;
        border: 1.5px solid var(--border) !important;
        border-radius: 12px !important;
        color: var(--text) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 1rem !important;
        padding: .85rem 1.1rem !important;
        transition: border-color .2s !important;
    }
    div[data-testid="stTextInput"] > div > div > input:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px rgba(0,229,160,.15) !important;
        outline: none !important;
    }

    /* ── Button override ── */
    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, var(--accent), var(--accent2)) !important;
        color: #07101e !important;
        border: none !important;
        border-radius: 12px !important;
        font-family: 'Syne', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        letter-spacing: .04em !important;
        padding: .75rem 2.2rem !important;
        cursor: pointer !important;
        transition: opacity .2s, transform .15s !important;
        width: 100% !important;
    }
    div[data-testid="stButton"] > button:hover {
        opacity: .88 !important;
        transform: translateY(-1px) !important;
    }
    div[data-testid="stButton"] > button:active {
        transform: translateY(0) !important;
    }

    /* ── Spinner override ── */
    .thinking-box {
        display: flex;
        align-items: center;
        gap: .75rem;
        background: rgba(0,229,160,.07);
        border: 1px solid rgba(0,229,160,.2);
        border-radius: 12px;
        padding: .9rem 1.2rem;
        margin: 1.2rem 0;
        font-size: .9rem;
        color: var(--accent);
        animation: pulse 1.6s ease-in-out infinite;
    }
    @keyframes pulse {
        0%,100% { opacity: 1; }
        50%      { opacity: .55; }
    }
    .dot-loader {
        display: flex;
        gap: 4px;
    }
    .dot-loader div {
        width: 6px; height: 6px;
        border-radius: 50%;
        background: var(--accent);
        animation: bounce 1s ease-in-out infinite;
    }
    .dot-loader div:nth-child(2) { animation-delay: .16s; }
    .dot-loader div:nth-child(3) { animation-delay: .32s; }
    @keyframes bounce {
        0%,80%,100% { transform: scale(0.7); opacity:.5; }
        40%          { transform: scale(1.2); opacity:1; }
    }

    /* ── Answer box ── */
    .answer-card {
        background: var(--surface2);
        border: 1px solid var(--border);
        border-left: 3px solid var(--accent);
        border-radius: 14px;
        padding: 1.4rem 1.6rem;
        margin-top: 1rem;
        line-height: 1.75;
        font-size: .97rem;
        color: var(--text);
        animation: fadeUp .4s ease;
    }
    .answer-head {
        display: flex;
        align-items: center;
        gap: .5rem;
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: .82rem;
        letter-spacing: .1em;
        text-transform: uppercase;
        color: var(--accent);
        margin-bottom: .9rem;
        padding-bottom: .7rem;
        border-bottom: 1px solid var(--border);
    }
    @keyframes fadeUp {
        from { opacity:0; transform: translateY(10px); }
        to   { opacity:1; transform: translateY(0); }
    }

    /* ── Error box ── */
    .error-box {
        background: rgba(255,95,126,.08);
        border: 1px solid rgba(255,95,126,.3);
        border-radius: 12px;
        padding: .85rem 1.1rem;
        color: var(--danger);
        font-size: .9rem;
        margin-top: .5rem;
    }

    /* ── Sample questions ── */
    .sample-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: .7rem;
        margin-top: 1rem;
    }
    .sample-q {
        background: var(--surface2);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: .65rem .9rem;
        font-size: .8rem;
        color: var(--muted);
        cursor: pointer;
        transition: all .2s;
        position: relative;
        padding-left: 1.5rem;
    }
    .sample-q::before {
        content: '→';
        position: absolute;
        left: .6rem;
        color: var(--accent);
        font-size: .8rem;
    }
    .sample-q:hover {
        border-color: var(--accent);
        color: var(--text);
    }

    /* ── Stats row ── */
    .stats-row {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    .stat-box {
        flex: 1;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 1.1rem 1rem;
        text-align: center;
    }
    .stat-num {
        font-family: 'Syne', sans-serif;
        font-size: 1.6rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--accent), var(--accent2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .stat-lbl {
        font-size: .73rem;
        color: var(--muted);
        margin-top: .2rem;
        letter-spacing: .05em;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        color: var(--muted);
        font-size: .75rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid var(--border);
    }
    .footer a { color: var(--accent); text-decoration: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Ticker tape ──────────────────────────────────────────────────────────────
TICKERS = [
    ("AAPL", "182.63", "+1.24%", True),
    ("TSLA", "243.10", "-0.87%", False),
    ("BTC",  "62,410", "+3.15%", True),
    ("ETH",  "3,245",  "+2.08%", True),
    ("SPY",  "521.30", "+0.43%", True),
    ("NVDA", "875.20", "+5.62%", True),
    ("GOLD", "2,318",  "-0.21%", False),
    ("EUR/USD","1.0832","+0.10%",True),
]
ticker_html = '<div class="ticker-wrap"><div class="ticker">'
for sym, price, chg, up in TICKERS * 2:
    cls = "up" if up else "down"
    arrow = "▲" if up else "▼"
    ticker_html += (
        f'<div class="ticker-item">'
        f'<span class="sym">{sym}</span>'
        f'<span>{price}</span>'
        f'<span class="{cls}">{arrow} {chg}</span>'
        f'</div>'
    )
ticker_html += "</div></div>"

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">✦ AI-Powered &nbsp;·&nbsp; Real Insights</div>
        <div class="hero-title">Your Personal<br>Finance Advisor</div>
        <p class="hero-sub">Ask anything — markets, budgeting, investments, taxes.<br>Get expert-level answers instantly.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(ticker_html, unsafe_allow_html=True)

# ── Feature chips ────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="chips">
        <div class="chip"><span>📈</span> Stock Analysis</div>
        <div class="chip"><span>🏦</span> Banking & Savings</div>
        <div class="chip"><span>₿</span> Crypto Markets</div>
        <div class="chip"><span>📊</span> Portfolio Strategy</div>
        <div class="chip"><span>🧾</span> Tax Planning</div>
        <div class="chip"><span>🎯</span> Retirement Goals</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Stats row ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="stats-row">
        <div class="stat-box"><div class="stat-num">50K+</div><div class="stat-lbl">Questions Answered</div></div>
        <div class="stat-box"><div class="stat-num">98%</div><div class="stat-lbl">Accuracy Rate</div></div>
        <div class="stat-box"><div class="stat-num">24/7</div><div class="stat-lbl">Always Available</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Main question card ────────────────────────────────────────────────────────
st.markdown('<div class="card"><div class="card-label">💬 Ask Your Question</div>', unsafe_allow_html=True)

user_question = st.text_input(
    label="",
    placeholder="e.g. How should I diversify my portfolio in 2024?",
    key="question",
)

st.markdown("</div>", unsafe_allow_html=True)

# ── Sample questions ─────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="card">
        <div class="card-label">⚡ Suggested Questions</div>
        <div class="sample-grid">
            <div class="sample-q">What's the best way to start investing with $1,000?</div>
            <div class="sample-q">How do index funds differ from ETFs?</div>
            <div class="sample-q">Should I pay off debt or invest first?</div>
            <div class="sample-q">What is dollar-cost averaging?</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Ask button + response ─────────────────────────────────────────────────────
ask = st.button("Get AI Advice →")

if ask:
    if not user_question.strip():
        st.markdown(
            '<div class="error-box">⚠️ Please enter a question before hitting "Get AI Advice".</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="thinking-box">
                <div class="dot-loader"><div></div><div></div><div></div></div>
                Analysing your question and crafting the best answer…
            </div>
            """,
            unsafe_allow_html=True,
        )

        answer = chat(user_question)

        st.markdown(
            f"""
            <div class="answer-card">
                <div class="answer-head">
                    <span>💹</span> AI Finance Advisor
                </div>
                {answer}
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="footer">
        ⚠️ This tool is for <strong>informational purposes only</strong> and does not constitute financial advice.<br>
        Always consult a qualified financial advisor before making investment decisions.<br><br>
        Built with ❤️ using <a href="https://streamlit.io" target="_blank">Streamlit</a> &amp; Claude AI
    </div>
    """,
    unsafe_allow_html=True,
)