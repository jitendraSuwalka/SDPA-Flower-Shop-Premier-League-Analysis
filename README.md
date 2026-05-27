# Software Development & Data Analytics: Flower Shop Simulator + Premier League Analysis

Full coursework for **Software Development: Programming and Algorithms (EMATM0048)**, MSc Data Science, University of Bristol. Two-part project demonstrating software engineering and data analytics skills.

---

## Part 1 — Flower Shop Simulation System (Python OOP)

### Overview

A console-based business simulation for a flower shop, built using object-oriented programming in Python. The system supports staff management, inventory tracking with depreciation, bouquet ordering with supply validation, speciality-aware work allocation, vendor restocking, and monthly P&L reporting.

### Project Structure

| File | Responsibility |
|------|---------------|
| `main.py` | Entry point — user interaction, simulation loop |
| `flowershop.py` | Central FlowerShop class: staff, inventory, orders, cash balance |
| `florist.py` | Florist dataclass with name, speciality, workload tracking |
| `staff.py` | Interactive hiring/removal with duplicate name prevention |
| `inventory.py` | Greenhouse capacity, depreciation (ceiling-based), storage costs |
| `orders.py` | Bouquet order collection and supply validation |
| `allocation.py` | Speciality-aware round-robin bouquet allocation algorithm |
| `vendor.py` | Supplier pricing model for restocking |
| `utils.py` | Input validation helpers (integer, yes/no, name) |

### Key Design Features

- **Speciality-aware allocation:** Specialist florists handle their bouquet type at half-time, then remaining work is distributed equally via round-robin
- **Encapsulation:** All shop state managed through FlowerShop class methods
- **Data-driven recipes:** Bouquet compositions stored as dictionaries for easy extensibility
- **Robust error handling:** All user inputs validated — no crashes on invalid data
- **Type hints and docstrings:** Every class and function documented

### Running Part 1

```bash
python main.py
```
Requires only Python 3.10+ standard library — no external packages needed.

---

## Part 2 — Premier League Home Advantage Analysis (Jupyter Notebook)

### Overview

Statistical analysis of the 2015–16 English Premier League season investigating:

> **Does playing at home give teams a scoring advantage?**

### Analysis Pipeline

| Step | Description | Key Output |
|------|-------------|------------|
| **1. Data Collection** | Web scraping of match-level EPL data, cleaning, feature engineering | Clean CSV with goal_diff, home_points, away_points |
| **2. EDA** | Histograms, boxplots, correlation heatmap, top 5 teams analysis | Home teams score 0–2 goals typically, slight positive goal difference |
| **3. League Table** | Reconstructed final standings from match-level points | Leicester City confirmed as champions (81 pts) |
| **4. Statistical Testing** | Welch's t-test + Linear Regression | p < 0.05 — home advantage statistically significant |
| **5. Champion Analysis** | Leicester City's 5-match rolling average goal form | Consistent attacking form throughout the season |

### Key Results

- **Welch's t-test:** p < 0.05 — home teams score significantly more goals than away teams
- **Linear Regression:** R² near 0 — home and away goals are independent (scoring is not correlated)
- **League Table:** Successfully reconstructed with Leicester City as champions (81 points)

### Visualisations (7 plots)

- Home goals histogram + Away goals histogram
- Goal difference boxplot
- Correlation heatmap (home_goals, away_goals, total_goals, goal_diff)
- Top 5 vs Bottom 5 teams bar chart
- Regression scatter plot with fitted line
- Leicester City match-by-match goals + 5-match rolling average

### Running Part 2

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
jupyter notebook SDPA_part2_premier_league_analysis.ipynb
```

Run all cells sequentially (Kernel → Restart & Run All).

---

## Tech Stack

- **Language:** Python 3.10+
- **Part 1:** Standard library only (OOP, dataclasses, math)
- **Part 2:** Pandas, NumPy, Matplotlib, Seaborn, SciPy, Scikit-learn
- **Notebook:** Jupyter Notebook

## Author

**Jitendra Suwalka**
MSc Data Science — University of Bristol
- [LinkedIn](https://www.linkedin.com/in/jitendra-suwalka-ds)
- [GitHub](https://github.com/jitendraSuwalka)
