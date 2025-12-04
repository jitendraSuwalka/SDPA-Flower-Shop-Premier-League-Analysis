# SDPA EMATM0048-Flower Shop Simulation System and Premier League Data Analysis

I created the repository which contains my full coursework submission for **SDPA EMATM0048 (Software Development and Programming for Analytics)**.
The project has two parts that have been described in this single 'README.md' file:

- **Part1-Python : Flower Shop Simulation System**
- **Part2-Jupyter Notebook : Premier Leaugue Home Advantage Data Analysis**

My objective by creating this document is to explain **What are the functions of both the parts, how the code has been written and arranged, and what are the instructions to run the code for both the parts** on any device.

---

## 1.Part 1 - Flower Shop Simulation System

### 1.1 Overview

Part 1 Here I created a **console-based information system** for a flower shop.
I wrote this program in python language using object-oriented programming and it supports:

- Managing employees i.e. florists (staff hiring, staff removal and staff list).
- Tracking the stock of flowers(i.e. roses, daisies and greenery) in a storage space(i.e.greenhouse).
- Applying depreciation and greenhouse storage costs per month to the remaining inventory after selling.
- Taking bouquet orders from customers and at the same time checking whether the currently available stock would be sufficient.
- Allocating work to prepare bouquets based on:
  - Firstly, speciality of florists and afterwards equally among all florists.
  - Secondly, there all the florists have no speciality, then work is distributed equally among them.
- Reporting updated cash balance and greenhouse quantity for each month.
- Giving options to full replenish the greenhouse inventory. Displaying pricing information for  different suppliers.
- Reporting florist revenue contribution and bouquets made for each month.

The starting point for Part 1 is **main.py**, which provides a simple text menu for running a "month in the shop". This simulation is designed to be very user friendly.

---

### 1.2 Project Structure (Part 1)

I have organized the part-1 source code in the project root, which is present there as a collection of one-off modules:

| File / Module                 | Main Contents & Responsibility  |
|---------------------------------|-------------------------------------| 
|`main.py`                      | Entry point of the application, User interaction at a high-level. Shows menu to the user, creates a `FlowerShop` object, and controls a simulated working month.|
|`flowershop.py`                | Contains the high-level FlowerShop Class that binds together: Staff, Inventory, Orders, Bouquet Allocation. Stores the Shop-Wide State (Cash Balance, Greenhouse Stock)|
|`florist.py`                   | Represents a `florist` Dataclass. Holds Information about each Florist: Name, Hourly Wage, Experience Level, Etc. Stores per florist Workload Information.|
|`staff.py`                     | Contains Functions to Display/Modify the Staff List. Includes `print_staff_list`, `hire_interactive`, and `remove_interactive`. All Console Input/Output Regarding Staff Management are Included Here.|
|`inventory.py`                 | Contains Constants and Functions to Manage Remaining Flower Stock. Contains Initial Capacity ('CAPACITY'), Depreciation of Unsold Stock, Greenhouse Storage Cost Calculation, and Helper Function `restock_to_capacity`.|
|`orders.py`                    | Contains Functions to Collect Customer Orders from the User Interactively and Check Whether the Greenhouse Has Enough Flowers to Fulfill Them (`check_supplies_for_order`).|
|`allocation.py`                | Contains the main allocation logic in the function `allocate_bouquets_among_florists`, Which Allocates Completed Bouquets Among the Current Florists Fairly and Transparently.|
|`vendor.py`                    | Contains a Simple Model of External Flower Vendor/Seller Supplier Used When Restocking to Capacity.|
|`utils.py`                     | Contains Reusable Helper Functions (e.g., `get_valid_integer` to Get Validated Integer Input, `get_yes_no_input` to Robust Yes/No Prompt, and `get_valid_name` to Get Valid Name).|
|`README.md`                     | A Documentation File, Which Describes Both Part 1 and Part 2.|

Having separated the **business logic**, **user interaction**, and **data structures** in this way makes the entire system much easier to test and expand.

---

### 1.3 Design and Key Classes 

#### `FlowerShop`

`FlowerShop` is the central Coordinating Class, Which Is Defined in 'flowershop.py'. It Manages the Following Things:

