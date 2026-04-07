<div align="center">

<br>

```
███████╗██╗███╗   ██╗ █████╗ ██╗
██╔════╝██║████╗  ██║██╔══██╗██║
█████╗  ██║██╔██╗ ██║███████║██║
██╔══╝  ██║██║╚██╗██║██╔══██║██║
██║     ██║██║ ╚████║██║  ██║██║
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝
```

### *"Stop guessing. Start knowing."*

<br>

![Python](https://img.shields.io/badge/Python-3.9+-FFD43B?style=flat-square&logo=python&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Powered_by-Groq_LLaMA_3.3_70B-8B5CF6?style=flat-square)
![India](https://img.shields.io/badge/Built_for-🇮🇳_India-FF9933?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-10B981?style=flat-square)
![Status](https://img.shields.io/badge/Status-Live-00D4AA?style=flat-square)

<br>

> A dark-themed AI finance advisor that speaks plain language, thinks in Indian Rupees,  
> and explains everything from SIPs to Section 80C — in seconds.

<br>

**[🚀 Get Started](#-get-started-in-3-minutes) &nbsp;·&nbsp; [💬 See It In Action](#-what-finai-actually-says) &nbsp;·&nbsp; [🧮 Calculators](#-built-in-calculators) &nbsp;·&nbsp; [🗺️ Roadmap](#️-roadmap)**

<br>

---

</div>

## 🧭 What Is FinAI?

Most finance tools are either too complex or too shallow. FinAI sits in the sweet spot — it's an AI chatbot that:

- Answers your personal finance questions **in structured, readable Markdown**
- Adapts its explanation depth to **your knowledge level** (beginner or advanced)
- Uses **your exact numbers** in examples, not generic placeholders
- Stays laser-focused on **Indian financial instruments and context**
- Comes with **3 built-in calculators** so you can validate what it tells you

Built with Streamlit + Groq's blazing-fast inference. No logins. No paywalls. No jargon walls.

<br>

---

## ⚡ Get Started in 3 Minutes

```bash
# 1. Clone
git clone https://github.com/your-username/finai-advisor.git
cd finai-advisor

# 2. Install
pip install -r requirements.txt

# 3. Add your Groq key
echo "GROQ_API_KEY=gsk_your_key_here" > .env

# 4. Launch
streamlit run app.py
```

> 🔑 Get a **free** Groq API key at [console.groq.com](https://console.groq.com) — no credit card needed.

Open **http://localhost:8501** and start asking. ✅

<br>

---

## 💬 What FinAI Actually Says

Unlike generic AI, FinAI structures every single response the same clean way. Here's what you get when you ask *"How does SIP work?"*:

```
💡  What Is a SIP?

    Great question! Let me break down how SIPs work in simple terms.

📖  Explanation
    A Systematic Investment Plan (SIP) lets you invest a fixed
    amount in a mutual fund every month automatically...

📌  Key Points
    • Rupee cost averaging  —  buy more units when markets dip
    • Power of compounding  —  your returns earn returns
    • Flexibility           —  start with as little as ₹500/month

🧮  Example  (using ₹5,000/month at 12% for 10 years)
    Invested:  ₹6,00,000
    Returns:   ₹5,61,695
    Total:     ₹11,61,695

🛠️  Practical Tips
    • Set up an auto-debit on salary day
    • Don't stop SIPs during market dips — that's when it helps most
    • Review your fund's performance annually, not monthly

⚡  Quick Summary
    SIPs make investing automatic, affordable, and surprisingly powerful
    over the long term thanks to compounding.

💬  You might also want to ask:
    → What is ELSS and can I save tax with SIP?
    → What's a good SIP amount for a ₹50,000 salary?
```

**Every. Single. Response.** No exceptions. No walls of text.

<br>

---

## 🧮 Built-In Calculators

No need to open a separate tab. Three financial calculators live inside the app:

<br>

### 📈 SIP Calculator
> *"If I invest ₹5,000/month at 12% for 10 years, what do I get?"*

| Input | Output |
|-------|--------|
| Monthly investment | Maturity value |
| Expected return % p.a. | Amount invested |
| Time period (years) | Estimated returns |
| | Total gain % |

<br>

### 🏠 EMI Calculator
> *"What will my monthly payment be on a ₹40 lakh home loan at 8.5% for 20 years?"*

| Input | Output |
|-------|--------|
| Loan amount | Monthly EMI |
| Interest rate % p.a. | Total interest paid |
| Tenure (years) | Total amount paid |

<br>

### 🎯 Retirement Planner
> *"I'm 27, want to retire at 60, spend ₹40,000/month now — what corpus do I need?"*

| Input | Output |
|-------|--------|
| Current age + retirement age | Corpus required |
| Monthly expenses today | Future monthly expense (inflation-adjusted) |
| Inflation % + investment return % | Monthly SIP to start now |
| Life expectancy | Years left to build the corpus |

All three use **real financial formulas** — SIP future value, standard EMI formula, and inflation-adjusted corpus calculation. Not rough estimates.

<br>

---

## 🧠 The AI Behind It

FinAI's advisor is powered by **Groq's LLaMA 3.3 70B** — one of the fastest LLMs available — with a deeply customized system prompt that makes it behave like a knowledgeable Indian finance guide.

### What it knows

```
Personal Finance     → Budgeting, 50-30-20 rule, emergency funds
Investing            → Stocks, bonds, mutual funds, ETFs, SGBs
Indian Instruments   → SIP · ELSS · PPF · NPS · FD · RD · NSC
Markets              → Fundamentals, technicals, SEBI regulations
Tax Planning         → Sec 80C · LTCG · STCG · HRA · NPS deduction
Debt Management      → EMI structuring, credit scores, prepayment
Retirement           → Corpus planning, SWP strategies
Crypto               → Educational overview only
Economics            → RBI policy, inflation, GDP, repo rate impact
```

### What it will never do

```
✗  Recommend specific stocks or funds by name
✗  Guarantee returns or profits
✗  Answer non-finance questions (redirects gracefully)
✗  Provide SEBI-registered investment advice
```

### How it adapts

| User Signal | FinAI Behavior |
|-------------|----------------|
| Simple, casual language | Uses analogies, avoids jargon, explains every term |
| Technical terms used confidently | Full depth, technical terminology, no hand-holding |
| Mentions specific numbers (e.g. "₹60,000 salary") | Uses those exact figures in every example and calculation |

<br>

---

## 🖥️ UI at a Glance

The app is designed to feel like a real fintech product, not a demo:

```
┌─────────────────────────────────────────────────────────┐
│  💹 FinAI                                    ● LIVE      │  ← sticky nav
├─────────────────────────────────────────────────────────┤
│                                                         │
│         Your AI Finance Advisor                         │  ← hero section
│         for the Indian market.                          │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  NIFTY ▲0.6%  SENSEX ▲0.4%  USDINR 83.42  GOLD ▲0.2%  │  ← live ticker
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [Chat interface]                                       │  ← AI advisor
│  Ask about SIP, taxes, mutual funds, EMI...    Send →   │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  [ 📈 SIP ] [ 🏠 EMI ] [ 🎯 Retirement ]               │  ← calculators
└─────────────────────────────────────────────────────────┘
```

- **Dark navy base** — `#080c12` background, surfaces in `#111820`
- **Teal accent** — `#00d4aa` for highlights and interactive elements
- **Gold secondary** — `#f0b429` for gains and important numbers
- **Three fonts** — *Playfair Display* for headings, `IBM Plex Mono` for data labels, Outfit for body text
- **No sidebar** — clean single-column layout, fully distraction-free

<br>

---

## 📁 Project Structure

```
finai-advisor/
│
├── app.py              ← Streamlit UI: nav, hero, ticker, chat, calculators, footer
├── chatbot1.py         ← Groq client, system prompt, chat history, chat() function
├── requirements.txt    ← Dependencies
├── .env                ← Your Groq API key (never commit this)
└── .gitignore
```

Two files do all the heavy lifting.

<br>

---

## 📦 Requirements

```txt
streamlit        # App framework
groq>=0.9.0      # LLaMA 3.3 70B via Groq
python-dotenv    # Load .env secrets
```

Three dependencies. That's it.

<br>

---

## 🔐 Environment Setup

| Variable | Where to get it | Required? |
|----------|-----------------|-----------|
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) | ✅ Yes — for AI chat |

The calculators work without any API key. Only the AI chat requires it.

<br>

---

## 🗺️ Roadmap

```
Now ──────────────────────────────────────────────────────────▶ Future

✅ AI chat with structured responses
✅ SIP / EMI / Retirement calculators
✅ Live scrolling market ticker
✅ Beginner ↔ Advanced mode detection
✅ Indian finance context (₹, SIP, ELSS, RBI, etc.)

⬜ Real-time NSE / BSE price integration
⬜ Portfolio tracker — input holdings, get AI analysis
⬜ PDF export of AI responses
⬜ Persistent chat history across sessions
⬜ Hindi language support
⬜ Goal-based savings planner (home, car, education, travel)
⬜ Dark ↔ light theme toggle
⬜ Telegram / WhatsApp bot version
```

<br>

---

## 🤝 Contributing

Found a bug? Have an idea? PRs are very welcome.

```bash
git checkout -b feat/your-idea
# make your changes
git commit -m "feat: short description"
git push origin feat/your-idea
# open a pull request
```

One feature per PR keeps reviews fast and clean.

<br>

---

## ⚠️ Disclaimer

> FinAI is built for **educational purposes only** and is **not registered with SEBI**.  
> It does not provide personalized investment advice.  
> All AI responses are general in nature.  
> **Always consult a qualified financial advisor before making real investment decisions.**

<br>

---

## 📄 License

MIT — free to use, modify, and distribute. See [`LICENSE`](LICENSE) for details.

<br>

---

<div align="center">

<br>

*Made for people who want to understand their money — not just move it around.*

<br>

**Found it useful? Drop a ⭐ on GitHub.**

<br>

</div>
