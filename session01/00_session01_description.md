# Session 01 Overview

This folder (`session01`) contains a mix of Jupyter notebooks and Python scripts that introduce foundational concepts in data analytics, probability, and statistics, while developing strong programming techniques for simulation, data wrangling, and visualisation. 

## Data and Statistical Concepts Covered

1. **Probability Distributions & The Central Limit Theorem**
   - **Simulations**: Rolling dice and running repeated binomial trials to empirically observe the Central Limit Theorem.
   - **Distributions**: Binomial and Normal (Gaussian) distributions, including modeling real-world cases like university admissions thresholds (forward and inverse cumulative probabilities).

2. **Bootstrapping & Confidence Intervals**
   - **Resampling Methods**: Using bootstrapping to calculate robust confidence intervals for various statistics (mean, median, standard deviation, percentiles).
   - **Binomial Confidence Intervals**: Specialized tests for proportional data tracking.

3. **Exploratory Data Analysis (EDA) & Descriptive Statistics**
   - Examining varied datasets covering Carbon Emissions, Movie Ratings, and the GSS Income database.
   - Understanding distributions via empirical cumulative distribution functions (ECDF), probability mass functions (PMF), and kernel density estimations (KDE).
   - Structuring data cleanly using **Tidy Data principles** (distinguishing wide vs. long data).

## Programming Techniques & Tools

1. **Data Wrangling (`pandas`, `numpy`)**
   - Reading external data and preprocessing it using `pandas` (`read_csv`, `groupby`).
   - **Reshaping Data**: Mastering the transition from wide to long data formats using `pd.melt()`, which strongly enables downstream visualisations.
   - Utilizing `numpy` for efficient array operations and generating random numbers for large-scale Monte Carlo simulations.

2. **Advanced Data Visualisation (`matplotlib`, `seaborn`)**
   - **Matplotlib**: Creating explicit object-oriented plots, managing axes, and formatting tickers (`matplotlib.ticker`).
   - **Seaborn**: Generating high-level statistical graphics, notably using faceted grids (`FacetGrid`), boxplots, histograms, jitter plots, and error bar charts.
   - Exploring niche visualisations, such as Treemaps using the `squarify` library, and visualizing localized regression (LOESS smoothing) via `statsmodels`.

3. **Web Scraping & API Data Collection**
   - **HTML Parsing**: Extracting unstructured data from the web (e.g., UK opinion polls) using `BeautifulSoup`.
   - **APIs & Requests**: Programmatically fetching continuous macro-economic data (FRED Commodity indices).

4. **Software Engineering Practices**
   - **Refactoring & Reusability**: Extracting complex workflows from Jupyter notebooks into reusable Python modules (e.g., `06_bootstrap_function.py`).
   - **Secret Management**: Storing API keys or sensitive variables securely using environment variables (`python-dotenv`).
   - Leveraging statistical libraries such as `scipy.stats` and `statsmodels` for analytical heavy lifting.