- Initializing New Shop State (Initial Cash, Empty Staff List, Greenhouse Filled to Capacity).
- Store the List of 'Florist' Instances.
- Store the Current Greenhouse Inventory as a Dictionary ({"roses": ..., "daisies": ..., "greenery": ...}).
- Own Standard Catalogue of Bouquet Recipes (Predefined Combinations of Flowers and Greenery).
- Coordinate Daily Operations: Take Orders, Check Stock, Apply Depreciation and Greenhouse Costs, Update Cash, Call the Allocation Algorithm.

Design choices:

- **Encapsulation:** All Shop-Wide State Lives Inside the 'FlowerShop' Class. All Other Modules Obtain or Modify Shop-Wide State Through Method Calls to Prevent Accidental Global Variable Coupling.
- **Data Driven Recipes:** All the Bouquet Compositions Are Stored as Dictionaries. This Makes It Easy to Add or Modify Bouquet Types Without Changing Any Algorithmic Code.

#### `Florist`

The `Florist` dataclass models individual staff member:

- Identification (name).
- Hourly wage / pay.
- Speciality attributes for florists (depending on the implementation in 'florist.py`).
- Workload counter used by allocation algorithm to keep work distribution fair for all employees.

In Having All the Staff Attributes in the Same Class, We Can Potentially Extend the System With Scheduling or Payroll Functionality Without Modifying Other Modules.

#### Allocation Algorithm

The Function `allocate_bouquets_among_florists` in `allocation.py` Distributes Completed Bouquets Among Current Florists. The Design Focuses On:

- **Fairness:** Work is distributed in such a way that priority is given to specialists first , then it is 
equally distributed among all the florists. If all florists are general (non-specialists), then all the work
is distributed equally among them.
- **Transparency:** The Logic is Expressed in Small, Well-Defined Steps; Comments Explain How Ties Are Resolved.
- **Extensibility:** If the Shop Later Wanted specialists to Receive More Complex Bouquets, This Function Would Be the Only Place That Needs to Be Updated.

---

### 1.4 Running Instructions for Part 1

#### 1.4.1 Requirements

The first part of this coursework  runs on **only Standard Python 3**, and does not need any third party libraries.

- **Python version:** 3.10 or above is recommended.
- **Operating system:** Any OS with a working Python installation (Windows, macOS, Linux).

#### 1.4.2 How to run

When running this part of the course, from the root of the project (i.e., the directory containing main.py and README.md), you would type:

```bash
python main.py
```

This will present you with a menu driven interface to perform:

1. Hiring or Confirming Florists for a Month.
2. Viewing Current Greenhouse Inventory.
3. Creating One or More Customer Bouquet Orders.
4. Reviewing if there is enough stock, and Optionally Restock.
5. Allocating Bouquets among Florists.
6. Printing a Brief End of Month Summary (Cash Balance, Leftover Stock, etc.).

If your Python Executable is named "python3" instead of "python", then you should enter:

```bash
python3 main.py
```

---

### 1.5 Extensibility and Design Choices (Part 1)

For this coursework, some design choices were made:

- **Separation of Concerns:**
  - The business logic (Allocation, Depreciation) was separated from the User Input Code. 
  - Each Module had its own focus.

- **Type Hints and Doc Strings:**
  All core Classes and Functions had Type Hints added to make them easier to read, and to support Static Checking Tools (such as `mypy`).

- **User-Friendly Error Handling:**
  The Input Helpers in `utils.py` always asked the user for valid input, so the Program never crashed because of Bad Data.

- **Testability:** 
  While not all Test Code is included in this example, all Functions were written in such a way that they could be Unit-Tested Independently of Console I/O.

All of these design choices not only allowed the System to Function as required by the Assignment, but provided a Good Template for Future Data Driven Applications.

---

## 2. Part 2- Premier League Home Advantage Data Analysis (Jupyter Notebook)

### 2.1 Overview

The second part of your coursework is focused on **exploratory data analysis and statistical modeling** using the Python programming language.

The notebook analyzes a match-by-match dataset from the **2015-16 English Premier League** season and asks the question:

> **Does playing at home give teams a scoring advantage in the 2015-16 Premier League season?**

As mentioned above all the work for Part 2 is in a single Jupyter Notebook (e.g., `SDPA_part2_premier_league_analysis.ipynb`), created by myself and in PDF format is also in the repository.

The structure of the data analysis study is the following:  
1. **Step 1 – Data loading and cleaning**
2. **Step 2 – Exploratory data analysis (EDA)**
3. **Step 3 – Reconstruction of the league table**
4. **Step 4 – Formal statistical testing and regression**
5. **Step 5 – Analysis of the performance of the champion team**

All steps are clearly described with markdown headings inside the notebook. This part of the `README.md` explains how to run the notebook and what additional libraries you need to be able to run the notebook. All the steps are clearly explained in markdown headings inside the notebook. The section of the `README.md` describes how to run the notebook and which additional libraries you may need to run the notebook.

---

### 2.2 Data

- **Data source:** Kaggle / Public Football Results Dataset for the 2015–16 Premier League (as a CSV file in the repository).

- **Key fields used:** Name of the home team, name of the away team, number of goals scored by home team, number of goals scored by away team, date of the match and full-time result of the match.

The raw CSV is loaded into a `pandas.DataFrame` in the notebook.

Basic cleaning of the data was done as follows:
- Ensuring that the columns containing numerical values (the number of goals and the number of points) were correctly typed.
- Creating new columns to store derived values (`goal_diff`, `home_points`, `away_points` and `total_goals`).
---

### 2.3 Libraries and Environment (Part 2)

We are going to use well-known scientific Python libraries:

- **Python:** 3.10+  
- **Main libraries:**
  - `pandas` – for data manipulation purpose
  - `numpy` –  for mathematical computations purpose (rolling averages, etc.)
  - `matplotlib` – for plotting purpose
  - `seaborn` – for higher‑level visualization purpose
  - `scipy` – for performing statistical tests (`scipy.stats.ttest_ind`)
  - `scikit-learn` (`sklearn`) – for simple linear regression purpose

  - `pandas` – for manipulating data
  - `numpy` – for calculations (rolling averages, etc.)
  - `matplotlib` – for plotting
  - `seaborn` – for high-level visualization
  - `scipy` – for executing statistical tests (scipy.stats.ttest_ind)
  - `sklearn` – for executing simple linear regression
To install these in a fresh environment:
To create the necessary environment to run this part of the coursework, we have to execute the following commands in a terminal session after creating a new virtual environment:

You can install them in a fresh environment with the following commands in a terminal session after creating a new virtual environment:

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```
One way to help you to run the notebook is to create a lightweight virtual environment:

```bash
python -m venv venv

source venv/bin/activate         
# On Windows: venv\Scripts\activate

pip install -r requirements.txt   
# If a file named requirements.txt is available, otherwise use the command above
```
*(`requirements.txt` is optional, the notebook will run as long as all the above-listed packages are 
installed.)*
---

### 2.4 Running the Notebook

1. Starting Jupyter (either Notebooks or Jupyter Lab) from the root of the project:
```bash
jupyter notebook
```

2. Open the notebook file of part-2 (eg. `SDPA_part2_premier_league_analysis.ipynb`).

3. Run all the cells from top to bottom, one by one (**Kernel -> Restart & Run All**).

   - Each step has a title and explanations in the form of a markdown heading.
   - Some key graphs are:
     - Histograms of home and away goals of teams.
     - Boxplot of goal difference.
     - Heatmap illustrating the correlation between home goals, away goals, total goals and goal difference.
     - Chart of bars to compare the total points rebuilt for top 5 vs bottom 5 teams.
     - Regression scatterplot with fitted line.
     - Scatterplot of regression model with fitted line.
     - Graphical representation of time series of Leicester City's goals and their 5-match rolling average.

All the text appearing in the PDF export are created directly from markdown cells of the notebook.

---

### 2.5 Project Methodology and Approach

#### Step 1 –Statistical Summary

- Compute basic descriptive statistics for home and away goals.  
- Create a `goal_diff` variable (home goals minus away goals).  
- This gives us early evidence of home teams scoring slightly more goals on average.

#### Step 1 – Statistical Summarization

- Determine basic statistical characteristics for Home Goals & Away Goals.
- Develop a `goal_diff` variable (Home Goals – Away Goals).
- This gives us preliminary evidence of Home Teams scoring an average of more goals than Away Teams.

#### Step 2 – Exploratory Data Analysis (EDA)

- Visualise the distributions of goals for home and away teams:
  - Histograms of home and away goals.
  - Boxplot of goal difference.
- Evaluate the correlation matrix between:
  - `home_goals`, `away_goals`, `total_goals`, `goal_diff`.
- Each plot will be followed by a brief interpretation written in markdown. Thus, **the results and the explanations will always appear ** together in the notebook.

Key findings:

- Home teams and away teams both usually score between 0 and 2 goals.  
- The distribution of goal differences is centered around a slight positive value, which confirms the presence of the home advantage.  
- total goals highly correlate with both home and away goals; however, both home and away goals have almost no correlation with one another, indicating two teams perform
independently.

#### Step 2 – Exploratory Data Analysis (EDA)

- Graphic representations of the distribution of Home Goals & Away Goals.
  - Histograms of Home Goals & Away Goals.
  - Boxplot of Goal Difference.
- Evaluate the Correlation Matrix between:
  - `home_goals`, `away_goals`, `total_goals`, `goal_diff`.
- Each graphic will include a short interpretation in Markdown. Therefore, **each result and explanation** will always be presented **together** in the Notebook.

Main Findings:

- Both Home Teams and Away Teams typically score 0 to 2 goals.
- Goal differences distribute symmetrically about a slightly positive value, which shows that there is a Home Advantage.
- Total goals strongly correlate with both home and away goals; however, both home and away goals demonstrate very little correlation with each other; i.e., each team performs independently of the opponent.

#### Step 3 – Reconstruction of final League Table

- Calculate the number of points each team obtains when playing at Home and Away.
- Sum and Sort to replicate the Final League Standings.
- Present the resulting league table as a formatted `pandas` Table and produce a Bar Chart displaying **Top 5 v Bottom 5** Teams.

Checks:

- Leicester City is shown as the Champions with Total Points = 81.
- Performance disparity among teams was clearly evident with nearly 4 fold point spread between Champions and Bottom Teams.

#### Step 4 – Statistical Testing & Regression Analysis

- **Primary Question (Home advantage):**

  - We perform a Two Sample T Test comparing mean Home Goals to mean Away Goals.

  - We perform Welch’s t-test (equal_var= False) to allow variances in the two samples.

  - Provide a Short Summary Table containing Results, Mean Values, t-statistic and p-values.

- **Secondary question:Relationship between home and away goals.**
- Perform Simple Linear Regression Model home_goals ~ away_goals.
- Provide a Summary Table of the regression slope and R².
- Plot the regression line across the scatter plot of match results.

Results:

- Since the p-value of the test is **well less than 0.05**, we can reject the null-hypothesis of equal means and say that **home teams score significantly more goals than away teams**.
- The regression slope is slightly negative with an extremely low R², which suggests that away goals provide **virtually zero explanatory power** for home goals; the two teams' scoring is essentially independent.

#### Step 5 – Champion Form Analysis (Leicester City)

- We need to filter the dataset such that it only includes the eventual champions (Leicester City) in the data set.
- Create a time-based plot showing goals scored in each match.
- Compute  a **5 match rolling average of goals** to represent "team form."
- Plot both the match-by-match goals and the rolling average on the same graph.

#### Step 5 – Analysis of Champion Form (Leicester City)

- Filter the dataset to show only the eventual champions (Leicester City).
- Create a Time Based Plot showing the number of goals scored in each game.
- Create a **5 game moving average of goals** to represent "Team Form".
- Plot both the individual game goals and the moving average on the same plot.

Findings:

- The individual games scored vary, but the moving average is fairly steady and does not drop-off for extended periods of time.
- This continued high-scoring attacking performance likely helped Leicester stay in the title chase throughout the season.
- In the last Insight Paragraph, I connect this view of the champion-form to the original display of the home-advantage as seen in the league-wide home advantage.


---

## 2.6 Reproducibility Notes

To completely reproduce all results for Part 2:

1. Ensure that your Premier League 2015–16 matches CSV data file is in the same directory as your notebook; If it is not, update the file path at the beginning of the notebook.
2. See Section 2.3 for details regarding the installation of required python libraries.
3. Run all Jupyter Notebooks cells sequentially in order, one at a time, without skipping any.

As stated previously, the notebook is **self-contained**: thus, all figures, tables and explanations shown in the accompanying PDF are produced automatically with the code and Markdown contained in the notebook.

---
 
 ## 3. Summary

- **Part 1** illustrates software engineering skills: modular programming, encapsulation, and some minimal interaction of user and reasoning (allocation, depreciation).

- **Part 2** illustrates data analytics skills: cleaning actual-world data, producing informative visualization, conducting formal hypothesis testing and developing predictive models.

In combination, these two parts represent a full project that transitions from developing a software system to employing analysis techniques for data-driven insight using the same Python environment.


 






 





