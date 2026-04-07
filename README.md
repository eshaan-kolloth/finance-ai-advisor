<div align="center">

# 💹 FinAI · Finance Advisor

### *Your AI-Powered Personal Finance Guide for the Indian Market*

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq_AI-LLaMA_3.3_70B-F55036?style=for-the-badge)](https://console.groq.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

---

**A sleek, dark-themed AI finance chatbot built on Groq's LLaMA 3.3 70B — with a live market ticker, built-in financial calculators, and a conversational advisor that educates you on everything from SIPs to tax planning. Built for India. Built for clarity.**

[🚀 Quick Start](#-quick-start) · [📸 Screenshots](#-screenshots) · [🤖 Meet the Advisor](#-meet-the-advisor) · [🧮 Calculators](#-financial-calculators)

</div>

---

## ✨ What Makes This Special?

> FinAI isn't just a chatbot — it's a complete personal finance companion. Ask questions in plain English, get structured expert-level answers, and run real financial calculations — all inside a beautifully designed dark UI that feels like a professional fintech product.

---

## 🗂️ App Sections

| Section | Description |
|---------|-------------|
| 🏠 **Hero & Ticker** | Live-scrolling market ticker (NIFTY 50, SENSEX, USDINR, Gold, BTC, and more) |
| 💬 **AI Chat** | Conversational finance advisor powered by Groq's LLaMA 3.3 70B |
| 🧮 **SIP Calculator** | Compute SIP maturity value with invested amount, returns, and total gain |
| 🏠 **EMI Calculator** | Calculate monthly EMI, total interest, and total payment for any loan |
| 🎯 **Retirement Planner** | Find your retirement corpus, future monthly expenses, and required SIP |
| ℹ️ **Stats Banner** | Key platform stats — finance topics covered, Indian instruments, accuracy, and more |

---

## 📸 Screenshots

> *Coming soon — add your screenshots here!*

```
screenshots/
├── hero_ticker.png
├── ai_chat.png
├── sip_calculator.png
├── emi_calculator.png
└── retirement_planner.png
```

---

## 🤖 Meet the Advisor

The AI at the heart of FinAI is powered by **Groq's LLaMA-3.3 70B** model — one of the fastest and most capable open-weight models available. The advisor:

- 🇮🇳 **Speaks Indian finance** — uses ₹, references SIP, PPF, ELSS, NPS, FD, SEBI, RBI, Section 80C, LTCG/STCG by default
- 🎓 **Adapts to your level** — detects beginner vs. advanced users and adjusts tone and depth accordingly
- 📐 **Always structured** — every response follows a clean Markdown format with sections, bullet points, examples, and a quick summary
- 🔢 **Uses your numbers** — if you mention ₹50,000 salary or ₹10 lakh savings, those exact figures appear in the answer
- 💬 **Keeps the conversation going** — every reply ends with suggested follow-up questions
- 🔒 **Stays in its lane** — only answers finance-related questions; redirects off-topic queries gracefully
- ⚠️ **Never gives stock tips** — explains factors to consider rather than recommending specific assets

**Example questions to ask:**
```
"How does SIP work and how much should I invest monthly?"
"What is ELSS and how does it help save tax under Section 80C?"
"Explain LTCG vs STCG on equity mutual funds."
"I earn ₹60,000/month — how should I budget and save?"
"What's the difference between PPF and NPS for retirement?"
"How does RBI interest rate policy affect my FD returns?"
```

---

## 🧮 Financial Calculators

Three built-in calculators with real financial formulas — no approximations.

### 📈 SIP Calculator
Enter your monthly investment, expected annual return, and time period to see:
- **Total Maturity Value**
- **Amount Invested**
- **Estimated Returns**
- **Total Gain %**

### 🏠 EMI Calculator
Enter loan amount, interest rate, and tenure to see:
- **Monthly EMI**
- **Principal Amount**
- **Total Interest Paid**
- **Total Payment**

### 🎯 Retirement Planner
Enter current age, retirement age, monthly expenses, inflation, return rate, and life expectancy to see:
- **Retirement Corpus Required**
- **Monthly Expenses at Retirement** (inflation-adjusted)
- **Monthly SIP Needed to reach the corpus**
- **Years left to save**

---

## 📊 Key Features

- **Live Market Ticker** — scrolling strip with NIFTY 50, SENSEX, USDINR, Gold, Silver, Crude Oil, BTC, ETH
- **Dark Premium UI** — custom CSS with `Playfair Display`, `IBM Plex Mono`, and `Outfit` fonts; teal accent, deep navy surfaces
- **Full Chat Memory** — conversation history maintained across the session
- **Structured AI Responses** — every answer has Explanation → Key Points → Example → Tips → Summary → Follow-up Questions
- **Indian Financial Context** — SIP, ELSS, PPF, NPS, FD, RBI, SEBI, Section 80C referenced throughout
- **Educational Disclaimer** — clearly marked as educational only, not SEBI-registered advice

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/finai-advisor.git
cd finai-advisor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=gsk_your_key_here
```

> Get your **free** API key at [console.groq.com](https://console.groq.com)

### 4. Launch the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser. 🎉

---

## 🗃️ Project Structure

```
finai-advisor/
│
├── app.py              # Main Streamlit app — UI, chat interface, calculators
├── chatbot1.py         # Groq API integration, system prompt, chat memory
├── requirements.txt    # Python dependencies
├── .env                # Your API key (not committed to git)
└── .gitignore
```

---

## 📦 Dependencies

```txt
streamlit       # Web app framework
groq>=0.9.0     # Groq API client for LLaMA 3.3 70B
python-dotenv   # Load API keys from .env
```

---

## 🔐 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | ✅ Yes | Enables the AI finance advisor chat |

> Without the key, the calculator sections will still work, but the AI chatbot will not respond.

---

## 💡 Topics the Advisor Covers

- Personal finance & budgeting
- Saving strategies & emergency funds
- Mutual funds, stocks, bonds, ETFs
- Indian instruments — SIP, ELSS, PPF, NPS, FD, RD, NSC, Sovereign Gold Bonds
- Stock market concepts — technical & fundamental analysis
- Risk management & portfolio diversification
- Financial goal setting & planning
- Economic concepts — inflation, GDP, interest rates, RBI monetary policy
- Debt, EMI & credit score management
- Retirement planning
- Tax planning — Section 80C, LTCG, STCG, HRA, and more
- Cryptocurrency basics (educational only)

---

## 🛣️ Roadmap

- [ ] User authentication & saved chat history
- [ ] Downloadable PDF summaries of AI responses
- [ ] Real-time market data integration (NSE/BSE API)
- [ ] Portfolio tracker — input your holdings, get AI analysis
- [ ] Multi-language support (Hindi, Malayalam, Tamil)
- [ ] Goal-based savings planner
- [ ] Dark/light theme toggle

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## ⚠️ Disclaimer

FinAI is built **for educational purposes only**. It is **not** SEBI-registered financial advice. All information provided by the AI advisor is general in nature. Always consult a qualified financial advisor before making investment decisions.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

**Built with ❤️ for smarter financial decisions in India**

*If this project helped you, consider giving it a ⭐ on GitHub!*

</div>
