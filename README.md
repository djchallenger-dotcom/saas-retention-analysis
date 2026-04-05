# 📊 SaaS Retention & Funnel Optimization (Case Study)

> ⚡ **Quick Take:** Identified onboarding as the largest conversion bottleneck, demonstrated A/B improvements in activation and subscription rates, and uncovered sharp early retention drop-off within 3 days—highlighting key opportunities to improve SaaS growth.

---

## 📊 Sample Output

<p align="center">
  <img src="images/funnel_chart.png" width="700"/>
</p>
*Signup → Activation drops from **70.7% to 38.0% (−32.7pp)**, the largest funnel loss, indicating significant onboarding friction preventing users from reaching initial product value.*

<p align="center">
  <img src="images/ab_funnel.png" width="700"/>
</p>
*Treatment group increases subscription conversion from 9.3% to 15.9% (+6.6pp), with consistent gains across all funnel stages, indicating a meaningful improvement in overall user conversion.*

<p align="center">
  <img src="images/retention_curve.png" width="700"/>
</p>
*Retention peaks at approximately 5.4% around Day 18 before steadily declining to near zero by Day 80, indicating weak long-term engagement despite moderate early usage.*

---

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

## 🧩 Why I Built This
I wanted to simulate a real-world product analytics workflow end-to-end, focusing on how data scientists support product decisions in SaaS environments.

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

## 📌 Key Metrics (Example)

- Signup → Activation: **62% → 38% (−24pp drop)**  
- Activation → Subscription: **38% → 21%**  
- A/B Test Lift (Subscription): **+12%**  
- Day 3 Retention: **45% → 18%**  

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

## 💰 Business Impact

If applied in a real SaaS product, these insights could:
- Increase conversion by improving onboarding (highest ROI stage)  
- Validate product changes before full rollout (A/B testing)  
- Improve retention through early engagement strategies  

**Potential outcome:**  
> Even a 5–10% lift in activation can significantly increase revenue at scale  

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
🏗️ Project Structure

Designed with modular, production-style structure:

saas-retention-analysis/
│
├── src/
│   ├── data_generator.py
│   ├── funnel_analysis.py
│   ├── ab_testing.py
│   ├── retention_analysis.py
│   └── visualizer.py
│
├── main.py
├── requirements.txt
└── README.md
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
