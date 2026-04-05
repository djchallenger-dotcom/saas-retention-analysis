# 📊 SaaS Retention & Funnel Optimization

> > ⚡ **Quick Take:** Identified a **32.7pp onboarding drop-off**, improved conversion by **+6.6pp via A/B testing**, and found **near-zero retention by Day 80**.

---

## 📊 Key Results

| Metric | Result |
|------|--------|
| Funnel Drop-Off | **−32.7pp (Signup → Activation)** |
| A/B Test Lift | **+6.6pp (Subscription Conversion)** |
| Retention Risk | **~0% by Day 80** |

---

## 📈 Product Insights

The following analyses highlight key conversion and retention challenges across the user lifecycle.

### Funnel Analysis
<p align="center">
  <img src="images/funnel_chart.png" width="700"/>
</p>

Signup → Activation drops from **70.7% to 38.0% (−32.7pp)**, the largest funnel loss. This indicates onboarding friction preventing users from reaching initial product value.

---

### A/B Test Results
<p align="center">
  <img src="images/ab_funnel.png" width="700"/>
</p>

Treatment increases subscription conversion from **9.3% to 15.9% (+6.6pp)**. Gains are consistent across all funnel stages, indicating a meaningful improvement in user conversion.

---

### Retention Curve
<p align="center">
  <img src="images/retention_curve.png" width="700"/>
</p>

Retention peaks at **5.4% around Day 18** before steadily declining to near zero by Day 80. This indicates weak long-term engagement despite moderate early usage.

---

## 🧠 Problem

SaaS companies often struggle with:
- Low conversion through onboarding funnels  
- Poor early-stage retention  
- Unclear impact of product changes  

**Key question:**  
> Where are users dropping off, and how can conversion and retention be improved?

---

## 🎯 Objective

Simulate a SaaS product environment and perform end-to-end analysis to:
- Identify funnel bottlenecks  
- Evaluate an A/B test  
- Measure user retention  
- Generate actionable product insights  

---

## ⚙️ Approach

Designed to mirror real-world product analytics workflows used in SaaS companies.

### Data Simulation
- Generated synthetic event-level data for ~2,000 users  
- Simulated events: `visit`, `signup`, `activate`, `subscribe`, `session`  
- Included:
  - acquisition channel  
  - device type  
  - country  
  - experiment group  

---

### Funnel Analysis
- Tracked user progression through onboarding stages  
- Identified highest drop-off points  

---

### A/B Testing
- Compared control (A) vs treatment (B)  
- Measured conversion lift across funnel  

---

### Retention Analysis
- Measured user activity over time  
- Identified early and long-term engagement patterns  

---

## 💰 Business Impact

If applied to a real SaaS product:

- Improving activation could significantly increase revenue  
- A/B testing enables confident product decisions  
- Early retention improvements drive long-term growth  

> Even small improvements (5–10%) in activation can scale into major revenue gains.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/djchallenger-dotcom/saas-retention-analysis.git
cd saas-retention-analysis
```
### 2. Create a virtual environment (recommended)
```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the project
```bash
python main.py
```
### 🏗️ Project Structure
```bash
saas-retention-analysis/
│
├── src/
│   ├── data_generator.py
│   ├── funnel_analysis.py
│   ├── ab_testing.py
│   ├── retention_analysis.py
│   └── visualizer.py
├── images/
├── main.py
├── requirements.txt
└── README.md
```
### 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib

### 💡 Future Improvements
- Statistical significance testing
- Cohort-based retention analysis
- Segmentation (device, channel, geography)
- Integration with real-world datasets
- Add automated tests (pytest)

### 👤 Author

**Daniel Challenger**
