# Repository Description: Data Analytics for Executives (CO62 - CD62)

## Overview
This repository contains the materials, code, and datasets for the "Data Analytics for Executives" (CO62 - CD62) course, taught by Kostis Christodoulou in Spring 2026. The codebase is primarily composed of Jupyter Notebooks that guide students through various data manipulation, statistical analysis, simulation, and machine learning/regression concepts using Python.

## Main Themes and Contents of Each Session

### Session 1
**Main Theme:** Probability, Simulation, Web Scraping, and Bootstrapping.
**Contents:** This folder introduces foundational quantitative concepts through hands-on simulations (e.g., dice and binomial distributions). It progresses to practical data acquisition methods like web scraping UK polls, and introduces statistical techniques like bootstrapping and calculating confidence intervals.
**Key Files:** 
- `01_dice_simulation.ipynb`, `02_binomial_simulation.ipynb`, `04_admissions_normal_distribution.ipynb` (Probability & Distributions)
- `90_uk_polls_scraping.ipynb` (Web Scraping)
- `05_bootstrap_analysis.ipynb`, `04_binomial_CI.py`, `07_bootstrap_function.py` (Bootstrapping & Confidence Intervals)

### Session 2
**Main Theme:** Exploratory Data Analysis (EDA) and A/B Testing.
**Contents:** This section shifts focus towards analyzing real-world datasets and evaluating causal impact through experiments. It walks through cleaning and visualizing survey data, evaluating global warming trends, analyzing stock returns, and understanding the results of an Uber A/B test.
**Key Files:**
- `01_global_warming.ipynb` (Trend Analysis) 
- `02_uber_ab_test.ipynb` (A/B Testing)
- `05_stock_returns.ipynb` (Financial Data Analysis)
- `04_student_survey_analysis.ipynb` (Survey Data EDA)

### Session 3
**Main Theme:** Geo-spatial Visualization, Financial Modeling (CAPM), and Introduction to Linear Models & Regression.
**Contents:** This session bridges the gap between advanced plotting, financial theory, and introduces linear models and regression analysis. Half of the content deals with mapping spatial data (e.g., Uber/Lyft pickup locations in NYC) and analyzing surge pricing. The other half focuses on the Capital Asset Pricing Model (CAPM) and regression utilizing real asset data (Apple and the S&P 500).
**Key Files:**
- `00_nyc_uber_lyft_maps.ipynb`, `01_uber_surge_analysis.ipynb` (Geo-spatial Visualization)
- `03_aapl_capm.ipynb`, `04_sp500_CAPM.ipynb` (Financial Modeling)
- `02_world_happiness.ipynb` (EDA & Visualization)

### Session 4
**Main Theme:** Linear Modeling and Regression Analysis.
**Contents:** The final session is heavily geared towards statistical modeling, specifically linear regression. It uses various socio-economic and health datasets to teach students how to build, interpret, and evaluate linear models to uncover relationships between variables.
**Key Files:**
- `01_smoking_birth_weight.ipynb` (Health Data Regression)
- `02_height_earnings.ipynb` (Socio-economic Regression)
- `03_credit_linear_models.ipynb` (Financial/Credit Modeling)

### Other Notable Folders
- **`group_project`**: Contains the `london_bikes.ipynb` notebook and relies on the associated `london_bikes.csv` dataset from the `data` folder, presumably for a comprehensive final group assignment.
- **`data`**: A centralized directory hosting all CSV files used across the seminars, such as `credit.csv`, `gss_extract_2022.csv`, `uber.csv`, and more.

## Code, Libraries, and Tools Used
The repository uses a modern Python environment, strictly requiring Python 3.12+, managed via `uv` (as evidenced by `pyproject.toml` and `uv.lock`).

**Key Libraries & Tools:**
- **Data Manipulation & Analysis:** `pandas`, `numpy`, and `duckdb` (for reading and manipulating data, likely incorporating analytical SQL queries into workflows).
- **Statistical Modeling & Mathematics:** `statsmodels` (for running linear regressions and other statistical modeling) and `scipy` (for scientific and statistical mathematical applications).
- **Visualization:** `seaborn` (for statistical graphics), `squarify` (for treemaps), and `geopandas` (for plotting geo-spatial data, explicitly mapped in the NYC Uber/Lyft datasets).
- **Financial Data:** `yfinance` and `pandas-datareader` for dynamically fetching asset prices and stock market data (used in Session 3 CAPM modeling).
- **Web Scraping:** `bs4` (BeautifulSoup) and `requests` for fetching and parsing HTML data (utilized in the Session 1 UK polls notebook).
- **Environments/Formatting:** `ipykernel` for Jupyter Notebook execution, acting as the primary medium for both teaching and code experimentation.
