# 📊 SaaS Retention & Funnel Optimization (Case Study)

## 🧠 Problem
SaaS companies often struggle with:
- Low conversion through onboarding funnels  
- Poor early-stage retention  
- Unclear impact of product changes  

**Key question:**  
> Where are users dropping off, and what changes will most improve conversion and retention?

---

## 🎯 Objective
Simulate a SaaS product environment and perform end-to-end analysis to:
- Identify funnel bottlenecks  
- Evaluate an A/B test  
- Measure user retention  
- Generate actionable product insights  

---

## ⚙️ Approach

### 1. Data Simulation
- Generated synthetic event-level data for ~2,000 users  
- Simulated key events:
  - `visit`, `signup`, `activate`, `subscribe`, `session`  
- Included realistic features:
  - acquisition channel  
  - device type  
  - country  
  - experiment group (A/B)  

---

### 2. Funnel Analysis
Tracked user progression:

**Visit → Signup → Activation → Subscription**

**Goal:**
- Identify the highest drop-off stage  
- Quantify conversion rates between steps  

---

### 3. A/B Testing
Compared:
- **Group A (control)**
- **Group B (treatment)**

Measured:
- Conversion rates at each funnel stage  
- Relative performance lift  

⚠️ **Note:**  
The treatment effect is intentionally embedded in the synthetic data to demonstrate the A/B testing workflow.

---

### 4. Retention Analysis
Measured user engagement over time:
- Tracked activity after first interaction  
- Calculated day-level retention  

**Goal:**
- Understand when users disengage  
- Identify early retention risks  

---

## 📈 Key Findings

### 🚧 Funnel Bottleneck
- Largest drop-off occurs between **Signup → Activation**  
- Indicates friction in onboarding or initial product experience  

👉 **Recommendation:** Improve onboarding UX or reduce activation steps  

---

### 🧪 A/B Test Impact
- Treatment group outperforms control across funnel stages  
- Highest lift observed in **activation and subscription rates**  

👉 **Recommendation:** Roll out treatment changes *(pending statistical validation)*  

---

### 📉 Retention Drop-Off
- Significant user drop-off within the first few days  
- Retention curve declines rapidly after Day 3  

👉 **Recommendation:**  
- Improve early user engagement  
- Introduce onboarding emails or in-app prompts  

---

## 📊 Example Outputs
- Funnel conversion charts  
- A/B comparison plots  
- Retention curves  

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/djchallenger-dotcom/saas-retention-analysis.git
cd saas-retention-analysis
2. Create a virtual environment (recommended)
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run the project
python main.py
🛠️ Tech Stack
Python
Pandas
NumPy
Matplotlib / Seaborn
💡 What I Would Do Next (Production Scenario)

If this were real company data, next steps would include:

Statistical significance testing (e.g., two-proportion z-test)
Cohort-based retention analysis (Day 1, Day 7, Day 14)
Segmentation:
Device (mobile vs desktop)
Acquisition channel (paid vs organic)
Geography
Experiment iteration based on user behavior insights
🎯 Why This Project Stands Out

This project demonstrates:

End-to-end product analytics workflow
Strong business intuition (not just code)
Ability to translate data into actionable recommendations
Understanding of experimentation and user behavior
👤 Author

Daniel Challenger
